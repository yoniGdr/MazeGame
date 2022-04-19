import pygame
import sys
sys.path.insert(0,'..')
from config import *
from spritesheet import *

# write documentation

class Element(pygame.sprite.Sprite):
    def __init__(self,x: int, y : int, width : int,height : int,layer,imgURL : str, x_sheet : int,y_sheet : int , groups : list):
        """
        Constructor for the Element class.

        :param x: x coordinate of the element
        :param y: y coordinate of the element
        :param width: width of the element
        :param height: height of the element
        :param layer: layer of the element
        :param imgURL: URL of the image
        :param x_sheet: x coordinate of the image on the spritesheet
        :param y_sheet: y coordinate of the image on the spritesheet
        :param groups: groups of the element
        """
        self._layer = layer
        self.groups = groups

        self.width = width
        self.height = height

        self.x = x * self.width
        self.y = y * self.height
        
        self.spritesheet = Spritesheet(imgURL)
        self.image = self.spritesheet.get_image(x_sheet,y_sheet,width,height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def set_groups(self,groups):
        """
        Setter for the groups of the element.

        :param groups: groups of the element
        """
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)


    # getters
    def get_layer(self):
        """
        Gets the layer of the element.

        :return: layer of the element
        """
        return self._layer

    def get_x(self):
        """
        Gets the x coordinate of the element.

        :return: x coordinate of the element
        """

        return self.rect.x

    def get_y(self):
        """
        Gets the y coordinate of the element.

        :return: y coordinate of the element
        """
        return self.rect.y

    def get_width(self):
        """
        Gets the width of the element.

        :return: width of the element
        """
        return self.width

    def get_height(self):
        """
        Gets the height of the element.

        :return: height of the element
        """
        return self.height

    def get_rect(self):
        """
        Gets the rectangle of the element.

        :return: rect of the element
        """
        return self.rect

    def get_image(self):
        """
        Gets the image of the element.

        :return: image of the element
        """
        return self.image

    def get_spritesheet(self):
        """
        Gets the spritesheet of the element.

        :return: spritesheet of the element
        """
        return self.spritesheet


    def change_image(self,imgURL,x_sheet,y_sheet,width,height):
        """
        Change the image of the element.

        :param imgURL: URL of the image
        :param x_sheet: x coordinate of the image on the spritesheet
        :param y_sheet: y coordinate of the image on the spritesheet
        :param width: width of the image
        :param height: height of the image
        """
        self.spritesheet=Spritesheet(imgURL)
        self.image = self.spritesheet.get_image(x_sheet,y_sheet,width,height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    


