import math
import numpy as np
import matplotlib.pyplot as plt

import my_plotting


def f_xi_nth_derivative(xi, n):
    p_n = 0
    for j in range(0, n//2):
        p_n += ((-1)**j * (math.factorial(n)) / (math.factorial(j) * math.factorial(n - 2*j))
                * (2*xi)**(n - 2*j))

    return (-1)**(n+1) * p_n * math.e**(-xi**2)


def calculate_lagrange_remainder(x, x_for_calculating, n):
    max_f_xi = -1
    for xi in x-x_for_calculating:
        if abs(f_xi_nth_derivative(xi, n)) > abs(max_f_xi):
            max_f_xi = f_xi_nth_derivative(xi, n)

    x_nodes = np.linspace(-5, 5, n)
    prod = np.prod([x - x_i for x_i in x_nodes])

    return max_f_xi * prod / math.factorial(n)


approximate_distances_values = [0.929, 0.560, 0.568, 0.891, 0.284, 1.485, 0.512, 2.329, 0.892,
                                3.373, 1.403, 4.524, 2.003, 5.575, 2.617, 6.393, 3.106]


analytical_distances_values = []
x_for_calculating = np.linspace(-5, 5, 200)
print("Аналитическая верхняя граница погрешности:")
for n in range(4, 21):
    max_err = 0
    for x in x_for_calculating:
        max_err = max(max_err, abs(calculate_lagrange_remainder(x, x_for_calculating, n)))
    analytical_distances_values.append(max_err)
    print(f'n = {n:>2}   {round(max_err, 3):>10.3f}')


fig, axes = my_plotting.create_figure(1, 1, figsize=(12, 6))

my_plotting.semilogy(fig, axes[0][0], [n for n in range(4, 21)], approximate_distances_values,
                     x_label='$n$', y_label='Погрешность', func_label='Расстояние между $f(x)$ и $L_{n-1}(x)$')
my_plotting.semilogy(fig, axes[0][0], [n for n in range(4, 21)], analytical_distances_values,
                     x_label='$n$', y_label='Погрешность', func_label='Аналитич. оценка \nверхней границы погрешности')

plt.show()