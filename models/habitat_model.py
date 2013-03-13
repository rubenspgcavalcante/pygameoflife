from random import random

import pygame
from pygame.locals import *

from core.event import SetCellEvent
from core.model import Model
from core.config import Config

from models.cell_model import Cell

from resources.manager import Resource

class Habitat(Model):

    """
    Habitat of the cells.
    Represented by a grid with the size of the window
    """
    def __init__(self):
        Model.__init__(self)
        winSize = Config().get("game", "window-size")

        #Initializing a (i, j) list
        lins = int(winSize[0]/16)
        cols = int(winSize[1]/16)
        self.gridSize = (lins, cols)

        self.grid = [ [None] * cols for i in range(lins)]
        self.bind(SetCellEvent(), self.setCell)

    def defaultAction(self):
        pass

    def generateFirstPopulation(self):
        for i in range(self.gridSize[0]):
            for j in range(self.gridSize[1]):
                if Config().get("population", "first-percentage") >= random():
                    self.grid[i][j] = Cell()

    def setCell(self, event):
        x, y = event.posx, event.posy
        x = int(x/16)
        y = int(y/16)
        self.grid[x][y] = Cell()


    def check_neighborhood(self, position):
        """
        Checks the neighborhood and return the number of cells.
        The verification is made in a 3x3 matrix, with this cell in the
        center of it.
        """
        width, height = position
        count = 0

        #Caring the corners!
        for lin in range(width - 1, width + 2):
            for col in range(height - 1, height + 2):

                if lin < 0 or lin > len(self.grid) - 1:
                    continue

                if col < 0 or col > len(self.grid[0]) - 1:
                    continue

                #We'll not count the cell itself
                if (lin, col) == position:
                    continue

                elif self.grid[lin][col] != None:
                    if not self.grid[lin][col].is_dead():
                        count += 1

        return count

    def who_die_or_birth(self):
        """
        Checks who dies/birth and genarate a black/white list respectively
        """

        #Who will die
        blacklist = []

        #Who will birth
        whitelist = []

        #Mantain the state
        stables = []

        for i in range(self.gridSize[0]):
            for j in range(self.gridSize[1]):

                position = (i, j)
                neighbors = self.check_neighborhood(position)

                #Populated cell
                if self.grid[i][j] != None and not self.grid[i][j].is_dead():

                    if neighbors < 2:
                        blacklist.append(position)

                    elif neighbors > 3:
                        blacklist.append(position)

                    else:
                        stables.append(position)

                #Empty cell or Unpopulated
                else:
                    if neighbors == 3:
                        whitelist.append(position)

        return (whitelist, blacklist, stables)

    def nextGeneration(self):
        whitelist, blacklist, stables = self.who_die_or_birth()

        #Kill cells
        for pos in blacklist:
            lin, col = pos
            self.grid[lin][col].kill()

        #Birth cells
        for pos in whitelist:
            lin, col = pos
            if self.grid[lin][col] == None:
                self.grid[lin][col] = Cell()

            else:
                self.grid[lin][col].birth()

        return (whitelist, blacklist, stables)
