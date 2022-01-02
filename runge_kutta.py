import matplotlib.pyplot as plt
import numpy as np


class RungeKutta:

    @staticmethod
    def _get_epsilon(solution_range, solution, exact_function):
        epsilon = -1
        for n, t in enumerate(solution_range):
            epsilon = max(epsilon, abs(solution[n] - exact_function(t)))

        return epsilon

    @staticmethod
    def runge_kutta_custom(t0, x0, tn, n, f):
        delta = (tn - t0) / (n - 1)
        t = [t0]
        x_solution = [x0]

        for i in range(n - 1):
            u = t0 + delta/2
            k1 = delta * f(t0, x0)
            k2 = delta * f(u, x0 + k1 / 2)
            k3 = delta * f(u, x0 + k2 / 2)
            k4 = delta * f(t0 + delta, x0 + k3)
            next_x = x0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            x_solution.append(next_x)
            t0 += delta
            t.append(t0)
            x0 = next_x

        return {'t': t, 'x(t)': x_solution}

    @staticmethod
    def runge_kutta(t0, x0, tn, n, f, solution):
        delta = (tn - t0) / (n - 1)
        t = [t0]
        x_solution = [x0]
        start_t0 = t0

        for i in range(n - 1):
            u = t0 + delta/2
            k1 = delta * f(t0, x0)
            k2 = delta * f(u, x0 + k1 / 2)
            k3 = delta * f(u, x0 + k2 / 2)
            k4 = delta * f(t0 + delta, x0 + k3)
            next_x = x0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            x_solution.append(next_x)
            t0 += delta
            t.append(t0)
            x0 = next_x

        exact_range = np.arange(start_t0, t[-1] + 0.001, 0.001)
        exact_solution = [solution(i) for i in exact_range]

        return {'t': t,'x(t)':x_solution}, {'exact_t': exact_range, 'exact_x': exact_solution},\
               RungeKutta._get_epsilon(t, x_solution, solution)








