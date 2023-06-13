import numpy as np
from functions import *

x_arr = np.array([0.24, 0.32, 0.29, 0.31, 0.27, 0.32, 0.29,
                  0.37, 0.37, 0.30, 0.38, 0.33, 0.22, 0.28, 0.26,
                  0.38, 0.34, 0.37, 0.56, 0.63, 1.03, 0.96, 0.54, 0.24, 0.19, 0.12, 0.00,
                  0.24, 0.32, 0.35, 0.43, 0.62, 0.81, 0.99, 0.59, 0.43, 0.23,
                  0.12, 0.24, 0.36, 0.52, 0.56, 0.68, 0.62, 0.52, 0.27, 0.20, 0.10,
                  0.02, 0.22, 0.29, 0.31, 0.36, 0.63, 0.76, 0.56, 0.32, 0.13])


y_arr = np.array([0.35, 0.35, 0.30, 0.36, 0.31, 0.36, 0.34,
                  0.38, 0.37, 0.38, 0.36, 0.40, 0.36, 0.48, 0.32,
                  0.35, 0.38, 0.42, 0.47, 0.60, 0.91, 0.89, 0.59, 0.38, 0.27, 0.19, 0.02,
                  0.24, 0.32, 0.34, 0.41, 0.57, 0.81, 0.97, 0.59, 0.36, 0.21,
                  0.14, 0.28, 0.31, 0.57, 0.65, 0.78, 0.70, 0.52, 0.19, 0.11, 0.00,
                  0.03, 0.24, 0.33, 0.33, 0.38, 0.63, 0.79, 0.55, 0.34, 0.14])

n = len(x_arr)

print("Дослідження тісноти зв’язку між двома сумісно виміряними величинами\nдля малого обсягу статистичної вибірки")
print("")

alpha = 0.001

K_xy_stat = stat_corel_moment(x_arr, y_arr)
S_x = mean_square_deviation(x_arr)
S_y = mean_square_deviation(y_arr)
r_xy_stat = corel_coef(x_arr, y_arr)

t_Laplace = laplace_distribution(alpha)
z = fisher_function(x_arr, y_arr)
z_interval = [z - t_Laplace / math.sqrt(n - 3), z + t_Laplace / math.sqrt(n - 3)]

r_x1 = (math.exp(2 * (z - (t_Laplace / math.sqrt(n - 3)))) - 1) / (math.exp(2 * (z - (t_Laplace / math.sqrt(n - 3)))) + 1)
r_x2 = (math.exp(2 * (z + (t_Laplace / math.sqrt(n - 3)))) - 1) / (math.exp(2 * (z + (t_Laplace / math.sqrt(n - 3)))) + 1)

print("Статистичний кореляційний момент: ", K_xy_stat)
print("Середньоквадратичне відхилення за значеннями величин x: ", S_x)
print("Середньоквадратичне відхилення за значеннями величин y: ", S_y)
print("Статистичний коефіцієнт кореляції: ", r_xy_stat)
print("")

print("Значення аргументу функції Лапласа t: ", t_Laplace)
print("Емпіричне значення фунуції Фішера: ", z)
print("")

print(f"Інтервальна оцінка значення для теоретичної функції Фішера:  {z_interval[0]} ≤ z ≤ {z_interval[1]}")
print(f"Інтервальна оцінка значення для теоретичного кокфіцієнта кореляції:  {r_x1} ≤ r ≤ {r_x2}")
print("")

l = r_x2 - r_x1

print("Довжина інтервалу: ", l)
print("")

if l > math.fabs(r_xy_stat):
    print("l > |r_xy*| - кореляційного зв'язку між сумісно виміряними величинами не існує")
else:
    print("l < |r_xy*| - кореляційний зв'язок між сумісно виміряними величинами існує")



print("")
print("Дослідження тісноти зв’язку між двома сумісно виміряними величинами\nдля великого обсягу статистичної вибірки")
print("")

n = len(x_arr)
y_arr_test = np.array([1,2,3])

K_xy_stat = stat_corel_moment(x_arr, y_arr)
S_x = mean_square_deviation(x_arr)
S_y = mean_square_deviation(y_arr)
r_xy_stat = corel_coef(x_arr, y_arr)

romenov_coef = 3 * ((1 - r_xy_stat ** 2) / (n ** 0.5))

print("Статистичний кореляційний момент: ", K_xy_stat)
print("Середньоквадратичне відхилення за значеннями величин x: ", S_x)
print("Середньоквадратичне відхилення за значеннями величин y: ", S_y)
print("Статистичний коефіцієнт кореляції: ", r_xy_stat)
print("Значення правої частини нерівності Романовського: ", romenov_coef)
print("")

if math.fabs(r_xy_stat) >= romenov_coef:
    print(f"{r_xy_stat:0,.5f} ≥ {romenov_coef:0,.5f} - кореляційний зв'язок між сумісно виміряними величинами існує")
else:
    print(f"{r_xy_stat:0,.5f} ≤ {romenov_coef:0,.5f} - кореляційного зв'язку між сумісно виміряними величинами не існує")

