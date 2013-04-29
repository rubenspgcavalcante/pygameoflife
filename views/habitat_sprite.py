from core.config import Config
from core.view import *
from core.resource_manager import Resource

class HabitatSprite(View):
    def __init__(self, screen):
        View.__init__(self, screen)
        resource = Resource()
        self.config = Config()
        self.background = resource.image("bg", True)

    def generate(self):
        size = self.config.attr.game.habitat.size
        for x in range(size[0]):
            for y in range(size[1]):
                self.screen.blit(self.background, (x*16, y*16))

    def defaultAction(self):
        pass