from cycler import cycler
from functools import wraps
from warnings import warn
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
import colorsys

class color_cycle:
    def __init__(self):
        self.color_map = {
            "Red": "#e60049",
            "Green": "#50e991",
            "Purple": "#9b19f5",
            "Teal": "#00bfa0",
            "Orange": "#ffa300",
            "Pink": "#dc0ab4",
            "Blue": "#0bb4ff",
            "Yellow": "#e6d800",
            "Light Blue": "#b3d4ff"
        }
        self.index = 0
        self.colors = [self.Color(value) for value in self.color_map.values()]
    
    def __getitem__(self, key):
        if key in self.color_map:
            return self.Color(self.color_map[key])
        elif int(key) == key and 0 <= key < len(self.colors):
            return self.colors[key]
        else:
            raise KeyError(f"Invalid key: {key}")

    def __iter__(self):
        return self._ColorIterator(self.colors)
    
    def __next__(self):
        return next(self._ColorIterator(self.colors))

    def reset(self):
        self.index = 0

    @property
    def cmap(self):
        return LinearSegmentedColormap.from_list("custom_palette", [color.color for color in self.colors])

    def categorical_map(self, categories, format='hex'):
        sorted_categories = sorted(categories) # Sort the categories to ensure consistent color mapping
        color_iterator = iter(self)
        color_mapping = [self[category].astype(format) for category in categories]
        return color_mapping

    class _ColorIterator:
        def __init__(self, colors):
            self.colors = colors
            self.index = 0
            self._format = None
        
        def __iter__(self):
            return self
        
        def __next__(self):
            color = self.colors[self.index]
            self.index = (self.index + 1) % len(self.colors)
            return color.astype(self._format)
        
        def astype(self, format):
            self._format = format
            return self
    
    class Color:
        def __init__(self, hex_value):
            self.color = hex_value

        def __repr__(self):
            return self.color

        def __str__(self):
            return self.color
        
        def rgb(self):
            rgb = tuple(int(self.color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
            # Convert to 0-1 scale
            return tuple([c / 255 for c in rgb])
        
        def rgba(self, alpha=1.0):
            return tuple(list(self.rgb()) + [alpha])
        
        def hsv(self):
            return colorsys.rgb_to_hsv(*[c / 255 for c in self.rgb()])
        
        def hls(self):
            return colorsys.rgb_to_hls(*[c / 255 for c in self.rgb()])
        
        def astype(self, format, alpha=1.0):
            if format == 'hex':
                return self.color
            elif format == 'rgb':
                return self.rgb()
            elif format == 'rgba':
                return self.rgba(alpha)
            elif format == 'hsv':
                return self.hsv()
            elif format == 'hls':
                return self.hls()
            elif format is None:
                return self
            else:
                raise ValueError(f"Invalid format: {format}")

    


def can_use_latex():
    try:
        import matplotlib.pyplot as plt
        backend = plt.get_backend()
        plt.switch_backend('pgf')
        plt.switch_backend(backend)
        return True
    except:
        warn('LaTeX is not available. Using standard font instead.')
        return False


def set_plotting_style(plt, use_latex=False):
    # Instantiate the color cycle
    colors = color_cycle()

    
    # Register the custom colormap
    # Unregister the colormap if it already exists
    if mpl.colormaps.get('custom_palette'):
        mpl.colormaps.unregister('custom_palette')
    plt.register_cmap(name='custom_palette', cmap=colors.cmap)

    # Set default figure size
    plt.rc('figure', figsize=(5.5, 4.25))

    # Set x-axis and y-axis ticks
    plt.rc('xtick', direction='in', top=True)
    plt.rc('xtick.major', size=4, width=0.75)
    plt.rc('xtick.minor', size=2, width=0.75, visible=True)
    plt.rc('ytick', direction='in', right=True)
    plt.rc('ytick.major', size=4, width=0.75)
    plt.rc('ytick.minor', size=2, width=0.75, visible=True)

    # Set line widths
    plt.rc('axes', linewidth=1)
    plt.rc('grid', linewidth=1)
    plt.rc('lines', linewidth=2, markeredgewidth=0.8, markersize=4)

    # Set font sizes
    plt.rc('axes', labelsize=16, titlesize=20)
    plt.rc('xtick', labelsize=14)
    plt.rc('ytick', labelsize=14)
    plt.rc('legend', fontsize=15)
    plt.rc('figure', titlesize=17)

    # Refine legend
    plt.rc('legend', frameon=False, loc='best', borderaxespad=0.5, handlelength=2.0)

    # Always save as 'tight'
    plt.rc('savefig', bbox='tight', pad_inches=0.05)

    # Use serif fonts
    plt.rc('font', family='serif')
    plt.rc('mathtext', fontset='dejavuserif')

    if use_latex and can_use_latex():
        # Use LaTeX for math formatting
        plt.rc('text', usetex=True)
        plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{amssymb}')


