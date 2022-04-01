import matplotlib as mpl
import numpy as np
import scipy as sp
import sacs


class MidpointNormalize(mpl.colors.Normalize):
    def __init__(self, vmin, vmax, midpoint=0, clip=False):
        self.midpoint = midpoint
        mpl.colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        normalized_min = max(0, 1 / 2 * (1 - abs((self.midpoint - self.vmin) / (self.midpoint - self.vmax))))
        normalized_max = min(1, 1 / 2 * (1 + abs((self.vmax - self.midpoint) / (self.midpoint - self.vmin))))
        normalized_mid = 0.5
        x, y = [self.vmin, self.midpoint, self.vmax], [normalized_min, normalized_mid, normalized_max]
        return sp.ma.masked_array(sp.interp(value, x, y))

    def inverse(self, value):
        normalized_min = max(0, 1 / 2 * (1 - abs((self.midpoint - self.vmin) / (self.midpoint - self.vmax))))
        normalized_max = min(1, 1 / 2 * (1 + abs((self.vmax - self.midpoint) / (self.midpoint - self.vmin))))
        normalized_mid = 0.5
        return np.interp(value, [normalized_min, normalized_mid,
                                 normalized_max], [self.vmin, self.midpoint, self.vmax])

# https://github.com/Descanonge/tol_colors/blob/5815a3cb74834f70b56e0e131c1ff73bd51e0df4/src/tol_colors/__init__.py#L48-L56
"""
Copyright (c) 2019, Paul Tol
All rights reserved.
License:  Standard 3-clause BSD
"""

def discretemap(colormap_name, hexclrs):
    """Produce a colormap from a list of discrete colors without interpolation."""
    clrs = to_rgba_array(hexclrs)
    clrs = np.vstack([clrs[0], clrs, clrs[-1]])
    cdict = {}
    for ki, key in enumerate(('red', 'green', 'blue')):
        cdict[key] = [(i/(len(clrs)-2.), clrs[i, ki], clrs[i+1, ki])
                      for i in range(len(clrs)-1)]
    return mpl.colors.LinearSegmentedColormap(colormap_name, cdict)

# How to make a normal colormap
# cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
# cmap.set_bad('#999999')

def get_cmap(cmap):
    c = mpl.colors.LinearSegmentedColormap.from_list(cmap, sacs.matplotlib.colors.__dict__[cmap])
    c.set_bad(sacs.matplotlib.colors.__dict__[cmap+"_bad_data"])
    return c