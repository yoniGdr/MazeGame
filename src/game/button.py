import sys
sys.path.insert(0,'..')
from config import *
from spritesheet import *

class Button:
    """
    Class that represents a button
    and handles the logic of the button
    """
    def __init__(self, x : int, y : int, width : int, height : int, fg, content, fontsize):
        """
        Initializes the button

        :param x: x coordinate of the button
        :param y: y coordinate of the button
        :param width: width of the button
        :param height: height of the button
        :param fg: foreground color of the button
        :param content: content of the button
        :param fontsize: font size of the button
        """


        self.font = pygame.font.Font('../assets/img/font.ttf', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fg = fg

        self.image = pygame.Surface((self.width, self.height)) # simple rectangle pour notre boutons
        self.image.fill(BOUTON_COLOR) # color rect
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg) # Applique la police sur le texte
        self.text_rect = self.text.get_rect(center=(self.width/2,self.height/2)) # Position du texte (milieu du boutons)
        self.image.blit(self.text, self.text_rect) # Dessine le texte sur l'image ( le rect )


    def is_pressed(self, pos, pressed):
        """
        Checks if the button is pressed

        :param pos: position of the mouse
        :param pressed: if the mouse is pressed
        :return: True if the button is pressed, False otherwise
        """
        if self.rect.collidepoint(pos):
            if pressed[0]: # correspond au clic gauche
                return True
            return False
        return False
