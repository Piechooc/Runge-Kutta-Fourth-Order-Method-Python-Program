import parser
from math import *


class FunctionBuilder:
    def __init__(self, formula: str):
        self.code = parser.expr(formula).compile()

    def function(self, t, x):
        return eval(self.code)
