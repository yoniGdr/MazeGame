import pygame
import sys
sys.path.insert(0,'..')
from config import *
from element import Element

class Ground(Element):
    """
    Class for the ground
    """
    def __init__(self, game, x, y):
        """
        Initialize the ground

        :param game: the game
        :param x: the x position
        :param y: the y position
        """
        super().__init__(x, y,TILESIZE, TILESIZE, GROUND_LAYER,'../assets/img/ground.png', 0, 112,None)
        self.game = game
        if game == None:
            self.groups = []
        else:
            self.groups = self.game.get_all_sprites()
        pygame.sprite.Sprite.__init__(self, self.groups)



