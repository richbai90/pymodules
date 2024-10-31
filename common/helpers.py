import sys
import argparse
from os import path
from metavision_core.event_io import EventsIterator, DatWriter
import numpy as np
from toolz import map
from toolz.dicttoolz import valfilter
from toolz.functoolz import pipe, compose
from toolz.itertoolz import first, last
import matplotlib.pyplot as plt
import inspect
from typing import Sequence, Tuple
from functools import partial
from .func_helpers import flatten
from scipy.ndimage import label, center_of_mass
import pandas as pd
from skimage import measure
import pandas as pd
import re
import tempfile
import os
from metavision_sdk_base import EventCDBuffer
'''
A collection of helper functions for the PSF capture project
'''


class FilteredFrameGenerator():
    def __init__(self, frame_gen, *filters):
        self.frame_gen = frame_gen
        self.filters = filters

    def _process_filters(self, evs) -> EventCDBuffer:
        filter_len = len(self.filters)

        def _apply_filter(n, evs, buff):
            if n > filter_len:
                raise ValueError("n must be <= to number of filters")
            if n < 0:
                raise ValueError("n must be >= 0")
            if n == filter_len:
                return evs

            new_buff = self.filters[n].process_events(evs, buff)
            if new_buff is not None:
                # if the events weren't copied directly into buff, use the new buffer
                buff = new_buff

            return _apply_filter(
                n + 1, buff, EventCDBuffer()
            )

        return _apply_filter(0, evs, EventCDBuffer())

    def process_events(self, events):
        events = self._process_filters(events)
        self.frame_gen.process_events(events)


class DataFrameEventsIterator:
    '''
    Drop in replacement for EventsIterator taking a pandas dataframe instead of a file
    '''

    def __init__(
            self, df, start_ts=0, mode='delta_t', delta_t=10000, n_events=10000,
            max_duration=None, relative_timestamps=False, **kwargs):
        self.df = self._prepare_df(df)

        self.start_ts = start_ts
        self.mode = mode
        self.delta_t = delta_t
        self.n_events = n_events
        self.max_duration = max_duration
        self.relative_timestamps = relative_timestamps
        self.kwargs = kwargs
        self.current_time = start_ts
        self.end_ts = df['t'].max(
        ) if max_duration is None else start_ts + max_duration

    def _prepare_df(self, df: pd.DataFrame):
        # t is an integer normally when using EventsIterator
        df['t'] = pd.to_numeric(df['t']).astype(int)
        # sort by t and reset index. t should be monotonic when using EventsIterator
        df.sort_values(by='t').reset_index(drop=True)
        return df

    def __iter__(self):
        return self

    def __next__(self) -> np.ndarray:
        if self.current_time >= self.end_ts:
            raise StopIteration

        if self.mode == 'delta_t' or self.mode == 'mixed':
            df_slice = self.df[(self.df['t'] >= self.current_time) & (
                self.df['t'] < self.current_time + self.delta_t)]
        else:  # mode == 'n_events'
            df_slice = self.df[self.df['t'] >=
                               self.current_time].head(self.n_events)

        if df_slice.empty:
            raise StopIteration

        # Update current_time for the next iteration
        if self.mode == 'delta_t':
            self.current_time += self.delta_t
        elif self.mode == 'n_events':
            if not df_slice.empty:
                self.current_time = df_slice['t'].iloc[-1] + 1
        else:  # mixed mode
            self.current_time = max(
                self.current_time + self.delta_t, df_slice['t'].iloc[-1] + 1)

        if self.relative_timestamps and not df_slice.empty:
            df_slice['t'] -= df_slice['t'].iloc[0]  # Make timestamps relative

        # data type copied from debugger output of EventsIterator
        return df_slice.to_records(
            index=False,
            column_dtypes={'x': 'u2', 'y': 'u2', 'p': 'i2', 't': 'i8'})


