import pygame
from pygame.locals import *

from core.view import *
from resources.manager import *

class CellSprite(View):
    def __init__(self, screen):
        View.__init__(self)

        self.screen = screen
        self.images = Resource.sprite("cell")
        self.background = Resource.image("bg")

    def get_image(self):
        """Get the image representing the current state of the cell, based into
        his life"""

        return self.images[9]

    def put(self, position):
        """Updates the image of this cell in the screen. If the cell is dead
        don't plot it again"""

        x, y = position[0] * 16, position[1] * 16
        self.screen.blit(self.background, (x,y))
        self.screen.blit(self.get_image(), (x,y))

    def remove(self, position):
        x, y = position[0] * 16, position[1] * 16
        self.screen.blit(self.background, (x,y))