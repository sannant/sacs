import numpy as np


class Histogram:
    def __init__(self, values, bin_space):
        v_min = np.min(values)
        v_max = np.max(values)

        n_bins = int(v_max - v_min) / bin_space
        bins = np.arange(n_bins) / n_bins * (v_max - v_min) + v_min

        self.probability_density, self.bin_edges = np.histogram(values, bins=bins, density=True)

    @property
    def bin_centers(self):
        return (self.bin_edges[1:] + self.bin_edges[:-1]) / 2

    @property
    def bin_widths(self):
        return (self.bin_edges[1:] - self.bin_edges[:-1])

    @property
    def cdf(self):
        return np.cumsum(self.probability_density * self.bin_widths)

    def plot(self):
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()

        ax.plot(self.bin_centers, self.probability_density, c="k")
