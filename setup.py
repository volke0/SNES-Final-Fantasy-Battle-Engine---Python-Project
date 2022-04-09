import pygame as pg 
import os
import utils
from vars import *

pg.mixer.pre_init(44100, -16, 2, 512)
PYGAME_BLEND_ALPHA_SDL2 = 1
pg.init()
pg.mixer.init()
pg.mixer.set_num_channels(64)

screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption('Prototype RPG')
clock = pg.time.Clock()
#print(f'{len(player_list[0].player_inventory) - 1}')

#Graphics
ITEM_GFX = utils.load_all_gfx(os.path.join('resources', 'graphics', 'items'))
PC_GFX = utils.load_all_gfx(os.path.join('resources', 'graphics', 'playable_characters'))
BG_GFX = utils.load_all_gfx(os.path.join('resources', 'graphics', 'backgrounds'))
WP_GFX = utils.load_all_gfx(os.path.join('resources', 'graphics', 'items'))
EN_GFX = utils.load_all_gfx(os.path.join('resources', 'graphics', 'enemies'))
UI_GFX = utils.load_all_gfx(os.path.join('resources', 'graphics', 'ui'))
SFX_GFX = utils.load_all_gfx(os.path.join('resources', 'graphics', 'sfx'))
BUFF_GFX = utils.load_all_gfx(os.path.join('resources', 'graphics', 'buffs'))

#Weapon Special Effect Dictionaries
weapon_dict = utils.create_weapon_dict('weapons', WP_GFX, 16, 11, scale=2)
sword_hit_dict = utils.create_sfx_gfx_dict('sword_hit_effect', SFX_GFX, 45, 66, 1, 8, 2)
dagger_hit_dict = utils.create_sfx_gfx_dict('dagger_hit_effect', SFX_GFX, 45, 67, 1, 6, 2)
sword_swing_dict = utils.create_sfx_gfx_dict('sword_swing_effect', SFX_GFX, 34, 38, 1, 3, 2)

#Magic Effect Dictionaries
fire_dict = utils.create_sfx_gfx_dict('fire', SFX_GFX, 48, 48, 1, 3, 2)
snow_storm_dict = utils.create_sfx_gfx_dict('snow_storm', SFX_GFX, 242, 162, 11, 4, 2)
bolting_dict = utils.create_sfx_gfx_dict('bolting', SFX_GFX, 242, 162, 4, 5, 2)
bliz_dict, flip_bliz_dict = utils.create_single_images_animation(os.path.join('resources', 'graphics', 'sfx', 'blizzaga'), 3, colorkey=TURQUOISE)
cure_dict = utils.create_single_images_animation(os.path.join('resources', 'graphics', 'sfx', 'cure'), 3)
haste_dict = utils.create_single_images_animation(os.path.join('resources', 'graphics', 'sfx', 'haste'), 3)
bio_dict = utils.create_single_images_animation(os.path.join('resources', 'graphics', 'sfx', 'bio'), 3)
barrier_dict = utils.create_single_images_animation(os.path.join('resources', 'graphics', 'sfx', 'barrier'), 3)
restore_dict = utils.create_single_images_animation(os.path.join('resources', 'graphics', 'sfx', 'restore'), 3)

#Skill Effects
resolve_dict = utils.create_single_images_animation(os.path.join('resources', 'graphics', 'sfx', 'skills', 'resolve'), 3)

#Buff Effects
poison_dict = utils.create_single_images_animation(os.path.join('resources', 'graphics', 'sfx', 'poison'), 2)

#Special Effect Dictionaries
shock_dict = utils.create_single_images_animation(os.path.join('resources', 'graphics', 'sfx', 'shock'), 3)


#Item Special Effect Dictionaries
magic_use_dict = utils.create_sfx_gfx_dict('magic_use', SFX_GFX, 46, 46, 1, 11, 3)
heal_use_dict = utils.create_single_images_animation(os.path.join('resources', 'graphics', 'sfx', 'heal_use'), 3)
bolting_dict = utils.create_sfx_gfx_dict('bolting', SFX_GFX, 242, 162, 6, 4, 4)
potion_dict = utils.create_sfx_gfx_dict('potion', SFX_GFX, 42, 56, 1, 14, 2)
ether_dict = utils.create_sfx_gfx_dict('ether', SFX_GFX, 42, 56, 1, 14, 2)
revive_dict = utils.create_sfx_gfx_dict('phoenix_down', SFX_GFX, 33, 24, 1, 6, 3)

#UI Special Effect Dictionaries
pointer_dict = utils.create_sfx_gfx_dict('active_pointer', UI_GFX, 17, 10, 1, 3, 3)

#Sounds
SFX = utils.load_all_sfx(os.path.join('resources', 'sound'))
MUSIC = utils.load_all_music(os.path.join('resources', 'music'))
