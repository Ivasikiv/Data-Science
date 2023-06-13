import numpy as np
import pandas as pd
from scipy.stats import norm
from matplotlib import pyplot as plt
from StatisticalAnalysis import StatisticalAnalysis

data = [-5.0, -4.9, -4.8, -4.7, -4.6, -4.5, -4.4, -4.3, -4.2, -4.1, -4.0, -3.8, -3.8, -3.6, -3.4, -3.2, -3.0, -2.9, -2.8, -2.7, -2.6, -2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.8, -1.8, -1.6, -1.4, -1.2, -1.0, -0.7, -0.7, -0.3, -0.3, 0.0, 0.3, 0.3, 0.7, 0.7, 1.0, 1.0, 1.2, 1.4, 1.6, 1.8, 1.8, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.2, 3.4, 3.6, 3.8, 3.8, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.9, 4.9, 5.0]
analysis = StatisticalAnalysis(data)

""" створити програмні засоби, які дають
змогу формувати інтервальний статистичний ряд за частотами та
відносними частотами і визначати його основні числові параметри, а саме:
середнє статистичне, моду, медіану, розмах, дисперсію, середнє
квадратичне відхилення, виправлену дисперсію, виправлене середнє
квадратичне відхилення, варіацію, початкові та центральні моменти
певного порядку, асиметрію та ексцес, а також геометрично відображати
гістограму і кумулятивну криву за частотами та відносними частотами і
емпіричну функцію розподілу.
"""
#print("{:^10.2f} {:^10.2f} {:^10.2f}".format(interval[0], freq[i], rel_freq[i]))


#обчислення інтервального статистичного ряду та виведення на екран
freq, rel_freq, intervals = analysis.calculate_frequencies()
print('Інтервали: ', intervals)
print('Частоти: ', freq)
print('Відносні частоти: ', rel_freq)
print("")

def interval_table(data, intervals):
    freq, _ = np.histogram(data, bins=[i[0] for i in intervals] + [intervals[-1][1]])
    rel_freq = freq / len(data)
    mids = [(i[0] + i[1])/2 for i in intervals]
    #z_values = [norm.ppf((i[1] - np.mean(data)) / (np.std(data))) - norm.ppf((i[0] - np.mean(data)) / (np.std(data))) for i in intervals]
    z_values = [13, 11, 10, 7, 7, 11, 10, 5]
    return pd.DataFrame({
        'Intervals': intervals,
        'z_i': z_values,
        'm_i': rel_freq
    })

print(interval_table(data, intervals))
print("")

#виведення основних числових параметрів на екран
print("Середнє: {:^10.2f}".format(analysis.mean()))
print("Медіана: {:^10.2f}".format(analysis.median()))
print('Модальний інтервал: ', analysis.mode())
print("Мода: {:^10.2f}".format(analysis.calculate_mode()))
print("")
print("Діапазон: {:^10.2f}".format(analysis.range()))
print("Дисперсія: {:^10.2f}".format(analysis.variance()))
print("Стандартне відхилення: {:^10.2f}".format(analysis.std_dev()))
print("Скоригована дисперсія: {:^10.2f}".format(analysis.corrected_variance()))
print("Скориговане стандартне відхилення: {:^10.2f}".format(analysis.corrected_std_dev()))
print("")
print("Початковий момент 2-го порядку: {:^10.2f}".format(analysis.starting_moment(2)))
print("Центральний момент 2-го порядку: {:^10.2f}".format(analysis.central_moment(2)))
print("")
print("Варіація: {:^10.2f}".format(analysis.coefficient_of_variation()))
print("Асиметрія: {:^10.2f}".format(analysis.skewness()))
print("Ексцес: {:^10.2f}".format(analysis.kurtosis()))

#виведення графіків
#analysis.plot_histogram()
#analysis.plot_cumulative_curve()
analysis.plot_empirical_distribution()






