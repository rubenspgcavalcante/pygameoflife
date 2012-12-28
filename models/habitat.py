from random import random

import pygame
from pygame.locals import *

from models.cell import Cell

from resources.manager import Resource
from config import Config

class Habitat(object):

    """
    Habitat of the cells.
    Represented by a grid with the size of the window
    """
    def __init__(self, screen):
        winSize = Config.get("game", "window-size")

        #Initializing a (i, j) list
        lins = int(winSize[0]/16)
        cols = int(winSize[1]/16)
        self.gridSize = (lins, cols)

        self.grid = [ [None] * cols ] * lins

        self.screen = screen
        self.image =  Resource.image("habitat")

    def squarePosition(self, index):
        """
        Calculates the position of the given 'square'.
        Return None if is offset.

        param:
        index => A (x,y) tuple
        """

        if index[0] > self.gridSize[0]+1 or index[1] > self.gridSize[1]+1:
            return None

        else:
            return (16 * index[0], 16 * index[1])

    def generateFirstPopulation(self):
        for i in range(self.gridSize[0]):
            for j in range(self.gridSize[1]):
                if Config.get("population", "first-percentage") >= random():
                    position = self.squarePosition((i,j))
                    self.grid[i][j] = Cell(self.screen, position)


