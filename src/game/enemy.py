import time
from spritesheet import *
from character import Character


class Enemy(Character):
    """
    Class that represent a enemy
     - An enemy is a character that can move and kills the player
       when he touch him
     - An enemy can follws the direction of a given list of movements
     - An enemy moves at a given speed, he is faster than the player
       but he starts moving 3 secondes after the player
    """
    def __init__(self,x : int,y: int, groups : list):
        """
        Constructor of the class

        :param x: x position of the enemy
        :param y: y position of the enemy
        :param groups: groups of the enemy
        """
        super().__init__(x , y ,TILESIZE,TILESIZE, ENEMY_LAYER,'../assets/img/boss.png',0,0,groups,ENEMY_SPEED)
        self.moving = None
        self.steps = 0
        self.movements = [None]
        self.can_move = False

    def update(self):
        """
        Update the state of the enemy :
        - move the enemy
        - changes the image of the enemy
        - changes the direction of the enemy by calling the movement method
        
        if the game is not paused, the enemy moves otherwise he stays in the same position
        """
        if not self.game_started:
            return
        if self.moving != None:
            self.movement()

        self.animation()
        self.rect.x += self.x_change
        self.collision_blocks('x')
        self.rect.y += self.y_change
        self.collision_blocks('y')

        self.x_change = 0
        self.y_change = 0

    def set_movements(self,movements):
        """
        Set the movements of the enemy

        :param movements: movements of the enemy
        """
        self.movements = movements
        self.movements.insert(0,None)
        self.can_move = True

    def movement(self): #TODO 
        """
        Move the enemy
        the moves at a given speed every time that this method is called
        when the enemy has no more movements, he stops bu setting the moving variable to None
        """
        '''
        Permet de gerer les mouvement du jouer en récupérant les touche.
        en fonction de la touche : - on deplace les sprite vers une direction pour avoir une camera central
        sur le player ( le joueur se deplace dans une direction et les sprites dans l'autre )
        - on deplace sur l'axe en changant notre x_change ou y_change et on donne un 'etat' ( facing )
        '''
        if not self.can_move:
            return

        if self.steps > 0:
            self.move(self.moving)
            self.steps -= 1
        else :
            self.moving = self.movements.pop()
            if(self.moving == None):
                self.can_move = False
                return

            if self.moving != None:
                self.steps = 32
            else:
                self.can_move = False


    def move(self,move):
        """
        Move the enemy

        :param move: direction of the enemy
        """
        if move == "left":
            self.left()
        elif move == "right":
            self.right()
        elif move == "up":
            self.up()
        elif move == "down":
            self.down()
        elif move == None:
            return
        else:
            raise Exception("Enter a valid movement")

    def collision_blocks(self, direction):
        """
        Collision with the blocks

        :param direction: direction of the collision
        """

        '''Methode qui permet de gerer les collisions.
        On regarde sur quelle axe on se deplace puis dans quelle direction puis nous definisons notre
        rect pour qu'il ne puisse pas aller sur un block
        :param direction: directions dans lasquele nous nous dirigons
        :return:
        '''
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.blocks, False)  # verifie si le joeur est dans un block
            if hits:
                if self.x_change > 0:  # verifie dans quelle direction
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

