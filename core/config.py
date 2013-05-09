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

import re
import os
from core.singleton import singleton

from core.xml_configuration_parser import XMLConfigurationParser


@singleton
class Config(object):
    def __init__(self):
        self._parser = XMLConfigurationParser()
        self._attr = self._parser.parse(os.path.join(self.getBasePath(), "config.xml"), BASEPATH=self.getBasePath())
        self._bck = self._attr

    def getBasePath(self):
        """
        Returns the project base path
        @rtype: str
        """
        path = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
        if not os.path.exists(path + "/"):
            #If compiled, the binarie is represented like a dir, so we must remove it
            path = re.sub(r'((/|\\)run-pygameoflife(.exe)?)', "", path).replace("/resource_manager.pyc", "")

        return path

    @property
    def attr(self):
        return self._attr

    @attr.setter
    def attr(self, value):
        self._attr = value

    @property
    def bck(self):
        return None

    @bck.setter
    def bck(self, value):
        pass

    def reset(self):
        """
        Resets the config object to the default state, based on config,xml
        """
        self._attr = self._bck

    def reload(self):
        """
        Force the reload of the config.xml file
        """
        self._attr = self._parser.parse("config.xml")
        self._bck = self._attr