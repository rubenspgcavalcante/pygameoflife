from random import random

import pygame
from pygame.locals import *

from models.cell import Cell

from resources.manager import Resource
from config import Config
from helpers.singleton import singleton

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

        self.grid = [ [None] * cols for i in range(lins)]

        self.screen = screen
        self.image =  Resource.image("habitat")
        self.screen.blit(self.image, (0,0))

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

                    elif neighbors in (2,3):
                        stables.append(position)
                        pass

                    elif neighbors > 3:
                        blacklist.append(position)

                #Empty cell or Unpopulated
                else:
                    if neighbors == 3:
                        whitelist.append(position)

        return {"whitelist": whitelist, "blacklist": blacklist, "stables": stables}

    def nextGeneration(self):
        lists = self.who_die_or_birth()
        self.update()

        #Kill cells
        for pos in lists["blacklist"]:
            lin, col = pos
            self.grid[lin][col].kill()
            self.grid[lin][col].update()

        for pos in lists["whitelist"]:
            lin, col = pos
            if self.grid[lin][col] == None:
                pixelPos = self.squarePosition(pos)
                self.grid[lin][col] = Cell(self.screen, pixelPos)

            else:
                self.grid[lin][col].rebirth()
                self.grid[lin][col].update()

        for pos in lists["stables"]:
            lin, col = pos
            self.grid[lin][col].update()


    def update(self):
        self.screen.blit(self.image, (0,0))
