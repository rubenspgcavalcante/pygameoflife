import re

class TypeParser(object):
    def __init__(self):
        pass

    def tuple(value, type):
        resList = re.sub(r'\(*\)*\ *', r"", value).split(",")
        if type == "int":
            for key, value in enumerate(resList):
                resList[key] = int(value)

        return tuple(resList)