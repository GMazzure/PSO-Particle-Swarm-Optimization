import math
import os
from time import sleep

import pylab as p
from numpy import *
from src.CostFunctions import CostFunction
from src.helpers import scale


class Visualization:
    def __init__(self, costFn: CostFunction, points_count: int = 0) -> None:
        self.costFn = costFn
        self.fig = p.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.generateFnMeshCoordinates()
        self.colors = Visualization.generate_colors(points_count)

    def generateFnMeshCoordinates(self):
        x = r_[self.costFn.min_value:self.costFn.max_value:250j]
        y = r_[self.costFn.min_value:self.costFn.max_value:250j]

        self.X, self.Y = meshgrid(x, y)
        self.Z = self.costFn.plot(self.X, self.Y)

    def export(self):
        p.savefig(self.fileName+".png")

    def drawChart(self):
        p.draw()
        p.pause(0.01)

    def plotFn(self):
        self.ax.plot_surface(self.X, self.Y, self.Z, rstride=10, cstride=10,
                             color=[0.5, 0.5, 0.5], alpha=0.5)

        # Label dos axis
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')

    def plot(self, X, Y, Z):
        self.ax.cla()
        self.plotFn()
        self.ax.scatter(X, Y, Z, zdir='z', s=30,
                        c=self.colors ,depthshade=False)
        self.drawChart()
        sleep(0.1)

    def findEmptyDirToLog(self):
        testNumber = 1
        exists = os.path.exists("./Log/teste"+str(testNumber))
        while (exists):
            testNumber += 1
            exists = os.path.exists("./Log/teste"+str(testNumber))
        logPath = "Log/teste"+str(testNumber)+"/"
        os.makedirs(logPath)
        self.logPath = logPath

    @staticmethod
    def generate_colors(colors_count):
        c = []
        for i in range(colors_count):
            r = scale(i, 0, colors_count, 0, 1)
            g = 0
            b = 0
            c.append([r, g, b])
        
        print(c)
        return c
