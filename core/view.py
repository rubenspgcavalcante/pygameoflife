from pygame import display

class View():
    def __init__(self, screen):
        """
        View associated to a pygame screen
        @type screen: pygame.display
        @param screen: The pygame screen module reference
        """
        self.screen = screen