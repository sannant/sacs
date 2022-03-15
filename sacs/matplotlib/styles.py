from cycler import cycler

from .colors import bright

default_color_cycler = cycler('color', [bright[key] for key in
                                        ("blue", "red", "green", "yellow", "cyan", "purple", "grey")])

paper = {
    "font.family": "Arial Unicode MS",
    "axes.titlesize": "8",
    "axes.labelsize": 8,
    "axes.xmargin": 0,  # x margin.  See `axes.Axes.margins`
    "axes.ymargin": 0,  # y margin.  See `axes.Axes.margins`
    "font.size": "8",
    "legend.fontsize": 7,
    "lines.linewidth": "1",
    "lines.markersize": " 4",
    "xtick.labelsize": " 8",
    "ytick.labelsize": "8",
    "axes.formatter.limits": (-3, 4),
    "figure.figsize": "3.4, 2.36",
    "figure.titlesize": "small",
    "figure.subplot.left": " 0.15",  ## the left side of the subplots of the figure"
    "figure.subplot.right": " 0.95",  ## the right side of the subplots of the figure"
    "figure.subplot.bottom": " 0.15",  ## the bottom of the subplots of the figure"
    "figure.subplot.top": "0.95",  ## the top of the subplots of the figure"
    "figure.subplot.wspace": "0.15",  ## the amount of width reserved for space between subplots,"
    ## expressed as a fraction of the average axis width
    "figure.subplot.hspace": " 0.1",  ## the amount of height reserved for space between subplots,"
    ## expressed as a fraction of the average axis height
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "axes.grid": "False",
    "axes.prop_cycle": default_color_cycler
    }

notebook = {
    "font.family": "Arial Unicode MS",
    "axes.titlesize": "8",
    "axes.labelsize": 8,
    "axes.xmargin":   0,  # x margin.  See `axes.Axes.margins`
    "axes.ymargin":  0,  # y margin.  See `axes.Axes.margins`
    "font.size": "8",
    "legend.fontsize": 7,
    "lines.linewidth": "1",
    "lines.markersize": " 4",
    "xtick.labelsize": " 8",
    "ytick.labelsize": "8",
    "axes.formatter.limits": (-3, 4),
    "figure.figsize": "3.9, 1.5",
    "figure.titlesize": "small",
    "figure.subplot.left": " 0.15",  ## the left side of the subplots of the figure"
    "figure.subplot.right": " 0.95",  ## the right side of the subplots of the figure"
    "figure.subplot.bottom": " 0.15",  ## the bottom of the subplots of the figure"
    "figure.subplot.top": "0.95",  ## the top of the subplots of the figure"
    "figure.subplot.wspace": "0.15",  ## the amount of width reserved for space between subplots,"
    ## expressed as a fraction of the average axis width
    "figure.subplot.hspace": " 0.1",  ## the amount of height reserved for space between subplots,"
    ## expressed as a fraction of the average axis height
    "figure.dpi": 200,
    "savefig.dpi": 300,
    "axes.grid": "False",
    "axes.prop_cycle": default_color_cycler
    }
presentation = {
    "font.family": "Arial Unicode MS",
    "axes.titlesize": 20,
    "axes.labelsize": 18,
    "font.size": 16,
    "legend.fontsize": 16,
    "lines.linewidth": 2,
    "lines.markersize": 10,
    "xtick.labelsize": 18,
    "ytick.labelsize": 18,
    "axes.formatter.limits": (-40, 40),
    "axes.formatter.useoffset": False,
    "figure.subplot.left": 0.2,
    "figure.subplot.right": 0.9,
    "figure.subplot.bottom": 0.11,
    "figure.subplot.top": 0.88,
    "figure.subplot.wspace": 0.3,
    "figure.subplot.hspace": 0.2,
    "figure.dpi": 200,
    "savefig.dpi": 300,
    "axes.grid": False,
    "axes.prop_cycle": default_color_cycler
    }
