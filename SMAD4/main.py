import numpy as np
from scipy.stats import f

# Вхідні дані
data = np.array([[0.121, 0.140, 0.074, 0.106],
                 [0.173, 0.144, 0.125, 0.084],
                 [0.099, 0.062, 0.052, 0.045],
                 [-0.008, -0.052, 0.036, 0.023],
                 [0.051, 0.084, 0.090, 0.135],
                 [0.000, 0.124, 0.127, 0.185]])
# кількість факторів (рядки) - 6, кількість результатів вимірювання (стовбці) - 4


n_factors, n_measurements = data.shape
group_means = np.mean(data, axis=1)
overall_mean = np.mean(data)

print("")
print("Групові середні значення (𝑥̅𝑖):", group_means)
print("Загальне середнє значення (𝑥̅):", overall_mean)
print("")


Q = np.sum(np.square(data - overall_mean))
Q1 = np.sum(n_measurements * np.square(group_means - overall_mean))
Q2 = np.sum(np.sum(np.square(data - group_means.reshape(-1, 1)), axis=1))


print("Значення Q:", Q)
print("Значення Q1:", Q1)
print("Значення Q2:", Q2)
print("")

# Обчислення незміщених оцінок дисперсій
S = Q / (n_factors * n_measurements - 1)
S1 = Q1 / (n_factors - 1)
S2 = Q2 / (n_factors * (n_measurements - 1))

print("Незміщена оцінка загальної дисперсії (S^2):", S)
print("Незміщена оцінка міжгрупової дисперсії (S1^2):", S1)
print("Незміщена оцінка залишкової дисперсії (S2^2):", S2)
print("")

# Емпіричне та теоретичне значення критерія Фішера-Снедекора
# fisher_snedecor = {0.01: 4.2479, 0.05: 2.7728}
alpha = 0.05  # рівень значущості

F_empirical = S1 / S2
F_theoretical = f.ppf(1 - alpha, n_factors - 1, n_factors * (n_measurements - 1))


print("Емпіричне значення критерія Фішера-Снедекора:", F_empirical)
print("Теоретичне значення критерія Фішера-Снедекора:", F_theoretical)
print("")

# Порівняння емпіричного значення критерія Фішера-Снедекора з теоретичним значенням
if F_empirical > F_theoretical:
    print("Досліджуваний фактор впливає на результат вимірювання.")
else:
    print("Досліджуваний фактор не впливає на результат вимірювання.")
print("")
