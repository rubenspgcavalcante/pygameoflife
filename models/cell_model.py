from math import floor

import pygame
from pygame.locals import *

from core.model import Model
from resources.manager import Resource

class Cell(Model):
    """Entity Cell, represents a living/dead cell"""

    def __init__(self, keepAlive=0):
        Model.__init__(self)
        self.id = id(self)
        self.alive = True
        self.keepAlive = keepAlive

    def defaultAction(self):
        pass

    def is_dead(self):
        return not self.alive

    def kill(self):
        if self.keepAlive:
            self.keepAlive -= 1
            return False

        else:
            self.alive = False
            return True

    def birth(self):
        self.alive = True