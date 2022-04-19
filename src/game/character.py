import pygame
import math
import sys
sys.path.insert(0,'..')
from config import *
from spritesheet import *
from element import *

class Character(Element):
    """
    Class that defines a character
    a character is a sprite that can move
    and it can be a player or an enemy
    new types of characters can be added
    by adding a new class that inherits from Character
    """
    def __init__(self, x : int, y : int,width : int ,height : int,layer, imgURL : str ,x_sheet : int ,y_sheet : int , groups : list ,speed : int):
        """
        Constructor of the class

        :param x: x position of the character
        :param y: y position of the character
        :param width: width of the character
        :param height: height of the character
        :param layer: layer of the character
        :param imgURL: url of the image of the character
        :param x_sheet: number of the x position of the sprite sheet
        :param y_sheet: number of the y position of the sprite sheet
        :param groups: groups of the character
        :param speed: speed of the character
        """

        super().__init__(x, y, width,height,layer,imgURL,x_sheet,y_sheet,groups)
        pygame.sprite.Sprite.__init__(self, self.groups)


        self.speed = speed
        self.blocks = None
        self.x_change = 0 # changement direction

        self.game_started = False
        self.y_change = 0


        self.facing= 'down' # par defaut
        self.animation_loop = 1

    def get_position(self, rect):
        """
        Get the position of the character

        :param rect: rect of the character
        :return: x,y position of the character
        """
        persoPos = self.get_rect()
        x_pos = persoPos.x / 30
        y_pos = persoPos.y / 30
        return (x_pos,y_pos)

    def get_position_x(self):
        """
        Get the position x of the character

        :return: x position of the character
        """
        persoPos = self.get_rect()
        x_pos = persoPos.x / 30
        return x_pos

    def get_position_y(self):
        """
        Get the position y of the character

        :return: y position of the character
        """
        persoPos = self.get_rect()
        y_pos = persoPos.y / 30
        return y_pos

    def setBlocks(self,blocks):
        """
        Set the blocks of the character

        :param blocks: blocks of the character
        """
        self.blocks = blocks

    def left(self):
        """
        Move the character to the left
        """
        self.x_change -= self.speed
        self.facing = 'left'

    def right(self):
        """
        Move the character to the right
        """

        self.x_change += self.speed
        self.facing = 'right'

    def up(self):
        """
        Move the character to the up
        """

        self.y_change -= self.speed
        self.facing = 'up'

    def down(self):
        """
        Move the character to the down
        """
        self.y_change += self.speed
        self.facing = 'down'

    def game_has_started(self):
        """
        Set the game has started
        """
        self.game_started = True

    def camera_left(self):
        """
        Move the camera to the left
        """
        #if not self.game_started:
        #    return
        for sprite in self.groups:  # deplace les sprite pour avoir "camera centrale" sur le player
            sprite.rect.x += self.speed

    def camera_right(self):
        """
        Move the camera to the right
        """

        #if not self.game_started:
        #    return
        for sprite in self.groups:  # deplace les sprite pour avoir "camera centrale" sur le player
            sprite.rect.x -= self.speed

    def camera_up(self):
        """
        Move the camera to the up
        """

        #if not self.game_started:
        #    return
        for sprite in self.groups:  # deplace les sprite pour avoir "camera centrale" sur le player
            sprite.rect.y += self.speed

    def camera_down(self):
        """
        Move the camera to the down
        """
        #if not self.game_started:
        #    return
        for sprite in self.groups:  # deplace les sprite pour avoir "camera centrale" sur le player
            sprite.rect.y -= self.speed

    def collision_blocks(self, direction):
        """
        Check if the character collide with a block

        :param direction: direction of the collision
        """
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.blocks, False)  # verifie si le joeur est dans un block
            if hits:
                if self.x_change > 0:  # verifie dans quelle direction
                    self.rect.x = hits[0].rect.left - self.rect.width
                    #if self.get_position_x() < 12:
                    #    self.camera_left()

                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    #if self.get_position_x() > 12:

                     #   self.camera_right()
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    #if self.get_position_y() >= 12:

                    #   self.camera_up()
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    #if self.get_position_y() <= 12:

                     #   self.camera_down()


    def animation(self): #TODO
        """
        Animation of the characte

        methode qui gere les differentes animation du player.
        On charge les 3 images de chaque postion ( LEFT , RIGHT , ... )
        Si le player a la face ( facing ) 'down', si il ne bouge pas on lui donne l'image qui correspond a spn etat down sans mouvement.
        Sinon change l'image de down ( en ajoutant 0.1 a une variable animation_loop et grace a math.floor, nous allons atteindre
        1, 2 ou 3 toute les 10 image cela va changer la boucle d'animation et des qu'elle atteint 3 on la remet a 0
        car il y a que 3 images pour chaque facing.
        On fait de meme pour touts les autre 'facing'
        """
        # translate french docstring to english
        


        down_animations = [self.spritesheet.get_image(0, 0, self.width, self.height),
                           self.spritesheet.get_image(self.width, 0, self.width, self.height),
                           self.spritesheet.get_image(self.width*2, 0, self.width, self.height)]

        up_animations = [self.spritesheet.get_image(0, self.height*3, self.width, self.height),
                         self.spritesheet.get_image(self.width, self.height*3, self.width, self.height),
                         self.spritesheet.get_image(self.width*2, self.height*3, self.width, self.height)]

        left_animations = [self.spritesheet.get_image(0, self.height*2, self.width, self.height),
                           self.spritesheet.get_image(self.width, self.height, self.width, self.height),
                           self.spritesheet.get_image(self.width*2, self.height, self.width, self.height)]

        right_animations = [self.spritesheet.get_image(0, self.height*2, self.width, self.height),
                            self.spritesheet.get_image(self.width, self.height*2, self.width, self.height),
                            self.spritesheet.get_image(self.width*2, self.height*2, self.width, self.height)]

        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.spritesheet.get_image(32, 0, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.spritesheet.get_image(32, self.height*3, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.spritesheet.get_image(32, 64, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.spritesheet.get_image(32, 32, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1


