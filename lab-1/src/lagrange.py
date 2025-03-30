import numpy as np

def l(i, x, x_nodes):
    x_nodes_exc_i = np.r_[x_nodes[:i], x_nodes[i+1:]]
    l_multipliers = (x - x_nodes_exc_i) / (x_nodes[i] - x_nodes_exc_i)
    return np.prod(l_multipliers)

def L(x, x_nodes, y_nodes):
    L_summands = y_nodes * np.array([l(i, x, x_nodes) for i in range(len(x_nodes))])
    return np.sum(L_summands)