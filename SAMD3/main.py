from Functions import *


data = [-5.0, -4.9, -4.8, -4.7, -4.6, -4.5, -4.4, -4.3, -4.2, -4.1, -4.0, -3.8, -3.8, -3.6, -3.4, -3.2, -3.0, -2.9, -2.8, -2.7, -2.6, -2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.8, -1.8, -1.6, -1.4, -1.2, -1.0, -0.7, -0.7, -0.3, -0.3, 0.0, 0.3, 0.3, 0.7, 0.7, 1.0, 1.0, 1.2, 1.4, 1.6, 1.8, 1.8, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.2, 3.4, 3.6, 3.8, 3.8, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.9, 4.9, 5.0]

#data, alpha = get_input()

print("Виберіть рівень значущості:")
print("1. 95%")
print("2. 99%")
print("3. 99.9%")

choice = input("Ваш вибір: ")

if choice == "1":
    alpha = 0.95
elif choice == "2":
    alpha = 0.99
elif choice == "3":
    alpha = 0.999
else:
    print("Некоректний ввід даних. Спробуйте ще раз.")
    exit()


mean = get_mean(data)
var = get_variance(data)
stdd = get_standard_deviation(data)
sample_size = len(data)

# LAPLACE_DICT = {gamma: t(gamma)}
LAPLACE_DICT = {0.95: 1.95, 0.99: 2.58, 0.999: 3.38}
# STUDENT_DICT = {gamma: tau(gamma, n = 90)}
STUDENT_DICT = {0.95: 1.987, 0.99: 2.633, 0.999: 3.403}
# PEARSON_DICT = {gamma: q(gamma, n = 90)}
PEARSON_DICT = {0.95: 0.151, 0.99: 0.211, 0.999: 0.290}

print()
print("Значення аргументів функції Лапласа (T_y)", LAPLACE_DICT)
print("Значення аргументів функції Studenta (T_y)", STUDENT_DICT)
print("Значення аргументів функції Пірсона (Q_y)", PEARSON_DICT)
print()

print("Середнє значення: ", mean)
print("Дисперсія: ", var)
print("Середнє квадратичне відхилення: ", stdd)
print("Обсяг вибірки: ", sample_size)
print("")

interval1 = interval_estimate_known_variance(mean, var, sample_size, alpha)
interval2 = interval_estimate_unknown_variance(data, alpha)
interval3 = std_deviation_interval(data, alpha)

print("Інтервальна оцінка середнього значення з відомою дисперсією: ", interval1)
print("Інтервальна оцінка середнього значення з невідомою дисперсією: ", interval2)
print("Інтервальна оцінка середнього квадратичного відхилення: ", interval3)




