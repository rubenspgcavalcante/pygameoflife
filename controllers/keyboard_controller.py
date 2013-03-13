import pygame
from pygame.locals import *

from core.event import *
from core.constants import *
from core.controller import *

class KeyboardController(Controller):

    def __init__(self):
        Controller.__init__(self)
        self.bind(KeyboardEvent(), self.keyMap)

    def defaultAction(self):
        pass

    def keyMap(self, event):
        triggerEvent = None
        if event.key == K_ESCAPE:
            triggerEvent = QuitEvent()

        if event.key == K_SPACE:
            triggerEvent = PauseEvent()

        elif event.key == K_UP:
            triggerEvent = ChangeSpeedEvent(DELAY_DOWN)

        elif event.key == K_DOWN:
            triggerEvent = ChangeSpeedEvent(DELAY_UP)

        elif event.key == K_LEFT:
            triggerEvent = ChangeSpeedEvent(DELAY_UP)

        elif event.key == K_RIGHT:
            triggerEvent = ChangeSpeedEvent(DELAY_DOWN)

        if triggerEvent:
            self.trigger(triggerEvent)