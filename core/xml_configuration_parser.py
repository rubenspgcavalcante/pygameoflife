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
        e.g.:
            <tag type="tuple(int)">(20, 10)</tag>
            <tag type="tuple(float)">(20.3, 10.1)</tag>
            <tag type="tuple(str)">(hello, world)</tag>

        @type element: Element
        @param element: The element tree which contains the tag
        @rtype : tuple
        """
        attributeType = element.attrib["type"]
        if attributeType == "tuple(int)":
            return self.typeParser.tuple(element.text, 'int')

        elif attributeType == "tuple(float)":
            return self.typeParser.tuple(element.text, 'float')

        elif attributeType == "tuple(str)":
            return self.typeParser.tuple(element.text, 'str')

    def processType(self, element):
        """
        Process a value using the default cast, referenced by the type
        attribute into the tag
        e.g.:
            <tag type="int">20</tag>
            <tag type="float">1.9</tag>

        @type element: Element
        @param element: The tag to covert
        """
        if re.match(r'(tuple)', element.attrib["type"]):
            processed = self.parseTupleTag(element)

        elif element.attrib["type"] == "int":
            processed = self.typeParser.int(element.text)

        elif element.attrib["type"] == "float":
            processed = self.typeParser.float(element.text)

        else:
            processed = element.text

        return processed

    def XMLToDict(self, parent_element, template_args=None):
        """
        Parse a XML etree object into a dict, recursively

        @type parent_element: Element
        @param parent_element: The parent element to serve as the wrapper of the dict

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
                    obj = self.processType(element)

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