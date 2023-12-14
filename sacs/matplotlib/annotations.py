import numpy as np
from matplotlib.patches import FancyArrowPatch
from math import atan2

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
    artist = FancyArrowPatch((xs, ys), (xe, ye), **arrow_prop_dict)
    ax.add_artist(artist)
    if label is not None:
        ox, oy = labeloffset
        if labelpos == "end":
            ax.text(xe + ox, ye + oy, label, **textprops)
        elif labelpos == "start":
            ax.text(xs + ox, ys + oy, label, **textprops)
        elif labelpos == "center":
            ax.text((xe + xs) / 2 + ox, (ye + ys) / 2 + oy, label, **textprops)
    return artist


import numpy as np
from math import atan2


def label_line(line, x, label=None, rotation=None, **kwargs):
    ax = line.axes
    xdata = line.get_xdata()
    ydata = line.get_ydata()
    if (x < xdata[0]) or (x > xdata[-1]):
        print('x label location is outside data range!')
        return
    # Find corresponding y co-ordinate and angle of the
    ip = 1
    for i in range(len(xdata)):
        if x < xdata[i]:
            ip = i
            break
    y = ydata[ip - 1] + (ydata[ip] - ydata[ip - 1]) * (x - xdata[ip - 1]) / (xdata[ip] - xdata[ip - 1])
    if not label:
        label = line.get_label()
    if rotation is not None:
        trans_angle = rotation
    else:
        # Compute the slope
        dx = xdata[ip] - xdata[ip - 1]
        dy = ydata[ip] - ydata[ip - 1]
        ang = np.degrees(atan2(dy, dx))
        # Transform to screen co-ordinates
        pt = np.array([x, y]).reshape((1, 2))
        trans_angle = ax.transData.transform_angles(np.array((ang,)), pt)[0]
    # Set a bunch of keyword arguments
    if 'color' not in kwargs:
        kwargs['color'] = line.get_color()
    if ('horizontalalignment' not in kwargs) and ('ha' not in kwargs):
        kwargs['ha'] = 'center'
    if ('verticalalignment' not in kwargs) and ('va' not in kwargs):
        kwargs['va'] = 'center'
    if 'backgroundcolor' not in kwargs:
        kwargs['backgroundcolor'] = ax.get_facecolor()
    if 'clip_on' not in kwargs:
        kwargs['clip_on'] = True
    if 'zorder' not in kwargs:
        kwargs['zorder'] = 2.5
    ax.text(x, y, label, rotation=trans_angle, **kwargs)


def label_lines(lines, xvals=None, rotations=None, **kwargs):
    ax = lines[0].axes
    labLines = []
    labels = []
    # Take only the lines which have labels other than the default ones
    for line in lines:
        label = line.get_label()
        if "_line" not in label:
            labLines.append(line)
            labels.append(label)
    if xvals is None:
        xmin, xmax = ax.get_xlim()
        xvals = np.linspace(xmin, xmax, len(labLines) + 2)[1:-1]

    if rotations is None:
        rotations = [None] * len(labLines)
    for line, x, label, rotation in zip(labLines, xvals, labels, rotations):
        label_line(line, x, label, rotation, **kwargs)