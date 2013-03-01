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

    def defaultAction(self):
        if self.state == Game.STATE_RUNNING:
            lists = self.habitat.nextGeneration()
            whitelist, blacklist = lists["whitelist"], lists["blacklist"]
            self.trigger(NewGenerationEvent(whitelist, blacklist))