class FastFourierFilter():
    def __init__(self, width: int, height: int, min_freq: int, max_freq: int,
                 fps: int) -> None:
        self.width = width
        self.height = height
        self.min_freq = min_freq
        self.max_freq = max_freq
        self._recorded_frames = None
        self.fps = fps
        # require 5 samples of the minimum frequency before attempting to filter
        self._required_samples = int(round((1 / min_freq) * fps * 5))
        self._samples = []

        # make sure that the fps follows the nyquist theorem for accurate results
        assert fps >= 2 * max_freq

    def get_fourier_spectrum(self, evts):
        self._samples.append(evts)
        if len(self._samples) >= self._required_samples:
            all_samples = np.concatenate(self._samples)
            df = pd.DataFrame(all_samples, columns=['x', 'y', 'p', 't'])
            return self._do_fft(df)

    def process_events(self, evts: EventCDBuffer, _: EventCDBuffer):
        self._samples.append(evts)
        if len(self._samples) >= self._required_samples:
            new_buff = self._filter_events()
            self._samples = []
            return new_buff

    def _euclidean_distance(self, point1, point2):
        return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

    def _assign_to_group(self, row, groups, threshold):
        x, y = row['x'], row['y']
        for group_id, group_points in groups.items():
            for point in group_points:
                if self._euclidean_distance(
                    (row['x'],
                     row['y']),
                        point) <= threshold:
                    return group_id

        new_group_id = max(groups.keys(), default=-1) + 1
        groups[new_group_id] = [(x, y)]  # Create a new group with this point
        return new_group_id

    def _apply_fft_to_group(self, group):

        # Extract the 't' values
        time_series = group['t'].values

        # Apply FFT
        return np.fft.fft(time_series)

    def _remove_frequencies(
            self, fft_result, min_freq, max_freq, sampling_rate):
        # Calculate the frequency bins
        n = len(fft_result)
        freqs = np.fft.fftfreq(n, d=1/sampling_rate)

        # Find indices of frequencies to be removed
        min_index = np.searchsorted(freqs, min_freq)
        max_index = np.searchsorted(freqs, max_freq, side='right')

        # Zero out the unwanted frequencies
        fft_result[min_index:max_index] = 0
        fft_result[-max_index:-min_index] = 0  # For negative frequencies

        # Apply inverse FFT
        filtered_time_series = np.fft.ifft(fft_result)

        return filtered_time_series

    def _freq_to_time_domain(self, group):
        t = np.real(np.fft.ifft(group))
        t[t < 0] = 0
        return t

    def _apply_filter(self, row, reconstructed_time_series, groups):
        def convert_to_microseconds(time_series):
            # Convert the time values from seconds to integer microseconds
            return [int(t * 1e6) for t in time_series]

        def find_group_id(x, y, groups):
            # Iterate through the groups to find the group_id for the given (x, y) pair
            for group_id, xy_pairs in groups.items():
                if (x, y) in xy_pairs:
                    return group_id
            return None

        # Find the group_id for the current row
        group_id = find_group_id(row['x'], row['y'], groups)
        p = row['p']
        min_period = 1 / self.min_freq
        t = row['t'] / 1e6
        time_bin = round(t / min_period)
        reconstructed_time_series = reconstructed_time_series.apply(
            convert_to_microseconds)
        # Check if this combination exists in the reconstructed time series
        if (time_bin, group_id, p) in reconstructed_time_series.index:
            # Check if the time value (as integer microseconds) is in
            # the reconstructed time series for this group and polarity
            if row['t'] in reconstructed_time_series.loc[(time_bin, group_id, p)]:
                return True
        return False

    def _do_fft(self, df):

        # convert t to seconds for consistancy in processing
        df['t'] = df['t'] / 1e6

        # Time binning
        min_period = 1 / self.min_freq
        df['time_bin'] = round(df['t'] / min_period)

        # Assuming df is your DataFrame with columns ['x', 'y', 'p', 't']
        threshold_distance = 5  # Set your threshold distance here
        groups = {}

        df['group'] = df.apply(
            lambda row: self._assign_to_group(
                row, groups, threshold_distance),
            axis=1)

        # Now group by time_bin and spatial group
        grouped_df = df.groupby(['time_bin', 'group', 'p'])

        return grouped_df.apply(self._apply_fft_to_group)

    def _filter_events(self):

        # Concatenate samples
        all_samples = np.concatenate(self._samples)
        df = pd.DataFrame(all_samples, columns=['x', 'y', 'p', 't'])
        orig_df = df.copy(deep=True)  # copy the df to keep an original in tact
        fft_results = self._do_fft(df)

        filtered_results = fft_results.apply(
            lambda f: self._remove_frequencies(
                fft_result=f, min_freq=self.min_freq, max_freq=self.max_freq,
                sampling_rate=self.fps))

        reconstructed_time_series = filtered_results.apply(
            self._freq_to_time_domain)

        filtered_df = orig_df[orig_df.apply(
            lambda row: self._apply_filter(
                row, reconstructed_time_series, groups),
            axis=1)]

        structured_array = filtered_df.to_records(
            index=False, column_dtypes={'x': 'u2', 'y': 'u2', 'p': 'i2', 't': 'i8'})
        # copy the data to the buffer
        new_buffer = EventCDBuffer(size=structured_array.size)
        np.copyto(
            new_buffer.numpy(),
            structured_array
        )

        return new_buffer


