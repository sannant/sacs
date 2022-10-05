"""
Some of my custom colormaps, norms etc...
"""


# Midpointnormalize


# %% Colors from https://personal.sron.nl/~pault/#sec:qualitative


# qualitataive color schemes

# High contrast color scheme
high_contrast = dict(
    yellow="#DDAA33",
    blue="#004488",
    red="#BB5566",
)

# High contrast color scheme
medium_contrast = {
    "ligh yellow": "#EECC66",
    "light red": "#EE99AA",
    "light blue": "#6699CC",
    "dark yellow": "#997700",
    "dark red": "#994455",
    "dark blue": "#004488",
    }

# Muted color scheme
muted = dict(
    indigo="#332288",
    cyan="88CCEE",
    teal="#44AA99",
    green="#117733",
    olive="#999933",
    sand="#DDCC77",
    rose="#CC6677",
    wine="#882255",
    purple="#AA4499",
    )

muted_dict = muted
muted_default_order = ['#CC6677', '#332288', '#DDCC77', '#117733', '#88CCEE', '#882255', '#44AA99', '#999933', '#AA4499']

# Bright color scheme:
bright = dict(
    blue="#4477AA",
    cyan="#66CCEE",
    green="#228833",
    yellow="#CCBB44",
    red="#EE6677",
    purple="#AA3377",
    grey="#BBBBBB",
    )
#
# To use in Latex:
#\definecolor{tol-bright-blue}{HTML}{4477AA}
#\definecolor{tol-bright-cyan}{HTML}{66CCEE}
#\definecolor{tol-bright-green}{HTML}{228833}
#\definecolor{tol-bright-yellow}{HTML}{CCBB44}
#\definecolor{tol-bright-red}{HTML}{EE6677}
#\definecolor{tol-bright-purple}{HTML}{AA3377}
#\definecolor{tol-bright-grey}{HTML}{BBBBBB}

# Diverging colour schemes
sunset =  ['#364B9A', '#4A7BB7', '#6EA6CD', '#98CAE1', '#C2E4EF', '#EAECCC', '#FEDA8B', '#FDB366', '#F67E4B', '#DD3D2D', '#A50026']
sunset_bad_data = '#FFFFFF'
BuRd = ['#2166AC', '#4393C3', '#92C5DE', '#D1E5F0', '#F7F7F7', '#FDDBC7', '#F4A582', '#D6604D', '#B2182B']
BuRd_bad_data = '#FFEE99'
PRGn = ['#762A83', '#9970AB', '#C2A5CF', '#E7D4E8', '#F7F7F7', '#D9F0D3', '#ACD39E', '#5AAE61', '#1B7837']
PRGn_bad_data = '#FFEE99'

