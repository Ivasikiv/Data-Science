import numpy as np
from scipy.stats import f

# Вхідні дані
data = np.array([[-0.068, 0.071, 0.117, 0.023],
                 [-0.158, 0.066, 0.087, 0.000],
                 [-0.171, 0.029, 0.128, 0.124],
                 [-0.117, 0.117, 0.142, 0.051],
                 [-0.060, 0.131, 0.145, 0.084],
                 [-0.016, 0.108, 0.163, 0.090],
                 [0.164, 0.145, 0.122, 0.135],
                 [0.275, 0.203, 0.187, 0.127],
                 [0.276, 0.096, 0.183, 0.185]])

n_factor1, n_factor2 = data.shape

xi_mean = np.mean(data, axis=1)
xj_mean = np.mean(data, axis=0)
x_mean = np.mean(data)


print("Групові середні значення (Фактор 1):", xi_mean)
print("Групові середні значення (Фактор 2):", xj_mean)
print("Загальне середнє значення: x̄ = ", x_mean)
print("")


Q = np.sum((data - x_mean)**2)
Q1 = n_factor1 * np.sum((xi_mean - x_mean)**2)
Q2 = n_factor2 * np.sum((xj_mean - x_mean)**2)
Q3 = np.sum((data - xi_mean.reshape(-1, 1) - xj_mean + x_mean)**2)


print("Загальна сума квадратичних відхилень (Q):", Q)
print("Сума квадратичних відхилень для фактора 1 (Q1):", Q1)
print("Сума квадратичних відхилень для фактора 2 (Q2):", Q2)
print("Залишкова сума квадратичних відхилень (Q3):", Q3)
print("")


S = Q / (n_factor1 * n_factor2 - 1)
S1 = Q1 / (n_factor1 - 1)
S2 = Q2 / (n_factor2 - 1)
S3 = Q3 / ((n_factor1 - 1) * (n_factor2 - 1))

print("Незміщена оцінка загальної дисперсії (S^2):", S)
print("Незміщена оцінка дисперсії за фактором 1 (S1^2):", S1)
print("Незміщена оцінка дисперсії за фактором 2 (S2^2):", S2)
print("Незміщена оцінка залишкової дисперсії (S3^2):", S3)
print("")

F1 = S1 / S3
F2 = S2 / S3

alpha = 0.05

F1_theoretical = f.ppf(1 - alpha, n_factor1 - 1, (n_factor1 - 1) * (n_factor2 - 1))
F2_theoretical = f.ppf(1 - alpha, n_factor2 - 1, (n_factor1 - 1) * (n_factor2 - 1))


print("Емпіричне значення критерію Фішера-Снедекора за фактором 1:", F1)
print("Теоретичне значення критерію Фішера-Снедекора за фактором 1:", F1_theoretical)
print("")
print("Емпіричне значення критерію Фішера-Снедекора за фактором 2:", F2)
print("Теоретичне значення критерію Фішера-Снедекора за фактором 2:", F2_theoretical)
print("")

if F1 < F1_theoretical and F2 < F2_theoretical:
    print("Обидва фактори суттєво не впливають на результати досліджень.")
elif F1 > F1_theoretical and F2 > F2_theoretical:
    print("Обидва фактори суттєво впливають на результати досліджень.")
elif F1 < F1_theoretical and F2 > F2_theoretical:
    print("Перший фактор не впливає, а другий фактор суттєво впливає на результати досліджень.")
else: #F1 > F1_theoretical and F2 < F2_theoretical:
    print("Перший фактор суттєво впливає, а другий фактор не впливає на результати досліджень.")
