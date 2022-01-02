from runge_kutta import RungeKutta
from Functions import Functions
import parser
from math import *
from FunctionBuilder import FunctionBuilder


if __name__ == '__main__':
    formula = "-2 * x + exp(t)"
    fb = FunctionBuilder(formula)
    user = "t"
    n = 2
    while user == "t":
        # runge_kutta(t0, x0, tn, number of steps, function)
        fig = RungeKutta.runge_kutta(0, 1, 2, n, fb.function)
        n *= 2
        user = input("dalej?: \n>")



