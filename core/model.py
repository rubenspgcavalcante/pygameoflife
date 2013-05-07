import os
import pickle
from core.config import Config
from core.error import CacheError

class Model(object):
    def __init__(self):
        self._cachePath = os.path.join(Config().attr.path.resources, Config().attr.path.cache)
        pass

    def saveState(self, prefix=""):
        """
        Saves the state of the object into the cache
        Only one object can be stored per time
        @type prefix: str
        @param prefix: A prefix to add into the cache file name
        """
        try:
            with open(os.path.join(self._cachePath, prefix + self.__class__.__name__ + ".cache"), "wb") as dump:
                pickle.dump(self, dump, pickle.HIGHEST_PROTOCOL)

        except Exception as e:
            raise CacheError(e)

    def loadState(self, prefix=""):
        """
        Loads the last state saved of this object
        @type prefix: str
        @param prefix: A prefix to add into the cache file name
        @rtype: Model
        """
        try:
            with open(os.path.join(self._cachePath, prefix + self.__class__.__name__ + ".cache"), "rb") as dump:
                return pickle.load(dump)

        except Exception as e:
            raise CacheError(e)