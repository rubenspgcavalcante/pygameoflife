from core.model import Model
from core.event import *
from models.habitat_model import Habitat

class Game(Model):

    STATE_PREPARING = 'preparing'
    STATE_RUNNING = 'running'
    STATE_PAUSED = 'paused'

    def __init__(self):
        Model.__init__(self)
        self.habitat = Habitat()
        self.habitat.generateFirstPopulation()
        self.state = Game.STATE_PREPARING
        self.bind(PauseEvent(), self.pause)

    def pause(self, event):
        if self.state == Game.STATE_RUNNING:
            self.state = Game.STATE_PAUSED

        elif self.state == Game.STATE_PAUSED:
            self.state = Game.STATE_RUNNING

    def defaultAction(self):
        if self.state == Game.STATE_RUNNING:
            whitelist, blacklist, stables = self.habitat.nextGeneration()
            self.trigger(NewGenerationEvent(whitelist, blacklist, stables))

        elif self.state == Game.STATE_PAUSED:
            pass