import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

COLORS = ('#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
        '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5')

plt.rcParams['font.size'] = 22
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['CMU Serif']
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rc('axes', unicode_minus=False)


def create_figure(nrows, ncols, figsize=(12, 6)):
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize, squeeze=False)
    if nrows > 1 or ncols > 1:
        for ax in axes.flat:
            ax.set_prop_cycle(color=COLORS)
            ax.minorticks_on()
    return fig, axes


def plot(fig, ax, x_for_plotting, y_for_plotting, x_nodes_to_show=None, y_nodes_to_show=None, show_nodes=False, node_size=6,
         x_label=None, y_label=None, func_label=None, linewidth=2, legend_on_fig=False, x_lim=None, y_lim=None):

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True, linestyle='--', alpha=0.6)

    if x_lim is not None:
        ax.set_xlim(*x_lim)
    if y_lim is not None:
        ax.set_ylim(*y_lim)

    ax.plot(x_for_plotting, y_for_plotting, '-', label=func_label,
              linewidth=linewidth)
    if show_nodes:
        ax.plot(x_nodes_to_show, y_nodes_to_show, 'ro', markersize=node_size)

    if func_label is not None:
        if legend_on_fig:
            fig.legend(labelspacing=0.1, frameon=True)
        else:
            ax.legend(labelspacing=0.1, frameon=True)

def semilogy(fig, ax, x_for_plotting, y_for_plotting, x_label=None, y_label=None, func_label=None,
             linewidth=2, legend_on_fig=False, x_lim=None, y_lim=None):
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True, linestyle='--', alpha=0.6)

    if x_lim is not None:
        ax.set_xlim(*x_lim)
    if y_lim is not None:
        ax.set_ylim(*y_lim)

    ax.semilogy(x_for_plotting, y_for_plotting, '-', linewidth=linewidth, label=func_label)

    if func_label is not None:
        if legend_on_fig:
            fig.legend(labelspacing=0.1, frameon=True)
        else:
            ax.legend(labelspacing=0.1, frameon=True)