import numpy as np
from matplotlib.patches import FancyArrowPatch


def asscalar(a):
    if isinstance(a, np.ndarray):
        return asscalar(a.tolist()[0])
    elif isinstance(a, (list, tuple)):
        return asscalar(a[0])
    else:
        return a


def arrow(ax, start, end=None, delta=None, arrowprops={}, label=None,
                   textprops={}, labelpos="end", labeloffset=(0, 0)):
    arrow_prop_dict = dict(mutation_scale=10, arrowstyle='-|>', color='k', shrinkA=0, shrinkB=0)
    for key in arrowprops:
        arrow_prop_dict[key] = arrowprops[key]

    xs = asscalar(start[0])
    ys = asscalar(start[1])

    if end is not None:
        xe = asscalar(end[0])
        ye = asscalar(end[1])
    elif delta is not None:
        xe = xs + asscalar(delta[0])
        ye = ys + asscalar(delta[1])
    else:
        raise AssertionError('Missing Argument end or delta')

    ax.add_artist(FancyArrowPatch((xs, ys), (xe, ye), **arrow_prop_dict))
    if label is not None:
        ox, oy = labeloffset
        if labelpos == "end":
            ax.text(xe + ox, ye + oy, label, **textprops)
        elif labelpos == "start":
            ax.text(xs + ox, ys + oy, label, **textprops)
        elif labelpos == "center":
            ax.text((xe + xs) / 2 + ox, (ye + ys) / 2 + oy, label, **textprops)
