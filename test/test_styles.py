
import sacs.matplotlib.styles as styles
import matplotlib as mpl

def test_styles():
    mpl.rcParams.update(styles.paper)
    mpl.rcParams.update(styles.notebook)
    mpl.rcParams.update(styles.presentation)