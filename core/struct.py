class Struct:
    def __init__(self, **entries):
        for key, value in entries.items():
            if type(value) == dict:
                entries[key] = Struct(**value)

        self.__dict__.update(entries)

    def showAttributes(self, ident=0):
        for i in dir(self):
            if i not in ('__doc__', '__init__', '__module__', 'showAttributes'):
                if self.__dict__[i].__class__.__name__ == 'Struct':
                    print ("\t" * ident) + i +":"
                    self.__dict__[i].showAttributes(ident+1)

                else:
                    print ("\t" * ident) + i