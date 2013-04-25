from core.view import *
from core.resource_manager import Resource

class HabitatSprite(View):
    def __init__(self, screen):
        View.__init__(self, screen)
        self.background = Resource.image("bg", True)

    def generate(self):
        resources = Resource()
        size = resources.get("habitat", "size")
        for x in range(size[0]):
            for y in range(size[1]):
                self.screen.blit(self.background, (x*16, y*16))

    def defaultAction(self):
        pass