def evts_to_df(
        event_iterator: EventsIterator, copy=True, **kwargs) -> pd.DataFrame:
    '''
    Convert a raw file to a pandas dataframe. 
    Uses an EventsIterator under the hood and can take the same arguments.

    Parameters
    ----------
    event_iterator : EventsIterator
        The EventsIterator to convert to a dataframe
    **kwargs : dict
        Keyword arguments passed to EventsIterator
    '''
    if copy:
        it = copy_iterator(event_iterator, **kwargs)
    else:
        it = event_iterator
    evts = list(it)
    return pd.concat((pd.DataFrame(evt) for evt in evts), ignore_index=True)


def get_local_path(*parts):
    '''
    Get the path to a file relative to this file

    Parameters
    ----------
    *parts : str
        Path parts

    Returns
    -------
    str
        The path to the file
    '''
    # check if we're running in the context of a jupyter notebook
    try:
        return path.abspath(path.join(path.dirname(__file__), *parts))
    except NameError:
        return path.abspath(
            path.join(path.dirname(path.abspath(__name__)),
                      *parts))


def load_evts_from_file(filename, **kwargs):
    '''
    Load events from a file

    Parameters
    ----------
    filename : str
        The filename to load from
    **kwargs : dict
        Keyword arguments passed to EventsIterator

    Returns
    -------
    np.ndarray
        The events
    '''
    mv_iterator = EventsIterator(input_path=filename, **kwargs)
    return mv_iterator


def load_psf_evts(psf_id, folder='raw'):
    '''
    Load an EventsIterator for a PSF given its ID
    A helper function for load_evts_from_file

    Parameters
    ----------
    psf_id : int
        PSF ID
    folder : str
        Folder to load the PSF from relative to this file

    Returns
    -------
    EventsIterator
        The EventsIterator for the PSF
    '''
    filename = get_local_path('..', 'psf_capture', folder, f'{psf_id}.raw')
    return load_evts_from_file(filename)


def copy_iterator(iterator, **kwargs):
    '''Helper function to copy an iterator without changing the original'''
    return EventsIterator(iterator.reader.path, **kwargs)


