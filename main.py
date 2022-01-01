from runge_kutta import RungeKutta
from Functions import Functions

if __name__ == '__main__':
    user = "t"
    n = 2
    while user == "t":
        fig = RungeKutta.runge_kutta(0, 1, 10, n, Functions.f1, Functions.f1_solution)
        n *= 2
        user = input("dalej?: \n>")
