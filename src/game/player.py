import pygame
import sys
sys.path.insert(0,'..')
from config import *
from character import Character
#  from spritesheet import *

class Player(Character):
    """
    Class that represents the player :
    - the player is a sprite
    - the player is a character
    - the player can be controlled by the keyboard
    """


    def __init__(self, x : int,y : int  , groups: list, img):
        """
        Constructor of the player

        :param x: x position of the player
        :param y: y position of the player
        :param groups: groups of the player
        :param img: image of the player
        """
        super().__init__(x , y ,TILESIZE,TILESIZE,PLAYER_LAYER,img,0,0, groups,PLAYER_SPEED)

        '''Genere le joueur et le place en fonction des coordonner
        :param game: le game actuel ( permet d'utiliser les methode de Game)
        :param x: coordonner x du player
        :param y: coordonner y du player
        '''

        self.enemies = None

    def update(self):
        """
        Update the player

        """
        if not self.game_started:
            return
        '''Permet de mettre a jour automatiquement les sprites du joueur
        Quand le joueur change de direction on appelle la methode collision blocks
        pour faire les collisions si necessaire
        '''
        self.movement()
        self.animation()
        self.colision_enemy()
        self.rect.x += self.x_change
        self.collision_blocks('x')
        self.rect.y += self.y_change
        self.collision_blocks('y')

        self.x_change = 0
        self.y_change = 0


    def movement(self): 
        """
        Handle the player movement
        by checking the keyboard input
        """

        '''Permet de gerer les mouvement du jouer en récupérant les touche.
        en fonction de la touche : - on deplace les sprite vers une direction pour avoir une camera central
        sur le player ( le joueur se deplace dans une direction et les sprites dans l'autre )
        - on deplace sur l'axe en changant notre x_change ou y_change et on donne un 'etat' ( facing )
        '''
        keys = pygame.key.get_pressed() # récupere les touches actuellement enclencher par le joueur
        if keys[pygame.K_LEFT]:
            #if self.get_position_x() < 12 :
                #self.camera_left()
                #self.count_y -= 1
            self.left()
        if keys[pygame.K_RIGHT]:
            #if self.get_position_x() > 12 :
                #self.camera_right()
               # self.count_y += 1
            self.right()
        if keys[pygame.K_UP]:
            #if  self.get_position_y() <= 10:
                #self.camera_up()
               # self.count_x += 1
            self.up()
        if keys[pygame.K_DOWN]:
            #if self.get_position_y() >= 10:
              #  self.camera_down()
           #     self.count_x -= 1
            self.down()


    def setEnemies(self, enemies):
        """
        Set the enemies of the player

        :param enemies: enemies of the player
        """
        self.enemies = enemies


    
    """ 
    def collision_blocks(self, direction):
        '''Methode qui permet de gerer les collisions.
        On regarde sur quelle axe on se deplace puis dans quelle direction puis nous definisons notre
        rect pour qu'il ne puisse pas aller sur un block
        :param direction: directions dans lasquele nous nous dirigons
        :return:
        '''
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.blocks, False) # verifie si le joeur est dans un block
            if hits:
                if self.x_change > 0: # verifie dans quelle direction
                    self.rect.x = hits[0].rect.left - self.rect.width
                    self.camera_left()
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    self.camera_right()
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    self.camera_up()
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    self.camera_down()
    """
    def colision_enemy(self): 
        """
        Check if the player colide with an enemy
        """
        hits = pygame.sprite.spritecollide(self, self.enemies, False)
        if hits:
            self.kill()
            return True
        return False