def centroid_region(img: np.array, **kwargs) -> float:
    '''
    Compute the centroid of an image and return a bounding box around it
    '''
    defaults = {'crop_factor': 1}
    config = valfilter(lambda x: x is not None, {**defaults, **kwargs})
    # Calculate the image's centroid
    M = measure.moments(img)
    centroid_y, centroid_x = M[1, 0] / M[0, 0], M[0, 1] / M[0, 0]

    # Calculate the minimum distance from the centroid to the image borders
    distances = np.array([
        centroid_x,
        img.shape[1] - centroid_x,
        centroid_y,
        img.shape[0] - centroid_y
    ])
    # scale the distances by the crop factor
    distances *= 1/config['crop_factor']
    half_side_length = np.min(distances)

    # Define bounding box
    min_x = int(centroid_x - half_side_length)
    max_x = int(centroid_x + half_side_length)
    min_y = int(centroid_y - half_side_length)
    max_y = int(centroid_y + half_side_length)

    # Extract bounding region
    region = img[min_y:max_y, min_x:max_x]

    return region


def pad_image(img: np.ndarray, size: Tuple[int]) -> np.ndarray:
    '''
    Pad an image to a given size

    Parameters
    ----------
    img : np.ndarray
        The image to pad
    size : Tuple[int]
        The size to pad the image to
    '''

    padded_img = np.zeros(size, dtype=img.dtype)
    padded_img[:img.shape[0], :img.shape[1]] = img
    return padded_img


def evts_to_img(
        event_iterator: EventsIterator, width: int = 640, height: int = 480, **
        kwargs: dict):
    '''
    Convert a list of events to an image

    Parameters
    ----------
    event_iterator : EventsIterator
        event iterator to convert to an image (e.g. from load_psf_evts)
    width : int
        Width of the image
    height : int
        Height of the image
    **kwargs : dict
        Keyword arguments

    Returns
    -------
    np.ndarray
        The image
    '''

    defaults = {'integration_time': -1, 'start_ts': 0,
                'integrate': False, 'dt': 100e3, 'std': 20, 'noise_floor': 0}
    config = valfilter(lambda x: x is not None, {**defaults, **kwargs})

    # preserve default behavior if integration_time is negative
    integration_time = config['integration_time'] if config['integration_time'] > 0 else None
    start_ts = config['start_ts']

    event_iterator = copy_iterator(
        event_iterator, delta_t=config['dt'],
        start_ts=start_ts, max_duration=integration_time)
    event_iterator.reader.reset()  # Reset the reader

    imgp = np.zeros((height, width), dtype=np.float32)  # Create an empty image
    imgn = np.zeros((height, width), dtype=np.float32)  # Create an empty image
    for evts in event_iterator:
        if not config['integrate']:
            imgp[evts['y'][evts['p'] == 1], evts['x'][evts['p'] == 1]] = 1
            imgn[evts['y'][evts['p'] == 0], evts['x'][evts['p'] == 0]] = 1
        else:  # if we're integrating, add 1 to each pixel
            # only add 1 if there are more than noise_floor events
            if evts.size < config['noise_floor']:
                continue
            np.add.at(imgn, (evts['y'][evts['p'] == 0],
                      evts['x'][evts['p'] == 0]), 1)
            np.add.at(imgp, (evts['y'][evts['p'] == 1],
                      evts['x'][evts['p'] == 1]), 1)

    if config['std'] > -1:
        # clip the images to std standard deviations
        imgp = np.clip(imgp, 0, np.mean(imgp) + config['std'] * np.std(imgp))
        imgn = np.clip(imgn, 0, np.mean(imgn) + config['std'] * np.std(imgn))
    # normalize the images 0 to 1
    imgp = imgp / np.max(imgp)
    imgn = imgn / np.max(imgn)
    return np.array([imgn, imgp])  # Return the images


