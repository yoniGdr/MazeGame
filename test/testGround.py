import unittest

import sys
sys.path.append('../src')
sys.path.append('../src/game')

from ground import Ground
from config import *
import pygame


# required to run tests
pygame.init()
pygame.display.set_mode((1,1))

class GroundTest(unittest.TestCase):
    def setUp(self):
        self.ground = Ground(None, 0, 0)
    def test_get_x(self):
        self.assertEqual(self.ground.get_x(), 0)

    def test_get_y(self):
        self.assertEqual(self.ground.get_y(), 0)

    def test_get_width(self):
        self.assertEqual(self.ground.get_width(), TILESIZE)

    def test_get_height(self):
        self.assertEqual(self.ground.get_height(), TILESIZE)

    def test_get_layer(self):
        self.assertEqual(self.ground.get_layer(), GROUND_LAYER)

    def test_get_image(self):
        self.assertEqual(self.ground.get_spritesheet().get_imageURL(), '../assets/img/ground.png')

    def test_change_image(self):
        self.assertEqual(self.ground.get_spritesheet().get_imageURL(), '../assets/img/ground.png')
        self.ground.change_image('../assets/img/boss.png', 0 ,0 , TILESIZE, TILESIZE)
        self.assertEqual(self.ground.get_spritesheet().get_imageURL(), '../assets/img/boss.png')
        self.assertEqual(self.ground.get_height(), TILESIZE)
        self.assertEqual(self.ground.get_width(), TILESIZE)


if __name__ == '__main__':

    unittest.main()
    pygame.quit()
