import numpy as np
import h5py
import os
import logging
from time import time_ns
from numbers import Number
from sklearn.neighbors import KDTree

class DynamicDiskBackedArray:
    def __init__(
            self, filename, shape, dtype=np.float32, batch_size=100,
            resize_factor=4, record_timestamps=False):

        shape = (0,) + shape[:]  # Add a dimension to append to
        # Allow the dataset to be resized to an arbitrary length along the first dimension
        max_shape = (None,) + shape[1:]
        self.filename = filename
        self.dtype = dtype
        # Chunk size is 10 along the first dimension
        self.chunk_size = (25,) + shape[1:]
        self.batch_size = batch_size
        self.resize_factor = resize_factor  # New attribute to control anticipated resizing
        self.buffer = []  # Initialize an empty buffer for batching
        self.dataset_name = 'data'
        self.data_length = 0  # Initialize the length of the dataset
        self.record_timestamps = record_timestamps

        if not os.path.exists(filename):
            with h5py.File(filename, 'w') as f:
                try:
                    self.dataset = f.create_dataset(
                        self.dataset_name, shape=shape, maxshape=max_shape,
                        dtype=dtype, chunks=self.chunk_size,)
                    self.tsset = f.create_dataset(
                        'timestamps', shape=(0,), maxshape=(None,), dtype=np.float64
                    )
                except Exception as e:
                    print(e)
        self.refresh()

    def refresh(self):
        """Refresh the in-memory handle to the dataset."""
        self.file = h5py.File(self.filename, 'a')
        self.dataset = self.file[self.dataset_name]
        self.tsset = self.file['timestamps']

    def append(self, data, ts=None):
        """Append data to the buffer, and flush if necessary."""
        if ts is None:
            ts = time_ns()
        elif not isinstance(ts, Number):
            raise ValueError("Timestamp must be a number")
        self.buffer.append((data, ts))
        if len(self.buffer) >= self.batch_size:
            return self.flush()
        return True

    def truncate(self):
        '''Remove any padding from the dataset, resizing it to the minimum size necessary to contain the data.'''
        self.dataset.resize(self.data_length, axis=0)
        if self.record_timestamps:
            self.tsset.resize(self.data_length, axis=0)
        
    def flush(self) -> bool:
        """Flush the buffer to the disk, resizing the dataset with anticipation."""
        if not self.buffer:
            return  # Nothing to flush
        try:
            # data = np.concatenate([np.asarray(item, self.dtype) for item in self.buffer], axis=0)
            # This stacks along a new first axis, creating a shape (N, *shape)
            data, ts = zip(*self.buffer)
            data = np.stack(data, axis=0)
            ts = np.array(ts, dtype=np.float64)  # Convert timestamps to a numpy array
            self.data_length += len(data)
            # Only resize if the required size is greater than the current size
            if self.data_length > self.dataset.shape[0]:
                new_size = int(max(1, self.data_length) * self.resize_factor) # Anticipate the new size
                self.dataset.resize(new_size, axis=0)
                if self.record_timestamps:
                    self.tsset.resize(new_size, axis=0)

            # Ensure data is written to the correct location
            # The location is determined by the current dataset size minus the buffer size
            start_index = self.data_length - len(data) # The start index of the new data
            end_index = start_index + data.shape[0]
            self.dataset[start_index:end_index, ...] = data
            if self.record_timestamps:
                self.tsset[start_index:end_index] = ts
        except Exception as e:
            self.data_length -= len(self.buffer)  # Revert the data length if an error occurs
            logging.error(f"Error flushing data to disk: {e}")
            return False
        self.buffer = []  # Clear the buffer after flushing
        return True

    def __getitem__(self, item):
        self.flush()  # Ensure all data is written before reading
        return self.dataset[item]

    def close(self):
        """Close the file properly, ensuring the buffer is flushed."""
        self.flush()  # Flush any remaining data in the buffer
        self.truncate()
        self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def test_dynamic_diskbacked_array():
    filename = 'test.h5'
    shape = (3, 3)
    with DynamicDiskBackedArray(filename, shape, record_timestamps=True) as d:
        for i in range(500):
            d.append(np.random.random(shape))
        print(d[0:10])
        print(d[0:10].shape)

class EnhancedDataKDTree(KDTree):
    '''
    An enhanced KDTree class that extends the functionality of the KDTree class from scipy.spatial.
    Supports mapping of query indices to data indices, and returns data corresponding to the nearest neighbors.
    '''
    def __init__(self, points, data, mapping_function=None, **kwargs):
        """
        Initializes an enhanced KDTree with extended functionality and validations.

        Parameters:
        - points (array-like): 2D data points for building the KDTree.
        - data (List or array): Data corresponding to each point.
        - mapping_function (function, optional): Customizable function to map query indices to 'data' indices.
        - kwargs: Additional arguments passed to scipy.spatial.KDTree.
        """
        if not len(points) == len(data):
            raise ValueError("The lengths of 'points' and 'data' must be identical.")
        if not isinstance(data, (list, np.ndarray)):
            raise TypeError("'data' must be either a list or a numpy array.")
        if len(data) == 0:
            raise ValueError("'data' cannot be empty.")

        # Initialize the KDTree with specified metric and leaf size
        super().__init__(np.asarray(points), **kwargs)
        self._data = np.asarray(data)
        # Allow for a default mapping function that simplifies custom mappings
        self.mapping_function = mapping_function if mapping_function else lambda _, i: i

    def query(self, x, k=1, return_distance=True, **kwargs):
        """
        Extends the KDTree query method to return nearest neighbors along with associated 'data'.

        Parameters:
        - x (array-like): Query point(s) in a 2D array.
        - k (int, optional): Number of nearest neighbors to return.
        - return_distance (bool, optional): Indicates if distances to nearest neighbors should be returned.
        - kwargs: Additional arguments for the query method.

        Returns:
        Tuple of (distances, indices, data) if return_distance=True; otherwise, (indices, data).
        """
        x = np.atleast_2d(x)

        # Perform the query using the parent's method. The unpacking accounts for return_distance flag automatically.
        results = super().query(x, k=k, return_distance=return_distance, **kwargs)

        if return_distance:
            distances, indices = results
        else:
            indices = results

        points = np.asanyarray([tuple(self.data[i, :]) for i in indices.ravel()])
        # Retrieve data corresponding to found indices using the mapping function.
        # This step is significantly optimized by vectorizing the mapping and indexing operations.
        mapped_indices = self.mapping_function(points, indices.ravel()) 
        data_results = np.asarray(self._data[mapped_indices]) # Ensure data_results is a numpy array for consistency

        # Reshape data_results if multiple neighbors are requested (k > 1).
        if k > 1:
            data_results = data_results.reshape(indices.shape)

        return (distances, indices, data_results) if return_distance else (indices, data_results)
    
