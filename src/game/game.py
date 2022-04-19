import sys
import pygame
import sys
sys.path.insert(0,'..')
sys.path.insert(1,'maze')
import time
from maze import Maze
from solver import Solver

from block import *
from button import Button
from config import *
from player import Player
from spritesheet import *
from ground import Ground
from enemy import Enemy

import time
import threading



class Game:
    """
    Class game that represent a game
    """
    def __init__(self):
        """
        Constructor of the game
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # fenetre du jeu
        self.titre = pygame.display.set_caption("MAZE - GAME") # titre de la fenetre
        self.clock = pygame.time.Clock() # definir les fps
        self.running = True # etat du jeu complet
        self.font = pygame.font.Font('../assets/img/font.ttf', 80) # police et ca taille ( pour menu )
        self.font2 = pygame.font.Font('../assets/img/font.ttf', 32)
        self.class_maze = Maze(39,24)
        self.class_maze.remove_random_walls(20)
        self.maze = self.class_maze.get_maze()
        self.solver = Solver(self.class_maze)

        self.game_started = False
        self.playing = False # etat de la partie

        self.imagePlayerChoice = ['../assets/img/player.png', '../assets/img/paul.png', '../assets/img/robin.png']
        self.imagePlayerUse = '../assets/img/player.png'

        self.movements = []

        self.intro_background = pygame.image.load('../assets/img/Background.png')
        self.intro_background = pygame.transform.scale(self.intro_background, ( WIDTH, HEIGHT))

        self.intro_j1 = pygame.image.load('../assets/img/player.png')
        self.intro_j1 = pygame.transform.scale(self.intro_j1, (648, 512))

        self.intro_j2 = pygame.image.load('../assets/img/paul.png')
        self.intro_j2 = pygame.transform.scale(self.intro_j2, (188, 260))

        self.intro_j3 = pygame.image.load('../assets/img/robin.png')
        self.intro_j3 = pygame.transform.scale(self.intro_j3, (198, 270))



    def path_to_player(self):
        """
        Path to player, the path between the enemy and the player
        """

        
        start = (int(self.enemy.get_y()/32), int(self.enemy.get_x()/32))
        target = (int(self.player.get_y()/32), int(self.player.get_x()/32))
        if not self.solver.is_cell(start):
            
            if self.solver.is_cell((start[0]+1,start[1])):
                start = (start[0]+1,start[1])
            
            elif self.solver.is_cell((start[0]-1,start[1])):
                start = (start[0]-1,start[1])

            elif self.solver.is_cell((start[0],start[1]+1)):
                start = (start[0],start[1]+1)

            elif self.solver.is_cell((start[0],start[1]-1)):
                start = (start[0],start[1]-1)
            else:
                start = (int(self.enemy.get_y()/32), int(self.enemy.get_x()/32))
        if not self.solver.is_cell(target):
            
            if self.solver.is_cell((target[0]+1,target[1])):
                target = (target[0]+1,target[1])
            
            elif self.solver.is_cell((target[0]-1,target[1])):
                target = (target[0]-1,target[1])

            elif self.solver.is_cell((target[0],target[1]+1)):
                target = (target[0],target[1]+1)

            elif self.solver.is_cell((target[0],target[1]-1)):
                target = (target[0],target[1]-1)
            
            else:
                target = (int(self.player.get_y()/32), int(self.player.get_x()/32))


        self.solver.change_target(start,target)

        self.movements = []

        moves  = self.solver.get_movements()
        nb_moves = len(moves)
        j=0
        while nb_moves > j:
            for _ in range(8):
                self.movements.append(moves[j])
            j+=1




    def createTilemap(self, map):
        """
        Create the tilemap
        
        :param map: the map
        """


        for row_index, row in enumerate(map):
            for col_index, cell in enumerate(row):
                if cell == '0':
                    Block(self, col_index, row_index)

    def get_all_sprites(self):
        """
        Get all the sprites
        
        :return: all the sprites
        """
        return self.all_sprites


    def start_game(self):
        """
        Start the game
        """
        self.playing = True # etat de la partie

        self.all_sprites = pygame.sprite.LayeredUpdates() # group de calques de tout les sprites
        self.blocks = pygame.sprite.LayeredUpdates() # group de calques des blocks
        self.enemies = pygame.sprite.LayeredUpdates()
        # self.dialogue = pygame.sprite.LayeredUpdates()
        # self.attacks = pygame.sprite.LayeredUpdates()
        self.x_start, self.y_start = self.class_maze.get_start()
        self.x_end , self.y_end = self.class_maze.get_end()
        self.player = Player(self.y_start, self.x_start+1, self.all_sprites, self.imagePlayerUse)  # generer un joueur
        self.enemy = Enemy(self.y_start, self.x_start,(self.all_sprites,self.enemies)) #ici le deuxieme sprites) )
        self.player.setBlocks(self.blocks)
        self.enemy.setBlocks(self.blocks)
        self.enemy.set_movements(self.solver.get_movements())
        self.player.setEnemies(self.enemies)
        self.sortie = Ground(self, self.y_end, self.x_end)



        #pygame.draw.rect(self.screen, WHITE, pygame.Rect(30, 30, 60, 60))
        self.createTilemap(self.maze)
        #print(border_map)


        self.game_started = False
        #self.chase_player()

        #self.movements = ["right","down","right","down","right","down","right","down","right"]
        
        moves  = self.solver.get_movements()
        nb_moves = len(moves)
        j=1
        for _ in range(32):
            self.movements.append("down")

        while nb_moves > j:
            for _ in range(16):
                self.movements.append(moves[-j])
            j+=1

        #  self.path_to_player()
        
        for _ in range(128):
            self.movements.append(None)
        
        self.class_maze = Maze(40,23)
        self.class_maze.remove_random_walls(20)
        self.solver = Solver(self.class_maze)
        self.maze = self.class_maze.get_maze()
        #self.enemy.move(movements)

    def player_choice(self, int):
        """
        Player choice, a player can chose between 3 characters

        :param int: the number of the character
        """
        self.imagePlayerUse = self.imagePlayerChoice[int]



    def events(self):
        """
        Events of the game
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if self.player.colision_enemy():
                self.playing = False
                self.game_over('Game Over')

            if self.player.get_y() > self.x_end * 31:
                self.playing = False
                self.game_over('You Win !!!')

            if self.enemy.get_y() > self.x_end * 31 :
                self.playing = False
                self.game_over('Game Over')

        keys = pygame.key.get_pressed()  # récupere les touches actuellement enclencher par le joueur
        if keys[pygame.K_DOWN] or keys[pygame.K_RIGHT]  :
            self.emit_game_started()


    def update(self):
        """
        Update the game and all the sprites in it
        the sprites are updated in the order of their layer.
        A sprite can be a block, a player, an enemy, a dialogue, a button, etc.
        """
        self.all_sprites.update()

        # this is used with path_to_player
        #  if self.game_started :
        #      self.actual = None if len(self.movements) == 0 else self.movements.pop()
        #      self.enemy.move(self.actual)
        #      if(len(self.movements)==0):
        #          self.path_to_player()
        
        if not self.running :
            return
        if self.game_started :
            self.actual = None if len(self.movements) == 0 else self.movements.pop()
            self.enemy.move(self.actual)

    def emit_game_started(self):
        """
        Emit the game started event
        """

        self.game_started = True
        self.player.game_has_started()
        self.enemy.game_has_started()


    def draw(self):
        """
        Draw the game and all the sprites in it
        the sprites are drawn in the order of their layer.
        """
        #self.screen.fill(BLACK)
        self.screen.blit(self.intro_background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS) # vitesse de maj
        pygame.display.update()


    def run(self):
        """
        Run the game by calling the principal methods of the game
        """

        # boucle de jeu
        while self.playing:
            self.events() # evenement
            self.update() # maj
            self.draw() # dessiner
        raise Exception('Game Over')



    def intro_screen(self): #TODO: regler pb de page du menu
        """
        Display the intro screen
        """
        while True:
            mouse_pos = pygame.mouse.get_pos()  # postion de la souris sur l'ecran
            mouse_pressed = pygame.mouse.get_pressed()  # chanque fois que la souris est cliqué, renvoi une liste avec comme premier element le clic gauche

            title = self.font.render('Maze Game', True, OFF_WHITE)
            title_rec = title.get_rect(x=240,y=50)

            play_button = Button(515, 220, 180, 100, WHITE, 'PLAY', 36)
            option_button = Button(460, 350, 280, 100, WHITE, 'OPTIONS', 36)
            quit_button = Button(515, 480, 180, 100, WHITE, 'QUIT', 36)

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rec)

            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(option_button.image, option_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if play_button.is_pressed(mouse_pos, mouse_pressed):
                        self.select_player()

                if quit_button.is_pressed(mouse_pos, mouse_pressed):
                        pygame.quit()
                        sys.exit()

                if option_button.is_pressed(mouse_pos, mouse_pressed):
                        self.options()

            pygame.display.update()


    def select_player(self):
        """
        Display the select player screen,
        this screen is used to choose the look of the player
        """
        while True:
            mouse_pos = pygame.mouse.get_pos()  # postion de la souris sur l'ecran
            mouse_pressed = pygame.mouse.get_pressed()  # chanque fois que la souris est cliqué, renvoi une liste avec comme premier element le clic gauche

            t = self.font.render('Maze Game', True, OFF_WHITE)
            t_rec = t.get_rect(x=240,y=50)

            st = self.font2.render('choose your character', True, TITLE_COLOR2)
            st_rec = t.get_rect(x=255, y=160)

            joueur1_button = Button(320, 360, 140, 90, WHITE, 'YONI', 26)
            joueur2_button = Button(520, 360, 140, 90, WHITE, 'ZAC', 26)
            joueur3_button = Button(720, 360, 140, 90, WHITE, 'JEAN', 26)
            back_button = Button(1040, 730, 140, 90, WHITE, 'Back', 26)

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(self.intro_j1, (355, 280), (51, 0, 62, 62))
            self.screen.blit(self.intro_j2, (550, 280), (57, 0, 62, 62))
            self.screen.blit(self.intro_j3, (750, 280), (57, 0, 62, 62))
            self.screen.blit(t, t_rec)
            self.screen.blit(st, st_rec)

            self.screen.blit(joueur1_button.image, joueur1_button.rect)
            self.screen.blit(joueur2_button.image, joueur2_button.rect)
            self.screen.blit(joueur3_button.image, joueur3_button.rect)
            self.screen.blit(back_button.image, back_button.rect)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if back_button.is_pressed(mouse_pos, mouse_pressed):
                    self.intro_screen()

                if joueur1_button.is_pressed(mouse_pos, mouse_pressed):
                    self.player_choice(0)
                    self.start_game()
                    self.run()


                if joueur2_button.is_pressed(mouse_pos, mouse_pressed):
                    self.player_choice(1)
                    self.start_game()
                    self.run()

                if joueur3_button.is_pressed(mouse_pos, mouse_pressed):
                    self.player_choice(2)
                    self.start_game()
                    self.run()

            pygame.display.update()


    def options(self):
        """
        Display the options screen
        In the options screen, the player can change the volume of the game
        """
        while True:
            mouse_pos = pygame.mouse.get_pos()  # postion de la souris sur l'ecran
            mouse_pressed = pygame.mouse.get_pressed()  # chanque fois que la souris est cliqué, renvoi une liste avec comme premier element le clic gauche

            t = self.font.render('Maze Game', True, OFF_WHITE)
            t_rec = t.get_rect(x=240, y=50)

            st = self.font2.render('Sound', True, TITLE_COLOR2)
            st_rec = t.get_rect(x=540, y=260)

            sound_off_button = Button(430, 360, 140, 90, WHITE, 'OFF', 26)
            sound_on_button = Button(660, 360, 140, 90, WHITE, 'ON', 26)
            back_button = Button(1040, 630, 140, 90, WHITE, 'Back', 26)

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(t, t_rec)
            self.screen.blit(st, st_rec)

            self.screen.blit(sound_off_button.image, sound_off_button.rect)
            self.screen.blit(sound_on_button.image, sound_on_button.rect)

            self.screen.blit(back_button.image, back_button.rect)
            self.clock.tick(FPS)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if back_button.is_pressed(mouse_pos, mouse_pressed):
                    self.intro_screen()


            pygame.display.update()

    def game_over(self,txt):
        """
        Display the game over screen
        this screen is displayed when the player touches the enemy
        """
        while True:

            mouse_pos = pygame.mouse.get_pos()  # postion de la souris sur l'ecran
            mouse_pressed = pygame.mouse.get_pressed()

            text = self.font.render(txt, True, OFF_WHITE)
            text_rec = text.get_rect(x=240, y=60)

            restart_button = Button(470, 330, 280, 100, WHITE, 'Restart', 36)
            quit_button = Button(520, 460, 180, 100, WHITE, 'QUIT', 36)
            menu_button = Button(1024, 630, 140, 90, WHITE, 'Menu', 26)

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(text, text_rec)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            self.screen.blit(menu_button.image, menu_button.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if restart_button.is_pressed(mouse_pos, mouse_pressed):
                    self.start_game()
                    self.run()

                if menu_button.is_pressed(mouse_pos, mouse_pressed):
                    self.intro_screen()

                if quit_button.is_pressed(mouse_pos, mouse_pressed):
                    pygame.quit()
                    sys.exit()


            pygame.display.update()

    
