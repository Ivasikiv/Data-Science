import numpy as np
import math

# Функція для перевірки правильності введення даних та рівня значущості
def get_input():
    while True:
        try:
            data = input("Введіть дані через кому: ").split(",")
            data = [float(d) for d in data]
            alpha = float(input("Введіть рівень значущості (від 0 до 1): "))
            if alpha < 0 or alpha > 1:
                raise ValueError
            return data, alpha
        except ValueError:
            print("Некоректний ввід даних. Спробуйте ще раз.")

# Функція для побудови дискретного статистичного ряду
def get_frequency_table(data):
    freq_dict = {}
    for x in data:
        if x in freq_dict:
            freq_dict[x] += 1
        else:
            freq_dict[x] = 1
    freq_list = sorted(freq_dict.items())
    return np.array(freq_list)

# Функція для обрахунку середнього статистичного значення
def get_mean(data):
    return np.mean(data)

# Функція для обрахунку дисперсії
def get_variance(data):
    return np.var(data, ddof=1)

# Функція для обрахунку середнього квадратичного відхилення
def get_standard_deviation(data):
    return np.std(data, ddof=1)


def interval_estimate_known_variance(mean, var, sample_size, significance_level):
    """
    Розраховує інтервальну оцінку для математичного сподівання з відомою дисперсією.

    Аргументи:
    mean -- середнє значення;
    var -- дисперсія;
    sample_size -- обсяг вибірки;
    significance_level -- рівень значущості (наприклад, 0.95 для довірчого інтервалу 95%).

    Результат:
    interval -- кортеж з нижньою та верхньою межами довірчого інтервалу.
    """
    laplace = {0.95: 1.95, 0.99: 2.58, 0.999: 3.38}     # таблиця квантилів розподілу Лапласа
    t = laplace.get(significance_level)                 # квантиль розподілу Лапласа
    se = math.sqrt(var) / math.sqrt(sample_size)        # стандартна похибка (S / sqrt(n))
    lower_bound = mean - t * se                         # нижня межа інтервалу
    upper_bound = mean + t * se                         # верхня межа інтервалу
    interval = (lower_bound, upper_bound)
    return interval

from scipy.stats import t

def interval_estimate_unknown_variance(data, confidence_level):
    """
    Розраховує інтервальну оцінку для математичного сподівання з невідомою дисперсією.

    Аргументи:
    data -- список з даними;
    confidence_level -- рівень значущості (наприклад, 0.95 для довірчого інтервалу 95%).

    Результат:
    interval -- кортеж з нижньою та верхньою межами довірчого інтервалу.
    """
    n = len(data)
    mean = np.mean(data)                                    # знаходжу середнє значення

    std_err = np.std(data, ddof=1) / np.sqrt(n)             # знаходжу стандартну похибку (S / sqrt(n)
    t_value = t.ppf(1 - (1 - confidence_level) / 2, n - 1)  # квантиль розподілу Стьюдента
    lower_bound = mean - t_value * std_err                  # нижня межа інтервалу
    upper_bound = mean + t_value * std_err                  # верхня межа інтервалу
    interval = (lower_bound, upper_bound)
    return interval

from scipy.stats import chi2

def std_deviation_interval(X, confidence_level):
    """
    Розраховує інтервальну оцінку для середньоквадратичного відхилення.

    Аргументи:
    X -- список з даними;
    confidence_level -- рівень значущості (наприклад, 0.95 для довірчого інтервалу 95%).

    Результат:
    interval -- кортеж з нижньою та верхньою межами довірчого інтервалу.
    """
    n = len(X)
    S = np.std(X, ddof=1)                                   # знаходжу середнє квадратичне відхилення
    S_0 = S * np.sqrt((n - 1) / n)                          # знаходжу виправлене середньоквадратичне відхилення
    alpha = 1 - confidence_level                            # рівень значущості
    q = chi2.ppf(1 - alpha/2, n - 1) / (n - 1)              # квантиль розподілу хі-квадрат
    lower_bound = 0 if q >= 1 else S_0 * (1 - np.sqrt(q))   # нижня межа інтервалу
    upper_bound = S_0 * (1 + np.sqrt(q))                    # верхня межа інтервалу
    interval = (lower_bound, upper_bound)
    return interval
