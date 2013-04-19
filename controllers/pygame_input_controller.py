import pygame
from pygame.locals import *

from core.event import *
from core.controller import *

class PygameInputController(Controller):

    def __init__(self):
        Controller.__init__(self)

    def defaultAction(self):
        for pygameEvent in pygame.event.get():
            event = None
            if pygameEvent.type == QUIT:
                event = QuitEvent()

            elif pygameEvent.type == KEYDOWN:
                event = KeyboardEvent(pygameEvent.key)

            elif pygameEvent.type == pygame.MOUSEBUTTONDOWN:
                event = MouseEvent(pygameEvent.button)

            if event:
                self.trigger(event)