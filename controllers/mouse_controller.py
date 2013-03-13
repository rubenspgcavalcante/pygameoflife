import pygame
from pygame.locals import *

from core.event import *
from core.constants import *
from core.controller import *

class MouseController(Controller):

    def __init__(self):
        Controller.__init__(self)
        self.pushed = False
        self.bind(MouseEvent(), self.buttonMap)

    def defaultAction(self):
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            self.trigger(SetCellEvent(pos[0], pos[1]))

    def buttonMap(self, event):
        triggerEvent = None
        if event.button == 1:
            pos = pygame.mouse.get_pos()
            triggerEvent = SetCellEvent(pos[0], pos[1])

        if triggerEvent:
            self.trigger(triggerEvent)