
import dataclasses
import math
import random
from copy import deepcopy
from typing import List

import src.helpers as helpers
from src.CostFunctions import CostFunction
from src.Scavanger import Scavenger
from src.Visualization import Visualization


class Trainer:
    def __init__(self, costFn: CostFunction, scavangerCount: int, max_it_without_optimization: int = 10) -> None:
        self.iteration = 0
        self.costFn = costFn
        self.scavangerCount = scavangerCount
        self.scavangers = []
        self.iterations_without_optimization = 0
        self.max_it_without_optimization = max_it_without_optimization
        self.visu = Visualization(costFn=costFn, points_count=scavangerCount)

        self.best = None

    def run(self):
        self.iterations_without_optimization = 0

        # Generate initial Scavangers
        self.scavangers = [Scavenger(self.costFn)
                           for _ in range(self.scavangerCount)]
        self.scavangers.sort(reverse=True)
        self.best = self.scavangers[0]

        while self.iterations_without_optimization <= self.max_it_without_optimization:
            self.iterate()

    def iterate(self):
        self.iteration += 1

        scavangers = self.scavangers

        # Duplicate every scavanger
        scavangers = scavangers + \
            [Scavenger(self.costFn, x=scavanger.x, y=scavanger.y)
             for scavanger in scavangers]

        # Generate random scavangers
        scavangers = scavangers + [Scavenger(self.costFn)
                                   for _ in range(math.floor(self.scavangerCount*.1))]

        # Move all scavangers
        for scavanger in scavangers:
            scavanger.move(best=self.best)

        # Select stochastically scavangers to the next generation
        self.scavangers = Trainer.select_scavangers(
            scavangers=scavangers, select_count=self.scavangerCount)
        self.scavangers.sort(reverse=True)

        # Check for best scavanger
        if (self.scavangers[0].evaluation > self.best.evaluation):
            self.best = self.scavangers[0]
            self.iterations_without_optimization = 0
        else:
            self.iterations_without_optimization += 1

        self.show_population_data()

    @staticmethod
    def select_scavangers(scavangers: List[Scavenger], select_count) -> List[Scavenger]:
        """Select a limited number of scavangers from list of scavangers, take 10% of the best and the ramaining are selected 
            stochasticaly through a weighted roullete wheel selection

        Args:
            scavangers (List[Scavenger]): list of scavangers to select from
            select_count (_type_): number of scavangers to select

        Returns:
            List[Scavenger]: list of selected scavangers
        """
        # Take the best 10% scavangers to the next iteration
        selected_scavangers = scavangers[:math.ceil(select_count*0.1)]

        # Use weighted roullette wheel to select the rest of the scavangers
        scavangers_selected_from_roulette = Trainer.make_weighted_roulette_wheel_selection(
            scavangers, select_count - len(selected_scavangers))
        selected_scavangers = selected_scavangers + scavangers_selected_from_roulette

        return selected_scavangers

    @staticmethod
    def make_weighted_roulette_wheel_selection(scavangers: List[Scavenger], winners_count: int) -> List[Scavenger]:
        """Choose winners_count scavangers from list using the roulette algorithmn, fitness proportionate selection

        Args:
            scavangers (List[Scavenger]): _description_
            winners_count (int): _description_

        Returns:
            List[Scavenger]: _description_
        """

        winners = []

        fitness_sum = sum(
            list(map(lambda scavanger: scavanger.evaluation, scavangers)))
        scavangers.sort()
        for _ in range(winners_count):
            random_value = random.random() * fitness_sum
            accumulated_fitness = 0
            for scavanger in scavangers:
                accumulated_fitness += scavanger.evaluation
                if accumulated_fitness >= random_value:
                    winners.append(deepcopy(scavanger))
                    break

        return winners

    def show_population_data(self):
        print(f"\n# Iteration {self.iteration}")
        print(f"# \t Best: {self.scavangers[0]}")

        X = list(map(lambda scavanger: scavanger.x, self.scavangers))
        Y = list(map(lambda scavanger: scavanger.y, self.scavangers))
        Z = list(map(lambda scavanger: scavanger.evaluation, self.scavangers))
        self.visu.plot(X, Y, Z)
