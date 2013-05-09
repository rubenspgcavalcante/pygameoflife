#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Rubens Pinheiro Gonçalves Cavalcante"
__date__ = "08/05/13 19:18"
__licence__ = "GPLv3"
__email__ = "rubenspgcavalcante@gmail.com"

from random import random
from ctypes import *
from core.error import CacheError

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
        winSize = Config().attr.game.window.size

        #Initializing a (i, j) list
        lins = int(winSize[0]/16)
        cols = int(winSize[1]/16)
        Config().attr.game.habitat.size = (lins, cols)
        self.gridSize = (lins, cols)
        self.keepAlive = []
        self.grid = [[None] * cols for i in range(lins)]


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
                if Config().attr.game.population.percentage >= random():
                    self.grid[i][j] = True
                else:
                    self.grid[i][j] = False

        self.turnIntoCArray()

    def turnIntoCArray(self):
        entrylist = []
        for sublist in self.grid:
            entrylist.append((c_ubyte * len(sublist))(*sublist))

        self.grid = (POINTER(c_ubyte) * len(entrylist))(*entrylist)

    def saveState(self):
        lins, cols = self.gridSize
        bckpList = [[None] * cols for i in range(lins)]
        for i in range(lins):
            for j in range(cols):
                bckpList[i][j] = self.grid[i][j]

        del self.grid
        self.grid = bckpList
        prefixName = str(lins) + "x" + str(cols)
        super(Habitat, self).saveState(prefix=prefixName)
        self.turnIntoCArray()

    def loadState(self):
        prefixName = str(self.gridSize[0]) + "x" + str(self.gridSize[1])
        habitat = super(Habitat, self).loadState(prefix=prefixName)
        habitat.turnIntoCArray()
        return habitat

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
