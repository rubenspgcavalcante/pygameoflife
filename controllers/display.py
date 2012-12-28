import pygame

from config import Config
from resources.manager import Resource

class DisplayController(object):

    """Manages the display"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Config.get("game", "window-size"))
        pygame.display.set_icon(Resource.image("icon"))
        pygame.display.set_caption(Resource.get("display", "title"))

    def getScreen(self):
        return self.screen

    def update(self):
        pygame.time.wait(Resource.get("display", "sleep"))
        pygame.display.update()
        pass
