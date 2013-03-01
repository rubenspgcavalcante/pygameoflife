from core.view import *

class CellSprite(View):
    def __init__(self):
        View.__init__(self)

        self.images = Resource.sprite("cell")
        self.position = position
        self.screen = screen

        screen.blit(self.get_image(), position)

    def get_image(self):
        """Get the image representing the current state of the cell, based into
        his life"""

        #Using proportional state
        prop = (self.lifeRange["max"] * self.life)/Resource.get("cell", "frames")
        state = int(floor(prop))+1

        return self.images[state]

    def update(self):
        """Updates the image of this cell in the screen. If the cell is dead
        don't plot it again"""

        if self.is_dead():
            return False
        else:
            self.screen.blit(self.get_image(), self.position)
            return True

    def squarePosition(self, index):
        """
        Calculates the position of the given 'square'.
        Return None if is offset.

        param:
        index => A (x,y) tuple
        """

        if index[0] > self.gridSize[0]+1 or index[1] > self.gridSize[1]+1:
            return None

        else:
            return (16 * index[0], 16 * index[1])