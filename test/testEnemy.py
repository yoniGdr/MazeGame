import unittest

import sys
sys.path.append('../src')
sys.path.append('../src/game')

from enemy import Enemy
from config import *
import pygame


# required to run tests
pygame.init()
pygame.display.set_mode((1,1))

class EnemyTest(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy(0, 0,[])
    def test_get_x(self):
        self.assertEqual(self.enemy.get_x(), 0)

    def test_get_y(self):
        self.assertEqual(self.enemy.get_y(), 0)

    def test_get_width(self):
        self.assertEqual(self.enemy.get_width(), TILESIZE)

    def test_get_height(self):
        self.assertEqual(self.enemy.get_height(), TILESIZE)

    def test_get_layer(self):
        self.assertEqual(self.enemy.get_layer(), ENEMY_LAYER)

    def test_get_image(self):
        self.assertEqual(self.enemy.get_spritesheet().get_imageURL(), '../assets/img/boss.png')

    def change_image(self):
        self.assertEqual(self.enemy.get_spritesheet().get_imageURL(), '../assets/img/boss.png')
        self.enemy.change_image('../assets/img/boss2.png')
        self.assertEqual(self.enemy.get_spritesheet().get_imageURL(), '../assets/img/boss2.png')


if __name__ == '__main__':
    print("gg")
    #  pygame.init()
    #  pygame.display.set_mode((1,1))
    #  tests_running= False
    #  while True:
    #      pygame.display.update()
    #      if not tests_running:
    #          tests_running = True
    unittest.main()
    pygame.quit()

