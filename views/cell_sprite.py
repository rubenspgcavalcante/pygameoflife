from core.view import *
from core.resource_manager import Resource

class CellSprite(View):
    def __init__(self, screen):
        View.__init__(self, screen)
        resource = Resource()
        self.cell = resource.image("cell", True)
        self.background = resource.image("bg", True)

    def put(self, position):
        x, y = position[0] * 16, position[1] * 16
        self.screen.blit(self.background, (x,y))
        self.screen.blit(self.cell, (x,y))

    def remove(self, position):
        x, y = position[0] * 16, position[1] * 16
        self.screen.blit(self.background, (x,y))