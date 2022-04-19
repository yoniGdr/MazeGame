import unittest

import sys
sys.path.append('../src')
sys.path.append('../src/game')
sys.path.append('../src/maze')

from player import Player
from config import *

# required to run tests
import pygame
pygame.init()
pygame.display.set_mode((1,1))

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player(0, 3,[],'../assets/img/player.png')
    def test_get_x(self):
        self.assertEqual(self.player.get_x(), 0 * TILESIZE  )

    def test_get_y(self):
        self.assertEqual(self.player.get_y(), 3 * TILESIZE)

    def test_get_width(self):
        self.assertEqual(self.player.get_width(), TILESIZE)

    def test_get_height(self):
        self.assertEqual(self.player.get_height(), TILESIZE)

    def test_get_layer(self):
        self.assertEqual(self.player.get_layer(), PLAYER_LAYER)

    def test_get_image(self):
        self.assertEqual(self.player.get_spritesheet().get_imageURL(), '../assets/img/player.png')

    def test_change_image(self):
        self.assertEqual(self.player.get_spritesheet().get_imageURL(), '../assets/img/player.png')
        self.player.change_image('../assets/img/paul.png' ,0 ,0 ,TILESIZE ,TILESIZE)
        self.assertEqual(self.player.get_spritesheet().get_imageURL(), '../assets/img/paul.png')
        self.assertEqual(self.player.get_width(), TILESIZE)
        self.assertEqual(self.player.get_height(), TILESIZE)

    def test_get_pos(self):
        self.assertEqual(self.player.get_x()/32, 0)
        self.assertEqual(self.player.get_y()/32, 3)



if __name__ == '__main__':
    print("gg")

    unittest.main()
    pygame.quit()
