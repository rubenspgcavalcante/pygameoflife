import pygame
from pygame.locals import *

from core.view import *
from core.resource_manager import Resource

class CellSprite(View):
    def __init__(self, screen):
        View.__init__(self)

        self.screen = screen
        self.images = Resource.sprite("cell")
        self.background = Resource.image("bg", True)

    def get_image(self, state):
        return self.images[state]

    def put(self, position, state):
        x, y = position[0] * 16, position[1] * 16
        self.screen.blit(self.background, (x,y))
        self.screen.blit(self.get_image(state), (x,y))

    def remove(self, position):
        x, y = position[0] * 16, position[1] * 16
        self.screen.blit(self.background, (x,y))