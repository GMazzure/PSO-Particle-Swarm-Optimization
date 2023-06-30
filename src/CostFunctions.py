import random
from enum import Enum

from numpy import *


class OptimizationType(Enum):
    MAXIMIZATION = 1
    MINIMIZATION = 2


class CostFunction:
    min_value = 0
    max_value = 100
    optimization_type = OptimizationType.MAXIMIZATION

    def generate_random_coord(self) -> float:
        return random.uniform(self.min_value, self.max_value)

    @staticmethod
    def plot(x: float, y: float) -> float:
        raise NotImplementedError("Plot not implemented")


class Schwefel(CostFunction):
    @staticmethod
    def plot(x: float, y: float) -> float:
        return 418.9829*2 - (x*(sin(sqrt(absolute(x)))) + y*(sin(sqrt(absolute(y)))))


class Rastrigin(CostFunction):
    @staticmethod
    def plot(x: float, y: float) -> float:
        a = 20 + (x**2) + (y**2)
        b = 10*(cos(2*pi*x) + cos(2*pi*y))
        return a-b


class Third(CostFunction):
    @staticmethod
    def plot(x, y):
        return exp(-((x**2) + (y**2)))
