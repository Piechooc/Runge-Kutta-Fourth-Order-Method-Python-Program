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
    def _get_plot(t, x_solution, solution, n):
        exact_range = np.arange(0, t[-1], 0.001)
        plt.subplot(111)
        plt.plot(exact_range, solution(exact_range), t, x_solution, "-o")
        plt.show()
        print("epsilon: ", RungeKutta._get_epsilon(t, x_solution, solution))
        print("steps: ", n)
        return plt.figure

    @staticmethod
    def runge_kutta(t0, x0, tn, n, f, solution):

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

        return RungeKutta._get_plot(t, x_solution, solution, n)







