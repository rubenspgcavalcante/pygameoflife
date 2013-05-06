import os
import pickle
from core.config import Config


class Model(object):
    def __init__(self):
        self._cachePath = os.path.join(Config().attr.path.resources, Config().attr.path.cache)
        pass

    def saveState(self):
        """
        Saves the state of the object into the cache
        Only one object can be stored per time
        """
        with open(os.path.join(self._cachePath, self.__class__.__name__ + ".cache"), "wb") as dump:
            pickle.dump(self, dump, pickle.HIGHEST_PROTOCOL)

    def loadState(self):
        """
        Loads the last state saved of this object
        @rtype: Model
        """
        with open(os.path.join(self._cachePath, self.__class__.__name__ + ".cache"), "rb") as dump:
            return pickle.load(dump)