import math
import numpy as np


class Functions:

    """
    x(0) = 1
    0 <= t <= 1
    """
    @staticmethod
    def f1(t, x):
        return -2 * x + math.exp(t)

    @staticmethod
    def f1_solution(t):
        return (1 / 3) * np.exp(-2 * t) * (np.exp(3 * t) + 2)

    """
    x(1) = 0
    1 <= t <= 2
    """
    @staticmethod
    def f2(t, x):
        return -(x/t) + 1 + 1/t

    @staticmethod
    def f2_solution(t, x):
        return (t - 3/t + 2)/2

    """
    x(1) = -1
    1 <= t <= 2
    """
    @staticmethod
    def f3(t, x):
        return (x*x + t*t) / (t*x)

    @staticmethod
    def f3_solution(t, x):
        return -t * math.sqrt(2 * math.log(t) + 1)

