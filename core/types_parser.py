import re

class TypeParser(object):
    def __init__(self):
        pass

    def tuple(self, value, type):
        """
        Parse a string value into a tuple of the given type

        @type value: str
        @param value: The string value to convert
        @type type: str
        @param type: The type of tuple to convert, e.g: int
        @rtype : tuple
        """
        resList = re.sub(r'\(*\)*\ *', r"", value).split(",")
        if type == "int":
            for key, value in enumerate(resList):
                resList[key] = int(value)

        return tuple(resList)

    def int(self, value):
        """
        Convert a string into a integer

        @type value: str
        @param value: The string to convert e.g: "10"
        @rtype: int
        """
        return int(value.replace(" ", ""))

    def float(self, value):
        """
        Convert a string into a float
        @type value: str
        @param value: The string to convert e.g: "10"
        @rtype: float
        """
        return float(value.replace(" ", ""))