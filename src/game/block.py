import pygame
from config import *
from element import Element

class Block(Element):
    """
    Class that represents a block
    """
    def __init__(self,game, x: int, y: int):
        """
        Constructor of the class

        :param game: the game object
        :param x: the x position of the block
        :param y: the y position of the block
        """
        super().__init__(x, y,TILESIZE, TILESIZE , BLOCK_LAYER,'../assets/img/wall_2.png', 0, 0,None)
        self.game = game
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)


        #image_wall = pygame.image.load("img/wall_2.png")
        #self.image = pygame.Surface([self.width, self.height])
        #self.image.blit(image_wall, (0,0))

