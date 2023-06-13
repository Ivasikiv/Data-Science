import numpy as np
from matplotlib import pyplot as plt
from StatisticalAnalysisClass import StatisticalAnalysis
from StatisticalAnalysisClass1 import StatisticalAnalysis1

data = [-5.0, -4.9, -4.8, -4.7, -4.6, -4.5, 4.7, 4.8, 4.9, 4.9, 4.9, 5.0]
analysis = StatisticalAnalysis1(data)

# обчислення дискретного статистичного ряду та виведення на екран
unique, counts, freq, rel_freq = analysis.frequencies()
print("Таблиця дискретної статистики:")
print("{:^10} {:^10} {:^10}".format("Значення", "Частота", "Відносна частота"))
for i in range(len(unique)):
    cum_freq = np.cumsum(rel_freq)[:i+1][-1]
    print("{:^10.1f} {:^10} {:^10.2f}%".format(unique[i], counts[i], rel_freq[i]))

print("")
print("Основні числові параметри:")
print("{:<25} {:.2f}".format("Середнє статистичне:", analysis.mean()))
print("{:<25} {:.2f}".format("Медіана:", analysis.median()))
print("{:<25} {:.2f}".format("Мода:", analysis.mode()))
print("{:<25} {:.2f}".format("Розмах:", analysis.range()))
print("")
print("{:<25} {:.2f}".format("Дисперсія:", analysis.variance()))
print("{:<25} {:.2f}".format("Середнє квадратичне відхилення:", analysis.std_dev()))
print("")
print("{:<25} {:.2f}".format("Виправлена дисперсія:", analysis.corrected_variance()))
print("{:<25} {:.2f}".format("Виправлене середнє квадратичне відхилення:", analysis.corrected_std_dev()))
print("")
print("{:<25} {:.2f}%".format("Коефіцієнт варіації:", analysis.coefficient_of_variation()))
print("")
print("{:<25} {:.2f}".format("Початковий момент 2-го порядку:", analysis.starting_moment(2)))
print("{:<25} {:.2f}".format("Початковий момент 3-го порядку:", analysis.starting_moment(3)))
print("{:<25} {:.2f}".format("Початковий момент 4-го порядку:", analysis.starting_moment(4)))
print("")
print("{:<25} {:.2f}".format("Центральний момент 2-го порядку:", analysis.central_moments(2)))
print("{:<25} {:.2f}".format("Центральний момент 3-го порядку:", analysis.central_moments(3)))
print("{:<25} {:.2f}".format("Центральний момент 4-го порядку:", analysis.central_moments(4)))
print("")
print("{:<25} {:.2f}".format("Асиметрія:", analysis.skewness()))
print("{:<25} {:.2f}".format("Ексцес:", analysis.kurtosis()))
print("")
print("{:<25} {:.2f}".format("Емпірична функція розподілу(4.8):", analysis.empirical_cdf(4.8)))



unique_values = list(set(data))
unique_values.sort()
value_occurances = {}
for element in unique_values:
    value_occurances[element] = data.count(element)
x_values = unique_values


# Полігон за частотами
y_values = []
for element in x_values:
    y_values.append(value_occurances[element])
fig, ax = plt.subplots()
ax.plot(x_values, y_values, "o-")
ax.set(title="Полігон за частотами")
ax.grid()
plt.show()

# Кумулятивна крива за накопиченими частотами
y_values = []
for element in x_values:
    sum = 0 if len(y_values) == 0 else y_values[-1]
    y_values.append(sum + value_occurances[element])
fig, ax = plt.subplots()
ax.plot(x_values, y_values, "o-")
ax.set(title="Кумулятивна крива за накопиченими частотами")
ax.grid()
plt.show()

# Полігон за відносними частотами
y_values = []
for element in x_values:
    y_values.append(value_occurances[element]/len(data))
fig, ax = plt.subplots()
ax.plot(x_values, y_values, "o-")
ax.set(title="Полігон за відносними частотами")
ax.grid()
plt.show()

# Кумулятивна крива за накопиченими відносними частотами
y_values = []
for element in x_values:
    sum = 0 if len(y_values) == 0 else y_values[-1]
    y_values.append(sum + value_occurances[element])
y_values = [i / len(data) for i in y_values]
fig, ax = plt.subplots()
ax.plot(x_values, y_values, "o-")
ax.set(title="Кумулятивна крива за накопиченими відносними частотами")
ax.grid()
plt.show()

# Емпірична функція розподілу
y_values = []
for element in x_values:
    sum = 0 if len(y_values) == 0 else y_values[-1]
    y_values.append(sum + value_occurances[element])
y_values = [y / len(data) for y in y_values]
x_values = [x_values[0]-0.2] + x_values + [x_values[-1]+0.2]
y_values = [0] + y_values
fig, ax = plt.subplots()
for i, element in enumerate(y_values):
    plt.plot([x_values[i], x_values[i+1]], [element, element], "b-")
ax.set(title="Емпірична функція розподілу")
ax.grid()
plt.show()




# відображення графіків
"""
analysis.plot_polygon()
analysis.plot_cumulative_freq()
analysis.plot_relative_polygon()
analysis.plot_relative_cumulative()
analysis.plot_empirical_cdf()
"""