# we don't care about the other arguments but we need to accept them
def create_grid(num_imgs: int, max_rows=None, max_cols=None, **_):
    '''
    Generate a grid of subplots for a given number of images
    With a maximum number of rows and columns

    Parameters
    ----------
    num_imgs : int
        Number of images
    max_rows : int
        Maximum number of rows
    max_cols : int
        Maximum number of columns

    Returns
    -------
    Sequence[plt.Figure, plt.Axes]
        The figure and axes
    '''
    ideal_rows = int(np.ceil(np.sqrt(num_imgs)))
    ideal_cols = int(np.ceil(np.sqrt(num_imgs)))
    if max_rows is None:
        max_rows = ideal_rows
    elif max_rows < ideal_rows:
        ideal_rows = max_rows
    else:
        max_rows = ideal_rows

    if max_cols is None:
        max_cols = ideal_cols
    elif max_cols < ideal_cols:
        ideal_cols = max_cols
    else:
        max_cols = ideal_cols

    if num_imgs > max_rows * max_cols:
        raise ValueError('Too many images to fit in the grid')

    fig, ax = plt.subplots(max_rows, max_cols)
    return fig, ax  # Return the figure and axes


def gen_image_plot(*imgs: Sequence[np.ndarray], **kwargs):
    '''
    Apply imshow with the given arguments to a list of images and return the figure and axes

    Parameters
    ----------
    img : np.ndarray
        The image to plot
    **kwargs : dict
        Keyword arguments


    Returns
    -------
    Sequence[plt.Figure, plt.Axes]
        The figure and axes
    '''

    def apply_config(config, func):
        """Helper function to apply a config dict to a function's kwargs"""
        valid_keys = filter(
            lambda x: check_keyword_arg(func, x), config.keys())
        return {key: config[key] for key in valid_keys if config[key] is not None}

    # Setup default configurations
    defaults = {
        'title': '', 'cmap': None, 'grid': False, 'colorbar': False,
        'vmin': None, 'vmax': None, 'interpolation': None,
        'max_rows': 4, 'max_cols': None, 'block': False
    }

    # Merge default configurations with provided configurations
    config = {**defaults, **kwargs}

    # Separate configurations for different functions
    imshow_config = apply_config(config, plt.imshow)
    grid_config = apply_config(config, create_grid)
    plot_config = apply_config(config, plt.subplots)

    # Create grid if grid flag is True, else create a single subplot
    create_plot = create_grid if config['grid'] else partial(plt.subplots, 1)
    create_config = grid_config if config['grid'] else plot_config
    # Create plot using the appropriate function
    fig, axs = create_plot(len(imgs), **create_config)

    # Flatten axes array if grid flag is True
    axs = axs.flat if config['grid'] else [axs]

    # Apply imshow to each axis with corresponding image
    img_mappables = [ax.imshow(np.squeeze(img), **imshow_config)
                     for ax, img in zip(axs, imgs)]

    if config['colorbar']:
        map(lambda ax_mappable: plt.colorbar(last(ax_mappable),
            ax=first(ax_mappable)), zip(axs, img_mappables))

    # Set super title if title is provided
    if config['title']:
        fig.suptitle(config['title'])

    # Adjust layout for better appearance
    fig.tight_layout()

    return fig, axs, img_mappables


def check_keyword_arg(func: callable, keyword: str):
    '''
    A helper function to check if a function has a keyword argument.

    Parameters
    ----------
    func : callable
        The function to check.
    keyword : str
        The keyword to check for.

    Returns
    -------
    bool
        True if the function has the keyword argument, False otherwise.
    '''
    params = inspect.signature(func).parameters
    return keyword in params


