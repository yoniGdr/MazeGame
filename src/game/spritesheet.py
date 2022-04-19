import pygame
import sys
sys.path.insert(0,'..')
from config import *

class Spritesheet:
    """
    Class used to grab images out of a sprite sheet.
    """
    def __init__(self, file):
        """
        Constructor the load the sprite sheet.
        
        :param file: The file name of the sprite sheet.
        """

        self.imageURL = file
        self.sheet = pygame.image.load(file).convert_alpha() # convert_alpha

    def get_image(self, x, y, width, height):
        """
        Grab an image out of a larger spritesheet.

        :param x: The x coordinate of the sprite.
        :param y: The y coordinate of the sprite.
        :param width: The width of the sprite.
        :param height: The height of the sprite.
        """
        image = pygame.Surface([width-2, height-2])
        image.blit(self.sheet, (0, 0), (x, y, 32, 32))  # dessiner une image sur une autre
        image.set_colorkey(BLACK) # rendre le fond noire inutile de l'image en transparent
        return image

    def get_imageURL(self):
        """
        Return the URL of the sprite sheet.

        :return: The URL of the sprite sheet.
        """
        return self.imageURL


