from xml import etree
from xml.etree import ElementTree
from core.struct import Struct


class XMLConfigurationParser(object):
    def __init__(self):
        self.conf = None

    def parse(self, file):
        xml = None
        confDict = {}
        with open(file, 'rt') as confFile:
            xml = ElementTree.parse(confFile)

        for node in xml.getiterator():
            confDict[node.tag] = node.text

        self.conf = Struct(**confDict)

    def show(self):
        for node in self.conf.getiterator():
            print node.tag, node.text