import unittest

import sys
sys.path.append('../src')
sys.path.append('../src/game')

from element import Element
from config import *


# required to run tests
import pygame
pygame.init()
pygame.display.set_mode((1,1))

class ElementTest(unittest.TestCase):
    def setUp(self):
        self.element = Element(0, 0, TILESIZE,TILESIZE,ENEMY_LAYER,'../assets/img/boss.png', 12,12, [])
   
    def test_get_x(self):
        self.assertEqual(self.element.get_x(), 0)

    def test_get_y(self):
        self.assertEqual(self.element.get_y(), 0)

    def test_get_width(self):
        self.assertEqual(self.element.get_width(), TILESIZE)

    def test_get_height(self):
        self.assertEqual(self.element.get_height(), TILESIZE)

    def test_get_layer(self):
        self.assertEqual(self.element.get_layer(), ENEMY_LAYER)

    def test_get_image(self):
        self.assertEqual(self.element.get_spritesheet().get_imageURL(), '../assets/img/boss.png')

    def test_change_image(self):
        self.assertEqual(self.element.get_spritesheet().get_imageURL(), '../assets/img/boss.png')
        self.element.change_image('../assets/img/robin.png', 0, 0, TILESIZE, TILESIZE)
        self.assertEqual(self.element.get_spritesheet().get_imageURL(), '../assets/img/robin.png')
        self.assertEqual(self.element.get_width(), TILESIZE)
        self.assertEqual(self.element.get_height(), TILESIZE)



if __name__ == '__main__':
    print("gg")
    unittest.main()
    pygame.quit()

