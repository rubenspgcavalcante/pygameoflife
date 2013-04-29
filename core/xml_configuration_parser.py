import re
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from core.struct import Struct
from core.types_parser import TypeParser


class XMLConfigurationParser(object):
    def __init__(self):
        self.typeParser = TypeParser()

    def clean(self, text):
        if text is not None:
            return text.replace("\n", "").replace("\t", "")
        else:
            return ""

    def parseTupleTag(self, element):
        """
        Parses a tag of type 'tuple' and analyse the content type
        of this tuple

        @type element: Element
        @param element: The element tree which contains the tag
        @rtype : tuple
        """
        attributeType = element.attrib["type"]
        if attributeType == "tuple(int)":
            return self.typeParser.tuple(element.text, 'int')

        elif attributeType == "tuple(str)":
            return self.typeParser.tuple(element.text, 'str')

    def XMLToDict(self, parent_element, template_args=None):
        """
        Parse a XML etree object into a dict, recursively

        @type parent_element: Element
        @param parent_element: The parent element to serve as the wraper of the dict

        @type template_args: dict
        @param template_args: Template arguments to process the tags with the 'template' attribute
        @returns The parsed dict
        """
        result = dict()
        for element in parent_element:
            if len(element):
                obj = self.XMLToDict(element, template_args)
            else:
                obj = self.clean(element.text)

            if result.get(element.tag):
                if hasattr(result[element.tag], "append"):
                    result[element.tag].append(obj)
                else:
                    result[element.tag] = [result[element.tag], obj]
            else:
                if 'type' in element.attrib:
                    if re.match(r'(tuple)', element.attrib["type"]):
                        obj = self.parseTupleTag(element)

                    elif element.attrib["type"] == "int":
                        obj = self.typeParser.int(element.text)

                    elif element.attrib["type"] == "float":
                        obj = self.typeParser.float(element.text)

                if 'template' in element.attrib:
                    if element.attrib['template'] == 'true' and template_args != None:
                        obj = element.text.format(**template_args)

                result[element.tag] = obj
        return result

    def parse(self, filePath, **variables):
        """
        Parse a file and loads it into a structured format

        @type filePath: str
        @param filePath: The path to the XML configuration file

        @type variables: dict
        @param variables: The template variables to substitute in the xml file

        @rtype : Struct
        """
        xml = None
        with open(filePath, 'rt') as confFile:
            xml = ElementTree.parse(confFile)

        confDict = self.XMLToDict(xml._root, variables)
        return Struct(**confDict)