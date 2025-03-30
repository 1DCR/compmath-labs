import math
import numpy as np
import matplotlib.pyplot as plt

from lagrange import L
import my_plotting


def f(x):
    return math.e**(-x**2)

x_for_plotting = np.linspace(-5, 5, 1000)

fig, axes = my_plotting.create_figure(2, 1)

my_plotting.plot(
    fig,
    axes[0][0],
    x_for_plotting,
    [f(x) for x in x_for_plotting],
    x_label='$x$', y_label='$f(x)$',
    linewidth=4, func_label='$e^{x^{-2}}$',
    x_lim=(-6, 7),
    y_lim=(-4, 4))

for n in range(4, 21, 2):
    x_nodes = np.linspace(-5, 5, n)
    y_nodes = [f(x) for x in x_nodes]

    my_plotting.plot(
        fig, axes[1][0],
        x_for_plotting,
        [L(x, x_nodes, y_nodes) for x in x_for_plotting],
        x_label='$x$',
        y_label='$L_{n-1}(x)$',
        linewidth=1,
        func_label=f'n = {n}',
        x_lim=(-6, 7),
        y_lim=(-4, 4))

plt.show()
