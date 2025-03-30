import math
import numpy as np
import matplotlib.pyplot as plt

import my_plotting


# x_nodes = np.array([2007, 2008, 2009, 2011, 2012, 2013, 2014, 2015])
# y_nodes = np.array([6.21, 4.71, 4.9, 4.62, 2.65, 2.95, 2.78, 0.83])
# x_for_plotting = np.linspace(2007, 2015, 200)

# my_plotting.plot(x_nodes,
#      y_nodes,
#      x_for_plotting,
#      linewidth=2,
#      x_label='Год',
#      y_label='Процент детей, не посещающих школу, %',
#      func_label='$bad\_kid\_percentage(year)$')
# plt.show()


def f(t):
    return math.e**(-t**2)

x_for_plotting = np.linspace(-5, 5, 200)

for n in range(4, 21):
    x_nodes = np.linspace(-5, 5, n)
    y_nodes = np.array([f(x) for x in x_nodes])
    my_plotting.plot(x_nodes, y_nodes, x_for_plotting, linewidth=1, func_label=f'n = {n}')

plt.show()



















# plt.rcParams['font.size'] = 18
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['font.serif'] = ['CMU Serif']
# plt.rcParams['mathtext.fontset'] = 'cm'
#
#
# def l(i, x, x_nodes):
#     x_nodes_exc_i = np.r_[x_nodes[:i], x_nodes[i+1:]]
#     l_multipliers = (x - x_nodes_exc_i) / (x_nodes[i] - x_nodes_exc_i)
#     return np.prod(l_multipliers)
#
# def L(x, x_nodes, y_nodes):
#     L_summands = y_nodes * np.array([l(i, x, x_nodes) for i in range(len(x_nodes))])
#     return np.sum(L_summands)
#
#
# x_nodes = np.array([2007, 2008, 2009, 2011, 2012, 2013, 2014, 2015])
# y_nodes = np.array([6.21, 4.71, 4.9, 4.62, 2.65, 2.95, 2.78, 0.83])
#
# fig, ax = plt.subplots(1, 1, figsize=(12, 6))
# x_for_plotting = np.linspace(2007, 2015, 100)
# ax.plot(x_for_plotting, [L(x, x_nodes, y_nodes) for x in x_for_plotting], 'b-', label='$bad\_kid\_percentage(year)$', linewidth=4)
# ax.plot(x_nodes, y_nodes, 'ro', markersize=10)
# ax.set_xlabel('Год')
# ax.set_ylabel('Процент детей, не посещающих школу, %')
# ax.grid()
# plt.legend()
# plt.show()