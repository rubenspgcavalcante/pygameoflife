from math import floor

import pygame
from pygame.locals import *

from resources.manager import Resource

class Cell(object):
    """Entity Cell, represents a living/dead cell"""

    def __init__(self, screen, position, life=None):
        self.id = id(self)

        self.lifeRange = {"min": 0, "max": 10}

        if life is not None:
            self.life = life
        else:
            self.life = self.lifeRange["max"]

        self.images = Resource.sprite("cell")
        self.position = position
        self.screen = screen

        screen.blit(self.get_image(), position)

    def is_dead(self):
        return self.life == self.lifeRange["min"]

    def kill(self):
        self.change_life(-self.lifeRange["max"])

    def rebirth(self):
        self.change_life(self.lifeRange["max"])

    def change_life(self, value):
        """Increase/Decrease life of the cell, limited by max/min life

        Keyword argument:
        value -- Integer value to increment in life

        """

        if self.life + value < self.lifeRange["min"]:
            self.life = self.lifeRange["min"]

        elif self.life + value > self.lifeRange["max"]:
            self.life = self.lifeRange["max"]

        else:
            self.life += value

    def get_image(self):
        """Get the image representing the current state of the cell, based into
        his life"""

        #Using proportional state
        prop = (self.lifeRange["max"] * self.life)/Resource.get("cell", "frames")
        state = int(floor(prop))+1

        return self.images[state]

    def update(self):
        """Updates the image of this cell in the screen. If the cell is dead
        don't plot it again"""

        if self.is_dead():
            return False
        else:
            self.screen.blit(self.get_image(), self.position)
            return True