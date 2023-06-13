import matplotlib.pyplot as plt
import numpy as np

class StatisticalAnalysis1:

    def __init__(self, data):
        self.data = data
        self.n = len(data)

    def frequencies(self):
        #wihout numpy
        unique = []
        counts = []
        for value in self.data:
            if value not in unique:
                unique.append(value)
                counts.append(1)
            else:
                counts[unique.index(value)] += 1
        freq = [count / self.n for count in counts]
        rel_freq = [f * 100 for f in freq]
        return unique, counts, freq, rel_freq

    def mean(self):
        return sum(self.data) / self.n

    def median(self):
        data_sorted = sorted(self.data)
        if self.n % 2 == 0:
            return (data_sorted[self.n // 2 - 1] + data_sorted[self.n // 2]) / 2
        else:
            return data_sorted[self.n // 2]

    def mode(self):
        unique, counts = self.frequencies()[:2]
        idx = counts.index(max(counts))
        return unique[idx]

    def range(self):
        return max(self.data) - min(self.data)

    def variance(self):
        return sum((x - self.mean()) ** 2 for x in self.data) / self.n

    def std_dev(self):
        return self.variance() ** 0.5

    def corrected_variance(self):
        return sum((x - self.mean()) ** 2 for x in self.data) / (self.n - 1)

    def corrected_std_dev(self):
        return self.corrected_variance() ** 0.5

    def coefficient_of_variation(self):
        return self.std_dev() / self.mean() * 100

    def central_moments(self, k):
        return sum((x - self.mean()) ** k for x in self.data) / self.n

    def starting_moment(self, k):
        return sum(x ** k for x in self.data) / self.n

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

    def plot_polygon(self):
        unique, counts = self.frequencies()[:2]
        #curve
        plt.step(unique, counts, where='post')
        plt.xlabel('Values')
        plt.ylabel('Frequencies')
        plt.title('Polygon')
        plt.show()

    def plot_cumulative_freq(self):
        print('plot_cumulative_freq')

    def plot_relative_polygon(self):
        print('plot_relative_polygon')

    def plot_relative_cumulative(self):
        print('plot_relative_cumulative')

    def plot_empirical_cdf(self):
        data_sorted = sorted(self.data)
        n = len(data_sorted)
        y = [i / n for i in range(1, n + 1)]
        plt.step(data_sorted, y)
        plt.xlabel('Values')
        plt.ylabel('Cumulative Probability')
        plt.title('Empirical CDF')
        plt.show()
