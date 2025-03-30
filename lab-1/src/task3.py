import numpy as np
import matplotlib.pyplot as plt

from lagrange import L
import my_plotting


x_nodes = np.array([2007, 2008, 2009, 2011, 2012, 2013, 2014, 2015])
y_nodes = np.array([6.21, 4.71, 4.9, 4.62, 2.65, 2.95, 2.78, 0.83])
x_for_plotting = np.linspace(2007, 2015, 200)
y_for_plotting = [L(x, x_nodes, y_nodes) for x in x_for_plotting]

fig, axes = my_plotting.create_figure(1, 1)

my_plotting.plot(
     fig,
     axes[0][0],
     x_for_plotting,
     y_for_plotting,
     x_nodes_to_show=x_nodes,
     y_nodes_to_show=y_nodes,
     show_nodes=True,
     node_size=6,
     linewidth=2,
     x_label='Год',
     y_label='Процент детей, не посещающих школу, %',
     func_label='$bad\_kid\_percentage(year)$')

plt.show()