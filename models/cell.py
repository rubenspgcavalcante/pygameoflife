import pygame
from pygame.locals import *

from resources.manager import Resource

class Cell(object):
    """Entity Cell, represents a living/dead cell"""

    def __init__(self, screen, position):
        self.id = id(self)

        self.lifeRange = {"min": 0, "max": 10}
        self.life = self.lifeRange["max"]

        self.images = Resource.sprite("cell")
        self.image = self.get_image()
        self.position = position
        self.screen = screen

        screen.blit(self.image, position)

    def is_dead(self):
        return self.life == self.lifeRange["min"]

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
        prop = (Resource.get("cell", "frames") * self.life)/self.lifeRange["max"]
        state = int(prop)

        return self.images[state-1]

    def update(self):
        """Updates the image of this cell in the screen. If the cell is dead
        don't plot it again"""

        if self.is_dead():
            return False
        else:
            self.screen.blit(self.get_image(), self.position)
            return True