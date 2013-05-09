#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Rubens Pinheiro Gonçalves Cavalcante"
__date__ = "08/05/13 19:18"
__licence__ = "GPLv3"
__email__ = "rubenspgcavalcante@gmail.com"

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