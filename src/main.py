import pygame
import sys
sys.path.append('game')
from game import Game


if __name__== "__main__":
    g = Game()
    g.intro_screen()
    g.start_game()
    try:
        g.run()
    except Exception:
        g.game_over()

    pygame.quit()

