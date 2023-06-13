import matplotlib.pyplot as plt
import numpy as np

class StatisticalAnalysis:

    def __init__(self, data):
        self.data = data
        self.n = len(data)

    def calculate_intervals(self):
        k = 2 + int(np.log2(self.n))
        interval_size = (max(self.data) - min(self.data)) / k
        intervals = []
        for i in range(k):
            lower_limit = min(self.data) + i * interval_size
            upper_limit = lower_limit + interval_size
            intervals.append((lower_limit, upper_limit))
        return intervals

    def calculate_frequencies(self):
        intervals = self.calculate_intervals()
        freq = np.zeros(len(intervals))
        for i, interval in enumerate(intervals):
            for value in self.data:
                if interval[0] <= value < interval[1]:
                    freq[i] += 1
        rel_freq = freq / self.n
        return freq, rel_freq, intervals

    def mean(self):
        return sum(self.data) / self.n

    def median(self):
        data_sorted = sorted(self.data)
        if self.n % 2 == 0:
            return (data_sorted[self.n // 2 - 1] + data_sorted[self.n // 2]) / 2
        else:
            return data_sorted[self.n // 2]

    def mode(self):
        freq, _, intervals = self.calculate_frequencies()
        idx = np.argmax(freq)
        return intervals[idx]

    def calculate_median_interval(self):
        freq, _, intervals = self.calculate_frequencies()
        idx = np.argmax(freq)
        if idx == 0:
            return intervals[0]
        elif idx == len(freq) - 1:
            return intervals[-1]
        else:
            return intervals[idx - 1], intervals[idx + 1]

    def calculate_mode(self):
        freq, _, intervals = self.calculate_frequencies()
        idx = np.argmax(freq)  # індекс модального інтервалу
        mode_interval = intervals[idx]  # модальний інтервал
        h = mode_interval[1] - mode_interval[0]  # довжина модального інтервалу
        left_freq = freq[idx - 1] if idx > 0 else 0  # частота попереднього інтервалу
        right_freq = freq[idx + 1] if idx < len(freq) - 1 else 0  # частота наступного інтервалу

        # частота післямодального інтервалу
        post_freq = freq[idx + 1] if idx < len(freq) - 1 else 0

        # порівнюємо частоти і повертаємо більш ймовірне значення моди
        if left_freq > right_freq + 100:
            return mode_interval[0] + h * (freq[idx - 1] - freq[idx]) / (2 * freq[idx] - freq[idx - 1] - freq[idx + 1])
        elif right_freq > left_freq:
            return mode_interval[0] + h * (freq[idx + 1] - freq[idx]) / (2 * freq[idx] - freq[idx - 1] - freq[idx + 1])
        else:
            # обидва інтервали мають однакову частоту
            if post_freq == 0:
                # модальний інтервал є останнім інтервалом
                return (mode_interval[0] + mode_interval[1]) / 2
            else:
                return mode_interval[0] + h * (freq[idx + 1] - freq[idx]) / (
                            2 * freq[idx] - freq[idx - 1] - freq[idx + 1])

    def calculate_median(self, interval, freq, n):
        '''Функція для обчислення медіани

        параметри:
        interval - список інтервалів
        freq - список частот
        n - кількість елементів вибірки
        '''
        width = interval[1] - interval[0]
        cum_freq = np.cumsum(freq)
        median_pos = n / 2
        for i in range(len(cum_freq)):
            if cum_freq[i] >= median_pos:
                median_interval = interval[i]
                break
        lower_bound = median_interval[0]
        freq_within_median = freq[i]
        median = lower_bound + ((median_pos - cum_freq[i - 1]) / freq_within_median) * width
        return median


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

    def central_moment(self, k):
        return sum((x - self.mean()) ** k for x in self.data) / self.n

    def starting_moment(self, k):
        return sum(x ** k for x in self.data) / self.n

    def skewness(self):
        return self.central_moment(3) / self.std_dev() ** 3

    def kurtosis(self):
        return self.central_moment(4) / self.std_dev() ** 4 - 3

    def empirical_cdf(self, x):
        count = 0
        for value in self.data:
            if value <= x:
                count += 1
        return count / self.n

    def plot_histogram(self):
        # Створення гістограми за частотами
        plt.hist(self.data, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.99)
        plt.xlabel('Значення')
        plt.ylabel('Частота')
        plt.title('Гістограма за частотами')
        plt.show()

        # Створення гістограми за відносними частотами
        plt.hist(self.data, bins='auto', density=True, color='#0504aa', alpha=0.7, rwidth=0.99)
        plt.xlabel('Значення')
        plt.ylabel('Відносна частота')
        plt.title('Гістограма за відносними частотами')
        plt.show()

    def plot_cumulative_curve(self):
        # Кумулятивна крива за частотами
        counts, bin_edges = np.histogram(self.data, bins='auto')
        cdf = np.cumsum(counts)
        plt.plot(bin_edges[1:], cdf, color='#0504aa', alpha=0.7)
        plt.xlabel('Значення')
        plt.ylabel('Частота')
        plt.title('Кумулятивна крива за частотами')
        plt.show()

        # Кумулятивна крива за відносними частотами
        counts, bin_edges = np.histogram(self.data, bins='auto', density=True)
        cdf = np.cumsum(counts)
        plt.plot(bin_edges[1:], cdf, color='#0504aa', alpha=0.7)
        plt.xlabel('Значення')
        plt.ylabel('Відносна частота')
        plt.title('Кумулятивна крива за відносними частотами')
        plt.show()

    # def plot_empirical_distribution(self):
    #     y_values = []
    #     for element in x_values:
    #         sum = 0 if len(y_values) == 0 else y_values[-1]
    #         y_values.append(sum + value_occurances[element])
    #     y_values = [y / len(data) for y in y_values]
    #     x_values = [x_values[0] - 0.2] + x_values + [x_values[-1] + 0.2]
    #     y_values = [0] + y_values
    #     fig, ax = plt.subplots()
    #     for i, element in enumerate(y_values):
    #         plt.plot([x_values[i], x_values[i + 1]], [element, element], "b-")
    #     ax.set(title="Емпірична функція розподілу")
    #     ax.grid()
    #     plt.show()

    def plot_empirical_distribution(self):
        num_intervals = 8
        data_min = min(self.data)
        data_max = max(self.data)
        interval_width = (data_max - data_min) / num_intervals
        x_values = [data_min + i * interval_width for i in range(num_intervals + 1)]
        value_occurances = np.histogram(self.data, bins=x_values)[0]
        y_values = []
        for i in range(num_intervals):
            sum = 0 if len(y_values) == 0 else y_values[-1]
            y_values.append(sum + value_occurances[i])
        y_values = [y / len(self.data) for y in y_values]
        x_values = [x_values[0] - 0.2] + x_values + [x_values[-1] + 0.2]
        y_values = [0] + y_values + [1.0]
        fig, ax = plt.subplots()

        for i, element in enumerate(y_values):
            plt.plot([x_values[i], x_values[i + 1]], [element, element], "b-")
        ax.set(title="Емпірична функція розподілу")
        ax.grid()
        plt.show()




