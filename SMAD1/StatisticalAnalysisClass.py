import numpy as np
import matplotlib.pyplot as plt


class StatisticalAnalysis:

    def __init__(self, data):
        self.data = np.array(data)
        self.n = len(data)

    def frequencies(self):
        unique, counts = np.unique(self.data, return_counts=True)
        freq = counts / self.n
        rel_freq = freq * 100
        return unique, counts, freq, rel_freq

    def mean(self):
        return np.mean(self.data)

    def median(self):
        return np.median(self.data)

    def mode(self):
        unique, counts = np.unique(self.data, return_counts=True)
        idx = np.argmax(counts)
        return unique[idx]

    def range(self):
        return np.max(self.data) - np.min(self.data)

    def variance(self):
        return np.var(self.data, ddof=0)

    def std_dev(self):
        return np.std(self.data, ddof=0)

    def corrected_variance(self):
        return np.var(self.data, ddof=1)

    def corrected_std_dev(self):
        return np.std(self.data, ddof=1)

    def coefficient_of_variation(self):
        return self.std_dev() / self.mean() * 100

    def central_moments(self, k):
        return np.mean((self.data - self.mean()) ** k)

    def skewness(self):
        return self.central_moments(3) / self.std_dev() ** 3

    def kurtosis(self):
        return self.central_moments(4) / self.std_dev() ** 4 - 3

    def empirical_cdf(self, x):
        count = 0
        for value in self.data:
            if value <= x:
                count += 1
        return count / self.n

    def plot_histogram(self):
        plt.hist(self.data, bins='auto', alpha=0.5, edgecolor='black', width=0.4)
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Histogram')
        plt.show()

    def plot_polygon(self):
        unique, _, freq, _ = self.frequencies()
        plt.plot(unique, freq, marker='o')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Polygon')
        plt.show()

    def plot_cumulative_curve(self):
        unique, _, _, rel_freq = self.frequencies()
        cum_freq = np.cumsum(rel_freq)
        plt.plot(unique, cum_freq, marker='o')
        plt.xlabel('Values')
        plt.ylabel('Cumulative Frequency')
        plt.title('Cumulative Curve')
        plt.show()

    def plot_empirical_cdf(self):
        data_sorted = np.sort(self.data)
        n = len(data_sorted)
        y = np.arange(1, n+1) / n
        plt.step(data_sorted, y)
        plt.xlabel('Values')
        plt.ylabel('Cumulative Probability')
        plt.title('Empirical CDF')
        plt.show()
