import pygame
from pygame.locals import *

from core.event import *
from core.controller import *
from core.event import *
from models.game_model import Game
from views.cell_sprite import CellSprite
from views.habitat_sprite import HabitatSprite

from config import *
from resources.manager import *

class DisplayController(Controller):
    def __init__(self, game):
        Controller.__init__(self)

        pygame.init()

        self.screen = None
        self.backSprites = pygame.sprite.RenderUpdates()
        self.frontSprites = pygame.sprite.RenderUpdates()
        self.bind(GameStartEvent(), self.show)

        self.game = game
        self.bind(NewGenerationEvent(), self.getGeneration)

    def getGeneration(self, event):
        cellSprite = CellSprite(self.screen)
        for position in event.whitelist:
            cellSprite.put(position)

        for position in event.blacklist:
            cellSprite.remove(position)

        pygame.display.flip()


    def show(self, event):
        config = Config()
        self.screen = pygame.display.set_mode(config.get("game", "window-size"))
        pygame.display.set_icon(Resource.image("icon", static=True))
        pygame.display.set_caption(Resource.get("display", "title"))
        habitat = HabitatSprite()
        habitat.generate(self.screen)
        self.game.state = Game.STATE_RUNNING

    def defaultAction(self):
        pass

