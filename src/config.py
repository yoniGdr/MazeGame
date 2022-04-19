import sys

### DIMENSION SCREEN ###
WIDTH = 1280
HEIGHT = 780

### CONFIG ###
PLAYER_SPEED = 2.5
ENEMY_SPEED = 2
FPS = 60
TILESIZE = 32

### COULEURS ###
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOUTON_COLOR = (92, 65, 76)
OFF_WHITE = (238, 235, 207)
TITLE_COLOR2 = (255, 195, 0)

### NIVEAU DE COUCHE ###
DIALOG_LAYER = 5
PLAYER_LAYER = 4
ENEMY_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

### TEST ### ( inutile pour le moment )
border_map = [

    '000000000000000000000000000000',
    '0............B..B..B.........0',
    '0............B..B..B.........0',
    '0BBBBBBB..B..B..B..B..BBBBB..0',
    '0.........B..B........B...B..0',
    '0.........B..B........B...B..0',
    '000000000000000000000000000000',
    'B.........B.....B.........B..B',
    'B.........B.....B.........B..B',
    'BBBBBBBB..B..B.....BBBBB..B..B',
    'B......B..B..B.....B.........B',
    'B......B..B..BBBB..B.........B',
    'B......BBBBBBB..B..B..BBBBB..B',
    'B............B..B.....B......B',
    'B............B..B.....B......B',
    'B............B..BBBBBBB......B',
    'B............................B',
    'B............................B',
    'B............................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',

]
### LYBYRINTHE ALEATOIRE ###


## equivalent de setinterval() en javascript
import threading
running = True

def restart_interval():
    running = True

def stop_interval():
    running = False

def set_interval(func, sec):
    if not running:
        return
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
