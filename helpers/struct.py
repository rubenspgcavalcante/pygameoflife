class Struct:
    """Transforms a dict into a struct"""
    def __init__(self, **entries): 
        self.__dict__.update(entries)