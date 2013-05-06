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