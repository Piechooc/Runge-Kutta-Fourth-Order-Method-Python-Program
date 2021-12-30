import matplotlib.pyplot as plt
import numpy as np
import math


def y(t, x):
    return -2*x + math.exp(t)


def sol(t):
    return (1/3) * np.exp(-2*t) * (np.exp(3*t) + 2)


def get_epsilon(solution_range, solution, exact_function):
    epsilon = -1
    for n, t in enumerate(solution_range):
        epsilon = max(epsilon, abs(solution[n] - exact_function(t)))

    return epsilon


def runge_kutta(t0, x0, tn, n, f):

    delta = (tn - t0) / n
    t = np.arange(t0, tn, delta)
    x_solution = [x0]
    for i in range(n - 1):
        u = t0 + delta/2
        k1 = delta * f(t0, x0)
        k2 = delta * f(u, x0 + k1/2)
        k3 = delta * f(u, x0 + k2/2)
        k4 = delta * f(t0 + delta, x0 + k3)
        next_x = x0 + (k1 + 2*k2 + 2*k3 + k4)/6
        x_solution.append(next_x)
        t0 += delta
        x0 = next_x

    plt.plot(t, x_solution, '-o')
    exact_range = np.arange(0, t[-1], 0.001)
    exact_solution = [sol(t) for t in exact_range]
    plt.plot(exact_range, exact_solution)
    plt.show()
    print("epsilon: ", get_epsilon(t, x_solution, sol))
    print("steps: ", n)


# runge_kutta(0, 1, 6, 30, y)

user = "t"
n = 2
while user == "t":

    runge_kutta(0, 1, 2, n, y)
    n *= 2
    user = input("dalej?: ")



