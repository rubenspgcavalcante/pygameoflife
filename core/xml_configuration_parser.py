import re
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from core.struct import Struct
from core.types_parser import TypeParser


class XMLConfigurationParser(object):
    def __init__(self):
        self.conf = None
        self.typeParser = TypeParser()

    def clean(self, text):
        if text is not None:
            return text.replace(" ", "").replace("\n", "").replace("\t", "")
        else:
            return ""

    def parseTupleTag(self, element):
        """
        Parses a tag of type 'tuple' and analyse the content type
        of this tuple

        @type element: Element
        @param element: The element tree which contains the tag
        """
        attributeType = element.attrib["type"]
        if re.match(r'(int)', attributeType):
            return self.typeParser.tuple(element.attrib["type"], 'int')

        elif re.match(r'(str)', attributeType):
            return self.typeParser.tuple(element.attrib["type"], 'str')

    def XMLToDict(self, parent_element):
        """
        Parse a XML etree object into a dict, recursively

        @type parent_element: Element
        @param parent_element: The parent element to serve as the wraper of the dict
        @returns The parsed dict
        """
        result = dict()
        for element in parent_element:
            if len(element):
                obj = self.XMLToDict(element)
            else:
                obj = self.clean(element.text)

            if result.get(element.tag):
                if hasattr(result[element.tag], "append"):
                    result[element.tag].append(obj)
                else:
                    result[element.tag] = [result[element.tag], obj]
            else:
                if 'type' in element.attrib and re.match(r'(tuple)', element.attrib["type"]):
                    obj = self.parseTupleTag(element)

                result[element.tag] = obj
        return result

    def parse(self, file):
        xml = None
        with open(file, 'rt') as confFile:
            xml = ElementTree.parse(confFile)

        confDict = self.XMLToDict(xml._root)
        self.conf = Struct(**confDict)

x = XMLConfigurationParser()
x.parse("/home/trix-rubens/projetos/pygameoflife/config.xml")