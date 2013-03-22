from math import floor

import pygame
from pygame.locals import *

from core.resource_manager import Resource

class Cell:
    """Entity Cell, represents a living/dead cell"""

    def __init__(self, keepAlive=0):
        self.id = id(self)
        self.alive = True
        self.keepAlive = keepAlive

    def defaultAction(self):
        pass

    def is_dead(self):
        return not self.alive

    def damage(self):
        if self.keepAlive:
            self.keepAlive -= 1
            return False

        else:
            self.alive = False
            return True

    def kill(self):
        self.keepAlive = 0
        self.alive = False

    def birth(self):
        self.alive = True