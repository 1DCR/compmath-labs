import math
import numpy as np

from lagrange import L


def f(x):
    return math.e**(-x**2)

def calculate_max_distance(y1, y2):
    distances = abs(y1-y2)
    return max(distances)

def approximate_distances():
    X = np.linspace(-5, 5, 200)
    f_X = np.array([f(x) for x in X])

    print('Приблизительное расстояния между f(x) и L_n-1(x):')

    for n in range(4, 21):
        x_nodes = np.linspace(-5, 5, n)
        y_nodes = np.array([f(x) for x in x_nodes])

        L_X = [L(x, x_nodes, y_nodes) for x in X]

        print(f'При n = {n:<2} равняется: {round(calculate_max_distance(f_X, L_X), 3):>.3f}')