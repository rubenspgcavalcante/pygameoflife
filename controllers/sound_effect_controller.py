import pygame

from core.controller import Controller
from core.resource_manager import Resource
from core.event import *
from core.config import Config

class SoundEffectController(Controller):

    def __init__(self):
        Controller.__init__(self)
        pygame.mixer.init()
        self.musicOn = False

        self.effects = {
            "bubble": Resource.audio("bubble.wav"),
            "click": Resource.audio("click.wav"),
            "delete": Resource.audio("delete.wav"),
        }

        self.bgSound = Resource.audio("bg.wav", music=True)

        self.bind(CellAddedEvent(), self.onCellAddedDoBubble)
        self.bind(CellRemovedEvent(), self.onCellRemovedDoDelete)
        self.bind(PauseEvent(), self.onPauseDoClick)
        self.bind(GameStartEvent(), self.onGameStartDoBackground)

    def defaultAction(self):
        pass


    def onCellAddedDoBubble(self, event):
        self.effects["bubble"].stop()
        self.effects["bubble"].play()


    def onCellRemovedDoDelete(self, event):
        self.effects["delete"].stop()
        self.effects["delete"].play()


    def onPauseDoClick(self, event):
        self.effects["click"].stop()
        self.effects["click"].play()

        if self.musicOn:
            self.bgSound.pause()
            self.musicOn = False

        else:
            self.bgSound.unpause()
            self.musicOn = True


    def onGameStartDoBackground(self, event):
        pygame.mixer.music.set_volume(Config().get("game", "music-volume"))
        fxVol = Config().get("game", "effects-volume")
        
        for i in self.effects:
            self.effects[i].set_volume(fxVol)

        self.bgSound.play()
        self.musicOn = True