def crop_image(
        img: np.ndarray, center_x: int, center_y: int, width: int, height: int):
    '''
    Crop an image around a specified center point.

    Parameters
    ----------
    img : np.ndarray
        The input image.
    center_x : int
        The x-coordinate of the center point.
    center_y : int
        The y-coordinate of the center point.
    width : int
        The width of the crop.
    height : int
        The height of the crop.

    Returns
    -------
    np.ndarray
        The cropped image.
    '''
    img_height, img_width = img.shape[:2]

    # Calculate the start and end coordinates for the crop
    start_x = max(center_x - width // 2, 0)
    end_x = min(center_x + width // 2, img_width)
    start_y = max(center_y - height // 2, 0)
    end_y = min(center_y + height // 2, img_height)

    # Extract the crop using array slicing
    crop = img[start_y:end_y, start_x:end_x]

    return crop


def split_img(img: np.ndarray, split_on: Sequence[int] = (255, 255//2)):
    '''
    split the image into 2 images based on the value of the pixel

    Parameters
    ----------
    img: np.ndarray
        the image to split
    split_on: Sequence[int]
        the values to split on

    Returns
    -------
    Sequence[np.ndarray]
        the split images
    '''

    p1 = pipe(np.zeros(img.shape, dtype=np.float32),
              lambda x: np.where(img == split_on[0], 255, x))
    p0 = pipe(np.zeros(img.shape, dtype=np.float32),
              lambda x: np.where(img == split_on[1], 255, x))

    return p0, p1


def event_df_to_time_series(df):
    '''
    Covert an event dataframe to a time series

    Parameters
    ----------
    df: A pandas dataframe to convert
    '''
    # Convert to datetime and set index
    # copy dataframe
    _df = df.copy()
    _df['t'] = pd.to_datetime(_df['t'], unit='us', origin='unix')
    _df.set_index('t', inplace=True)
    return _df


def resample_scale_factor(rate):
    def resample_unit(rate):
        return re.search(r'[a-z]+', rate).group(0)

    unit = resample_unit(rate)
    if unit == 'us':
        return 1e6
    elif unit == 'ms':
        return 1000
    elif unit == 's':
        return 1
    elif unit == 'm':
        return 60
    elif unit == 'h':
        return 3600
    else:
        return 1


def resample_time_series(df, rate, aggregate='count'):
    '''
    Given a time series dataframe resample it to a new rate
    Add elapsed time to the dataframe 
    '''
    def resample_group(group, rate):
        if aggregate == 'count':
            return group.resample(rate, on='t', closed='left', label='left').count() * resample_scale_factor(rate)
        elif aggregate == 'sum':
            return group.resample(rate, on='t', closed='left', label='left').sum() * resample_scale_factor(rate)
        elif aggregate == 'mean':
            return group.resample(rate, on='t', closed='left', label='left').mean() * resample_scale_factor(rate)
        else:
            # TODO: Implement more aggregate functions
            return group.resample(rate, on='t', closed='left', label='left').count() * resample_scale_factor(rate)

    _df = df.copy()
    _df = _df.reset_index()
    _df = _df.resample(rate, closed='left', label='left').count(
    ) * resample_scale_factor(rate)

    # Replace 0 with np.nan and forward fill
    _df.replace(0, np.nan, inplace=True)
    _df.fillna(method='ffill', inplace=True)

    # Reset index for resampled data and calculate elapsed time in milliseconds
    _df = _df.reset_index()
    return _df


def resample_time_series_by_group(df, rate, group_by, aggregate='count'):
    '''
    Given a time series dataframe resample it to a new rate.
    Add elapsed time to the dataframe.
    '''
    def resample_group(group, rate):
        if aggregate == 'count':
            return group.resample(rate, on='t').count()
        elif aggregate == 'sum':
            return group.resample(rate, on='t').sum()
        elif aggregate == 'mean':
            return group.resample(rate, on='t').mean()
        else:
            # Default behavior is count
            return group.resample(rate, on='t').count()

    _df = df.copy()
    _df = _df.reset_index()

    all_groups = []
    for _, group in _df.groupby(group_by):
        resampled = resample_group(group, rate)
        all_groups.append(resampled)

    aggregated_df = pd.concat(all_groups)

    # Replace 0 with np.nan and forward fill
    aggregated_df.replace(0, np.nan, inplace=True)
    aggregated_df.fillna(method='ffill', inplace=True)

    # Reset index for resampled data
    aggregated_df = aggregated_df.reset_index()
    return aggregated_df


def __example():
    col = 9
    row = 0
    psf = load_psf_evts(f'{row}_{col}_545')
    process = compose(
        lambda img: img / np.max(img) if np.max(img) != 0 else img,
        lambda img:
            crop_to_psf(*img, width=64, height=64),
        lambda psf: evts_to_img(psf, start_ts=1e6, integration_time=1e6),
    )

    def normalize_img(img): return img / \
        np.max(img) if np.max(img) != 0 else img

    img_p, img_n = pipe(psf,
                        lambda psf: evts_to_img(
                            psf, start_ts=1e6, integration_time=1e6),
                        # lambda imgs: crop_to_psf(*imgs, width=64, height=64),
                        lambda imgs: map(normalize_img, imgs),
                        list  # convert to list
                        )

    _, axs = gen_image_plot(img_p, img_n, grid=True,
                            colorbar=True, max_rows=1)

    def set_titles(titles): return [ax.set_title(title)
                                    for ax, title in zip(axs, titles)]
    plt.suptitle(f'grid location: ({row}, {col}) λ = 545nm')
    set_titles(['Positive Events', 'Negative Events'])
    axs[0].set_title('Positive Events')
    axs[1].set_title('Negative Events')
    plt.show(block=True)


if __name__ == '__main__':
    # pass
    __example()


class DebugArgParser(argparse.ArgumentParser):
    '''
    A custom argument parser that allows for debugging by reading arguments from a file
    Expects the DEBUG environment variable to be set to True
    Also expects the DEBUG_ARGS_FILE environment variable to be set to the path of the file containing the arguments
    If the DEBUG environment variable is not set, it will parse arguments as normal
    If theDEBUG environment variable is set and DEBUG_ARGS_FILE is not set, it will raise an error
    '''

    def __init__(self, *args, **kwargs):
        arg_file = kwargs.pop('arg_file', None) or kwargs.pop('args_file', None)
        super().__init__(*args, **kwargs)
        self.arg_file = arg_file

    def parse_args(self, args=None, namespace=None):
        # Check if DEBUG mode is enabled
        if os.environ.get("DEBUG", False):
            if args is None and len(sys.argv) <= 1:
                # Look for arguments in a file if specified
                debug_args_file = self.arg_file or os.environ.get(
                    "DEBUG_ARGS_FILE")
                debug_args_file = self._parse_argfile_template(
                    debug_args_file)
                if debug_args_file:
                    try:
                        with open(debug_args_file, "r") as f:
                            args = self._read_args_from_file(f)
                        if not args:
                            raise ValueError(
                                "No arguments provided in the debug args file")
                    except FileNotFoundError:
                        raise FileNotFoundError("Debug args file not found")
                else:
                    raise ValueError("No arguments provided")
            if args is not None:
                parsed_args = super().parse_args(args, namespace)
            else:
                parsed_args = super().parse_args(namespace)
        else:
            parsed_args = super().parse_args(args, namespace)
        return parsed_args

    def _read_args_from_file(self, file_handler):
        args = []
        for line in file_handler:
            # Remove all text after # in each argument
            line = line.split('#')[0].strip()
            if line:
                args.extend(line.split())
        return args

    def _parse_argfile_template(self, argfile):
        if argfile is None:
            return None
        strs = {
            'env': os.environ,
            # Get the filename without the extension
            'filename': os.path.basename(sys.argv[0]).split('.')[0],
            'filedir': os.path.dirname(sys.argv[0]),
        }
        return argfile.format(**strs)


def unzip(zipped_list: Sequence[Tuple]):
    '''
    Unzip a list of tuples

    Parameters
    ----------
    zipped_list : Sequence[Tuple]
        The list of tuples to unzip

    Returns
    -------
    Tuple[Sequence]
        The unzipped list
    '''
    res = [[i for i, j in zipped_list],
           [j for i, j in zipped_list]]

    return tuple(res)
