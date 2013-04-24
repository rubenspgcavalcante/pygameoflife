import os

import pygame

from core.event import *
from core.controller import *
from core.config import *

from models.game_model import Game
from views.cell_sprite import CellSprite
from views.habitat_sprite import HabitatSprite
from views.notification_sprite import *


class DisplayController(Controller):
    """
    Controls all the display actions and responses
    """
    def __init__(self, game):
        """
        Initiates the display controller
        @type game: Game
        @param game: The associated game model
        """
        Controller.__init__(self)
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        pygame.init()

        self.screen = None
        self.speed = None
        self.speedUpNotification = None
        self.speedDownNotification = None
        self.activeNotification = None

        self.layers = []
        self.game = game
        self.cellStates = [[0] * self.game.habitat.gridSize[1] for x in xrange(self.game.habitat.gridSize[0])]

        self.bind(GameStartEvent(), self.show)
        self.bind(ChangeSpeedEvent(), self.changeSpeed)
        self.bind(SetCellEvent(), self.setCell)
        self.bind(DelCellEvent(), self.delCell)

    def defaultAction(self):
        if self.game.nextIteration():
            self.speed = Config().get("game", "speed")

            #Animation loop
            pygame.time.wait(self.speed)
            self.trigger(DisplayRefreshEvent(0))
            self.updateCells()

            self.trigger(DisplayRefreshEvent(3))
            pygame.display.flip()

    def setCell(self, event):
        cellWidth, cellHeight = Resource.get("cell", "size")
        x, y = int(event.posx)/cellWidth, int(event.posy)/cellHeight

        if self.game.habitat.setCell(x, y):
            #The value ten means hi will live for 10 generations
            self.cellStates[x][y] = 10
            cellSprite = CellSprite(self.screen)
            cellSprite.put((x, y))
            pygame.display.flip()
            self.trigger(CellAddedEvent())

    def delCell(self, event):
        cellWidth, cellHeight = Resource.get("cell", "size")
        x, y = int(event.posx)/cellWidth, int(event.posy)/cellHeight

        if self.game.habitat.delCell(x, y):
            self.cellStates[x][y] = 0
            cellSprite = CellSprite(self.screen)
            cellSprite.remove((x, y))
            pygame.display.flip()
            self.trigger(CellRemovedEvent())

    def updateCells(self):
        cellSprite = CellSprite(self.screen)

        for i in range(self.game.habitat.gridSize[0]):
            for j in range(self.game.habitat.gridSize[1]):
                #If a cell is setted to keeps alive
                if self.cellStates[i][j] > 1:
                    self.cellStates[i][j] -= 1
                    self.game.habitat.grid[i][j] = 1

                if self.game.habitat.grid[i][j]:
                    if not self.cellStates[i][j]:
                        self.cellStates[i][j] = 1
                        cellSprite.put((i, j))

                elif self.cellStates[i][j]:
                    self.cellStates[i][j] = 0
                    cellSprite.remove((i, j))

    def changeSpeed(self, event):
        currentSpeed = Config().get("game", "speed")
        difference = currentSpeed + event.delayChange
        
        if event.state == ChangeSpeedEvent.UP:
            self.trigger(ShowNotificationEvent("speedUp"))

        elif event.state == ChangeSpeedEvent.DOWN:
            self.trigger(ShowNotificationEvent("speedDown"))

        if difference < 0 or difference < Config().get("game", "min-delay"):
            currentSpeed = Config().get("game", "min-delay")

        elif difference > Config().get("game", "max-delay"):
            currentSpeed += Config().get("game", "min-delay")

        else:
            currentSpeed = difference

        Config().set("game", "speed", currentSpeed)

    def show(self, event):
        config = Config()
        self.screen = pygame.display.set_mode(config.get("game", "window-size"))
        pygame.display.set_icon(Resource.image("icon", static=True))
        pygame.display.set_caption(Resource.get("display", "title"))

        habitat = HabitatSprite()
        habitat.generate(self.screen)

        self.speedUpNotification = SpeedUpNotification(self.screen)
        self.speedDownNotification = SpeedDownNotification(self.screen)

        self.game.state = Game.STATE_RUNNING
        self.trigger(ScreenAvaibleEvent(self.screen))