from cycler import cycler
from .colors import bright

default_color_cycler = cycler('color', [bright[key] for key in
                                        ("blue", "red", "green", "yellow", "cyan", "purple", "grey")])

mm2inch = 1 / 25.4

from sys import platform
if platform == "darwin":
    arial = "Arial Unicode MS"
else:
    arial = "Arial"

base_style = {
    "font.family": arial,
    "axes.grid": "False",
    "axes.prop_cycle": default_color_cycler
}


paper = base_style.copy()
paper.update({
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
    })


# font sizes are 5 to 7pt. except the a,b, c panel names that are 8 and bold
paper_nature = base_style.copy()
paper_nature.update({
    "axes.titlesize": "7",
    "axes.labelsize": 7,
    "axes.xmargin": 0,  # x margin.  See `axes.Axes.margins`
    "axes.ymargin": 0,  # y margin.  See `axes.Axes.margins`
    "font.size": "7",
    "legend.fontsize": 5,
    "lines.linewidth": "1",
    "lines.markersize": " 4",
    "xtick.labelsize": "7",
    "ytick.labelsize": "7",
    "axes.formatter.limits": (-3, 4),
    "figure.figsize": (mm2inch * 89, mm2inch * 60),
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
    })

thesis = base_style.copy()
thesis.update({
    "axes.titlesize": "10",
    "axes.labelsize": 10,
    "axes.xmargin": 0,  # x margin.  See `axes.Axes.margins`
    "axes.ymargin": 0,  # y margin.  See `axes.Axes.margins`
    "font.size": "8",
    "legend.fontsize": 8,
    "lines.linewidth": "1",
    "lines.markersize": " 4",
    "xtick.labelsize": "8",
    "ytick.labelsize": "8",
    "axes.formatter.limits": (-3, 4),
    "figure.figsize": (mm2inch * 140, mm2inch * 60),
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
    })


notebook = base_style.copy()
notebook.update({
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
    })
presentation = base_style.copy()
presentation.update({
    "axes.titlesize": 20,
    "axes.labelsize": 18,
    "axes.linewidth": 2,
    "axes.xmargin": 0,  # x margin.  See `axes.Axes.margins`
    "axes.ymargin": 0,  # y margin.  See `axes.Axes.margins`
    "font.size": 16,
    "legend.fontsize": 16,
    "lines.linewidth": 2,
    "lines.markersize": 10,
    "lines.markeredgewidth":2,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16,
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
    })
