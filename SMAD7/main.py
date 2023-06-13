from functions import *
import matplotlib.pyplot as plt
import numpy as np

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



extended_matrix_y = normal_sys_extended_matrix(x_arr, y_arr)

mnk_deternminant_y = deternminant(extended_matrix_y)
mnk_alpha_deternminant_y = second_order_determinant(extended_matrix_y, 2, 1)
mnk_beta_deternminant_y = second_order_determinant(extended_matrix_y, 0, 2)

print("")
print("Метод найменших квадратів")
print("")

print(f"△ = {mnk_deternminant_y:0,.5f}")
print(f"△α = {mnk_alpha_deternminant_y:0,.5f}")
print(f"△β = {mnk_beta_deternminant_y:0,.5f}")

print("")

try:
    mnk_alpha_y, mnk_beta_y = cramer_method(extended_matrix_y)

    print(f"α = {mnk_alpha_y:0,.5f}")
    print(f"β = {mnk_beta_y:0,.5f}")
    print(f"y꙳ = {mnk_alpha_y:0,.3f} + {mnk_beta_y:0,.3f}x꙳")
except ZeroDivisionError:
    print("Ділення на нуль")
    exit()


print("")
print("---------------------------------------------")
print("")

extended_matrix_x = normal_sys_extended_matrix(y_arr, x_arr)
mnk_deternminant_x = deternminant(extended_matrix_x)
mnk_alpha_deternminant_x = second_order_determinant(extended_matrix_x, 2, 1)
mnk_beta_deternminant_x = second_order_determinant(extended_matrix_x, 0, 2)

print(f"△' = {mnk_deternminant_x:0,.5f}")
print(f"△α' = {mnk_alpha_deternminant_x:0,.5f}")
print(f"△β' = {mnk_beta_deternminant_x:0,.5f}")

print("")

try:
    mnk_alpha_x, mnk_beta_x = cramer_method(extended_matrix_x)

    print(f"α' = {mnk_alpha_x:0,.5f}")
    print(f"β' = {mnk_beta_x:0,.5f}")
    print(f"x꙳ = {mnk_alpha_x:0,.3f} + {mnk_beta_x:0,.3f}y꙳")
except ZeroDivisionError:
    print("Ділення на нуль")
    exit()

print("")
print("")
print("")

# графік
mnk_figure = plt.figure(figsize=(10, 4))
mnk_axes = mnk_figure.add_axes([0, 0, 1, 1])
mnk_axes.grid(True, alpha=0.25)
ttl = plt.title("Метод найменших квадратів", y = 1.05)
mnk_axes.title.set_size(24)

plt.scatter(x_arr, y_arr, marker='.', s=50, color='blue', label="Вхідні дані")

plot_x = np.linspace(0, 1, 2)
plot_y = mnk_alpha_y + mnk_beta_y * plot_x
mnk_axes.plot(plot_x, plot_y, color="orange", label=f"y = {mnk_alpha_y:0,.3f} + {mnk_beta_y:0,.3f}x")

plot_y = np.linspace(0, 1, 2)
plot_x = mnk_alpha_x + mnk_beta_x * plot_y
mnk_axes.plot(plot_x, plot_y, color="green", label=f"x = {mnk_alpha_x:0,.3f} + {mnk_beta_x:0,.3f}y")

mnk_axes.legend(loc=2, frameon=False)
mnk_axes.set_xlim([0, 1])
mnk_axes.set_ylim([-0.05, 1])
mnk_axes.set_xticks([0, 0.25, 0.5, 0.75, 1])
mnk_axes.set_yticks([0, 0.25, 0.5, 0.75, 1])
mnk_axes.spines['top'].set_color('none')
mnk_axes.spines['right'].set_color('none')
mnk_axes.spines['bottom'].set_color('none')
mnk_axes.xaxis.set_tick_params(length=0)

plot_x = np.linspace(0, 2, 2)
plot_y = 0 * plot_x
mnk_axes.plot(plot_x, plot_y, color="black", linewidth=1)

#show
plt.show()





n = len(x_arr)
x_mean = mean(x_arr)
y_mean = mean(y_arr)

r_xy = correl_coef(x_arr, y_arr)
S_0x = mean_square_deviation(x_arr)
S_0y = mean_square_deviation(y_arr)
r_x = r_xy * (S_0x / S_0y)
r_y = r_xy * (S_0y / S_0x)

print("")
print("Використання статичного коефіцієнта кореляції")
print("")

print(f"r꙳xy = {r_xy:0,.5f}")

print("")
print(f"\u0078\u0304 = {x_mean:0,.5f}")
print(f"Sox = {S_0x:0,.5f}")
print(f"r꙳x|y = {r_x:0,.5f}")
print(f"x꙳ = {x_mean:0,.5f} + {r_x:0,.5f}(y꙳ - {y_mean:0,.5f})")
print("")
print(f"\u0079\u0304 = {y_mean:0,.5f}")
print(f"Soy = {S_0y:0,.5f}")
print(f"r꙳y|x = {r_y:0,.5f}")
print(f"y꙳ = {y_mean:0,.5f} + {r_y:0,.5f}(x꙳ - {x_mean:0,.5f})")

print("")

# графік
mnk_figure = plt.figure(figsize=(10, 4))
mnk_axes = mnk_figure.add_axes([0, 0, 1, 1])
mnk_axes.grid(True, alpha=0.25)
ttl = plt.title("Із використанням статичного коефіцієнта кореляції", y = 1.05)
mnk_axes.title.set_size(24)

plt.scatter(x_arr, y_arr, marker='.', s=50, color='blue', label="Вхідні дані")

plot_x = np.linspace(0, 2, 2)
plot_y = y_mean + r_y * (plot_x - x_mean)
mnk_axes.plot(plot_x, plot_y, color="orange", label=f"y = {y_mean:0,.3f} + {r_y:0,.3f}(x - {x_mean:0,.3f})")

plot_y = np.linspace(0, 1, 2)
plot_x = x_mean + r_x * (plot_y - y_mean)
mnk_axes.plot(plot_x, plot_y, color="green", label=f"x = {x_mean:0,.3f} + {r_x:0,.3f}(y - {y_mean:0,.3f})")

mnk_axes.legend(loc=2, frameon=False)
mnk_axes.set_xlim([0, 1])
mnk_axes.set_ylim([-0.05, 1])
mnk_axes.set_xticks([0, 0.25, 0.5, 0.75, 1])
mnk_axes.set_yticks([0, 0.25, 0.5, 0.75, 1])
mnk_axes.spines['top'].set_color('none')
mnk_axes.spines['right'].set_color('none')
mnk_axes.spines['bottom'].set_color('none')
mnk_axes.xaxis.set_tick_params(length=0)

plot_x = np.linspace(0, 2, 2)
plot_y = 0 * plot_x
mnk_axes.plot(plot_x, plot_y, color="black", linewidth=1)

#show
plt.show()




