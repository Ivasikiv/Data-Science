from statistics import mean

NUMBER_OF_ROWS = 2
NUMBER_OF_COLUMNS = 2

def stat_correl_moment(x_arr, y_arr):
    sum = 0;
    for i in range(0, len(x_arr)):
        sum += (x_arr[i] - mean(x_arr)) * (y_arr[i] - mean(y_arr))
    return sum / len(x_arr)

def mean_square_deviation(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum += (arr[i] - mean(arr)) ** 2
    return (sum / len(arr)) ** 0.5

def laplace_distribution(alpha):
    # alpha = 0.05 0.01 0.001
    match alpha:
        case 0.05:
            return 1.96
        case 0.01:
            return 2.58
        case 0.001:
            return 3.29
        case _:
            return 0

def correl_coef(x_arr, y_arr):
    return stat_correl_moment(x_arr, y_arr) / (mean_square_deviation(x_arr) * mean_square_deviation(y_arr))

def normal_sys_matrix(arr):
    res_matrix = [[0 for i in range(NUMBER_OF_COLUMNS)] for j in range(NUMBER_OF_ROWS)]
    res_matrix[0][0] = len(arr)
    for elem in arr:
        res_matrix[0][1] += elem
        res_matrix[1][1] += elem ** 2
    res_matrix[1][0] = res_matrix[0][1]
    return res_matrix

def normal_sys_extended_matrix(x_arr, y_arr):
    res_matrix = [[0 for i in range(NUMBER_OF_COLUMNS + 1)] for j in range(NUMBER_OF_ROWS)]
    res_matrix[0][0] = len(x_arr)
    for i in range(0, len(x_arr)):
        res_matrix[0][1] += x_arr[i]
        res_matrix[1][1] += x_arr[i] ** 2
        res_matrix[0][2] += y_arr[i]
        res_matrix[1][2] += x_arr[i] * y_arr[i]
    res_matrix[1][0] = res_matrix[0][1]
    return res_matrix

def deternminant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def second_order_determinant(matrix, col1, col2):
    return matrix[0][col1] * matrix[1][col2] - matrix[0][col2] * matrix[1][col1]

# def cramer_method(matrix):
#     return [second_order_determinant(matrix, 1, 2) / deternminant(matrix), second_order_determinant(matrix, 0, 2) / deternminant(matrix)]
#

def cramer_method(extd_matrix):
    deternminant_matrix = deternminant(extd_matrix)

    if deternminant_matrix == 0:
        return [0, 0]
    alpha_deternminant_matrix = second_order_determinant(extd_matrix, 2, 1)
    beta_deternminant_matrix = second_order_determinant(extd_matrix, 0, 2)
    res_arr = [0 for i in range(NUMBER_OF_COLUMNS)]
    res_arr[0] = alpha_deternminant_matrix / deternminant_matrix
    res_arr[1] = beta_deternminant_matrix / deternminant_matrix
    return res_arr

