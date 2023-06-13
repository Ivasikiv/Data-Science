import math
from statistics import mean
from pynverse import inversefunc
from scipy.special import erf
from scipy.stats import laplace

def stat_corel_moment(x, y):
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - mean(x)) * (y[i] - mean(y))
    return sum / len(x)

def mean_square_deviation(x):
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - mean(x)) ** 2
    return math.sqrt(sum / len(x))

def laplace_distribution_np(alpha):
    print ("Laplace distribution")
    erf(1)
    Phi = lambda x: erf(x / math.sqrt(2)) / 2
    invLap = inversefunc(Phi)
    return invLap((1 - alpha) / 2)

def laplace_distribution(alpha):
    # return value of laplace distribution for alpha = 0.05 or 0.01 or 0.001
    if alpha == 0.05:
        return 1.96
    elif alpha == 0.01:
        return 2.58
    elif alpha == 0.001:
        return 3.29
    else:
        return 0

def corel_coef(x, y):
    return stat_corel_moment(x, y) / (mean_square_deviation(x) * mean_square_deviation(y))

def fisher_function(x, y):
    r_xy = corel_coef(x, y)
    return 0.5 * math.log((1 + r_xy) / (1 - r_xy))