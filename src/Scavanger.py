
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List

from src.CostFunctions import CostFunction, OptimizationType


class Scavenger():

    def __init__(self, costfFn: CostFunction, x:float=None, y:float=None):

        self.costFn = costfFn
        self.x = x
        self.y = y
        
        if not x:
            self.x = self.costFn.generate_random_coord()
        if not y:
            self.y = self.costFn.generate_random_coord()
        self.evaluation = Scavenger.evaluate(self.costFn, self.x, self.y)

        self.lifetime = 0
        self.isRoaming = True
        self.hotness = 1
        self.velocity = (random.random()*0.5) - 0.025
        self.min_velocity_loss = random.uniform(0.95, 1)

    def __eq__(self, other: Scavenger):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other: Scavenger):
        if self.costFn.optimization_type == OptimizationType.MAXIMIZATION:
            return self.evaluation > other.evaluation
        return self.evaluation < other.evaluation

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}] +{self.lifetime} {'Roaming' if self.isRoaming else 'Hoping'} hot:{self.hotness}"

    @staticmethod
    def evaluate(costFn: CostFunction, x: float, y: float):
        return costFn.plot(x, y)

    def move(self, best:Scavenger):
        self.lifetime += 1
        if self.isRoaming:
            new_x, new_y = self.try_to_roam()
        else:
            new_x, new_y = self.try_to_hop(best)

        self.velocity = self.velocity*random.uniform(self.min_velocity_loss, 1)

        new_evaluation = Scavenger.evaluate(self.costFn, new_x, new_y)
        if new_evaluation > self.evaluation:
            self.x = new_x
            self.y = new_y
            self.evaluation = new_evaluation
            self.hotness += 0.3
        else:
            self.hotness -= 0.1

        if self.hotness <= 0:
            self.isRoaming = not self.isRoaming
            self.hotness = 1

    def try_to_roam(self) -> List[float]:
        roam_x = random.randint(-2, 2)/2
        roam_y = random.randint(-2, 2)/2

        x = self.x + roam_x*self.velocity
        if x > self.costFn.max_value:
            x = random.uniform(self.x, self.costFn.max_value)
        elif x < self.costFn.min_value:
            x = random.uniform(self.costFn.min_value, self.x)

        y = self.y + roam_y*self.velocity
        if y > self.costFn.max_value:
            y = random.uniform(self.y, self.costFn.max_value)
        elif y < self.costFn.min_value:
            y = random.uniform(self.costFn.min_value, self.y)

        return x, y

    def try_to_hop(self, best: Scavenger) -> List[float]:
        
        x = random.uniform(a=self.x, b=best.x) if self.x < best.x else random.uniform(a=best.x, b=self.x) 
        y = random.uniform(a=self.y, b=best.y) if self.y < best.y else random.uniform(a=best.y, b=self.y) 
        return x, y
