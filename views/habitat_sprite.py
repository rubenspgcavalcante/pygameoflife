from core.view import *
from resources.manager import Resource

class HabitatSprite(View):
    def __init__(self):
        View.__init__(self)
        self.background = Resource.image("bg", True)

    def generate(self, screen):
        resources = Resource()
        size = resources.get("habitat", "size")
        for x in range(size[0]):
            for y in range(size[1]):
                screen.blit(self.background, (x*16, y*16))

    def defaultAction(self):
        pass