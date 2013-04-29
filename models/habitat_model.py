from random import random
from ctypes import *

from core.event import CellAddedEvent, CellRemovedEvent, SetCellEvent, DelCellEvent
from core.model import Model
from core.config import Config

from core.resource_manager import Resource

class Habitat(Model):

    """
    Habitat of the cells.
    Represented by a grid with the size of the window
    """
    def __init__(self):
        Model.__init__(self)
        self.config = Config()
        winSize = self.config.attr.game.window.size

        #Initializing a (i, j) list
        lins = int(winSize[0]/16)
        cols = int(winSize[1]/16)
        self.config.attr.game.habitat.size = (lins, cols)
        self.gridSize = (lins, cols)
        self.keepAlive = []
        self.grid = [ [None] * cols for i in range(lins)]


    def defaultAction(self):
        pass

    def __str__(self):
        result = ""
        for i in range(self.gridSize[0]):
            for j in range(self.gridSize[1]):
                result += str(self.grid[i][j])+" "
            result += "\n"

        return result


    def generateFirstPopulation(self):
        for i in range(self.gridSize[0]):
            for j in range(self.gridSize[1]):
                if self.config.attr.game.population.percentage >= random():
                    self.grid[i][j] = True
                else:
                    self.grid[i][j] = False

        self.turnIntoCArray()


    def turnIntoCArray(self):
        entrylist = []
        for sublist in self.grid:
            entrylist.append((c_ubyte * len(sublist))(*sublist))

        self.grid = (POINTER(c_ubyte) * len(entrylist))(*entrylist)


    def setCell(self, x, y):
        if not self.grid[x][y]:
            self.grid[x][y] = True
            return True
        else:
            return False


    def delCell(self, x, y):
        if self.grid[x][y]:
            self.grid[x][y] = False
            return True
        else:
            return False


    def nextGeneration(self):
        lib = Resource().dll("game_of_life_algorithm")
        lib.nextGeneration(self.grid, self.gridSize[0], self.gridSize[1])
