class Struct:
    def __init__(self, **entries):
        """
        Transforms a simple dict object into a structured object

        @type entries: dict
        @param entries: The dict to be transformed into struct
        """
        for key, value in entries.items():
            if type(value) == dict:
                entries[key] = Struct(**value)

        self.__dict__.update(entries)

    def __str__(self):
        buffer = ""
        self._prettyString(buffer)
        return buffer

    def _prettyString(self, buffer, ident=0):
        for i in dir(self):
            if i not in ('__doc__', '__init__', '__module__', '__str__', '_prettyString'):
                if self.__dict__[i].__class__.__name__ == 'Struct':
                    buffer = ("\t" * ident) + i + ":"
                    self.__dict__[i]._prettyString(buffer, ident+1)

                else:
                    buffer = ("\t" * ident) + i