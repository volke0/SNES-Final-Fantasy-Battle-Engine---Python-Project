import time
#All variables in the game

#Colors
BLACK = (0, 0, 0)
PSEUDO_BLACK = (1, 1, 1)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_GREY = (50, 50, 50)
GREY = (128, 128, 128)
DARK_BLUE = (0, 0, 139)
RED = (255, 0 , 0)
FLUORESCENT_BLUE = (21, 244, 238)
LIGHT_GREEN = (144, 238, 144)
LIGHT_BLUE = (173, 216, 230)
TURQUOISE = (0, 255, 255)
#Poison colors
P_LIGHT_PURPLE = (216, 176, 248) #P_ = poison
P_DARKER_PURPLE = (152, 112, 152)
P_DARKEST_PURPLE = (117, 85, 117)

#Enemy Dead colors
D_LIGHTEST_PURPLE = (247, 0, 247) #D_ = dead
D_LIGHTER_PURPLE = (231, 0, 231)
D_PURPLE = (198, 0, 198)
D_MEDIUM_PURPLE = (181, 0, 181)
D_DARK_PURPLE = (66, 0, 66)

#Screen values
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60

#Character Values
CHARACTER_TILESIZE_1 = 24
CHARACTER_TILESIZE_2 = 36
CHARACTER_TILESIZE_3 = 66

#Battle Variables
MAX_ACTION_VALUE = 70192
MAX_SPECIAL_VALUE = 10

#Palettes
haste_palette = {'p': [RED], 'location': [[0,0]], 'effect': 'glow'}
glenys_poison_palette = {'p': [P_LIGHT_PURPLE, P_DARKER_PURPLE, P_DARKEST_PURPLE, P_DARKEST_PURPLE, P_DARKEST_PURPLE], 'location': [[1,0], [2,0], [3,0], [13,0], [4,1]]}
peachy_poison_palette = {'p': [P_LIGHT_PURPLE, P_DARKER_PURPLE, P_DARKER_PURPLE], 'location': [[1,1], [2,1], [0,1]]}

#Time
last_time = time.time()