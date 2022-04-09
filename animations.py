import pygame as pg 
import setup, utils, engines
from vars import *

def make_weapon_animation(character):
    weapon_animation = None
    if character.weapon != None:
        weapon_animation = setup.weapon_dict[character.weapon]
        temp_img = pg.transform.flip(weapon_animation[0], True, False)
        temp_img.set_colorkey(BLACK)
        temp_img.convert_alpha()
        weapon_animation.append(temp_img)
    else:
        pass
    return weapon_animation

def make_cursor_animation():
    cursor_animation = []
    cursor_animation.append(setup.UI_GFX['smallarrow'])
    temp_img_0 = pg.transform.flip(cursor_animation[0], True, False)
    temp_img_0.set_colorkey(BLACK)
    temp_img_0.convert_alpha()
    cursor_animation.append(temp_img_0)
    return cursor_animation

def make_colored_background(color):
    background = pg.Surface(SCREEN_SIZE)
    background.set_alpha(255)
    background.fill(color)
    return background

#Player Animations
def player_stand(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 1, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 3, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},]

    engine = engines.BattleAnimationSystem(script)
    return engine

def player_magic_wait(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 4, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 3, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 7, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 3, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 10, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 3, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},]

    engine = engines.BattleAnimationSystem(script, repeat=True)
    return engine

def player_melee_wait(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 4, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 3, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},]

    engine = engines.BattleAnimationSystem(script, repeat=True)
    return engine

def player_attack_melee(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 5, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 5, 'frame': 0, 'x': -13, 'y': -13, 'speed_x': -4, 'speed_y': -4, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 5, 'frame': 1, 'x': -25, 'y': -25, 'speed_x': -4, 'speed_y': -4, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 5, 'frame': 1, 'x': -29, 'y': -24, 'speed_x': -4, 'speed_y': 4, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 5, 'frame': 2, 'x': -50, 'y': 0, 'speed_x': -4, 'speed_y': 4, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0, },]

    engine = engines.BattleAnimationSystem(script)
    return engine

def player_walk_back(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 3, 'frame': None, 'x': 0, 'y': 0, 'speed_x': 5, 'speed_y': 0, 'fps': 3, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 1, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0, 'fixed_location': True}]

    engine = engines.BattleAnimationSystem(script)
    return engine

def player_hit(character):
    x = 1
    speed_x = 2
    script = [{'mode': 'unit', 'fast_rumble': True},
              {'character': character, 'action': 13, 'frame': 0, 'x': x, 'y': 0, 'speed_x': speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 13, 'frame': 0, 'x': -x, 'y': 0, 'speed_x': -speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 13, 'frame': 0, 'x': x, 'y': 0, 'speed_x': speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 13, 'frame': 0, 'x': -x, 'y': 0, 'speed_x': -speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 13, 'frame': 0, 'x': x, 'y': 0, 'speed_x': speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 13, 'frame': 0, 'x': -x, 'y': 0, 'speed_x': -speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 13, 'frame': 0, 'x': x, 'y': 0, 'speed_x': speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 13, 'frame': 0, 'x': -x, 'y': 0, 'speed_x': -speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 13, 'frame': 0, 'x': x, 'y': 0, 'speed_x': speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 13, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0, 'fixed_location': True}]

    engine = engines.BattleAnimationSystem(script)
    return engine

def player_low_hp(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 9, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 60, 'alpha': 255},
              {'character': character, 'action': 12, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 5, 'alpha': 255},
              {'character': character, 'action': 15, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 3, 'alpha': 255},]

    engine = engines.BattleAnimationSystem(script, repeat=True)
    return engine

def player_dead(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 18, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 3, 'alpha': 255},]

    engine = engines.BattleAnimationSystem(script)
    return engine

def player_victory_dance(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 3, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 8, 'alpha': 255, 'no_repeat': True},
              {'character': character, 'action': 6, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 8, 'alpha': 255},
              {'character': character, 'action': 6, 'frame': 1, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 8, 'alpha': 255},
              {'character': character, 'action': 6, 'frame': 2, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 8, 'alpha': 255},]

    engine = engines.BattleAnimationSystem(script, repeat=True)
    return engine

def player_enter_battle(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 6, 'frame': 0, 'x': 230, 'y': -230, 'speed_x': 0, 'speed_y': 0, 'fps': 3, 'alpha': 255, 'fixed_location': True},
              {'character': character, 'action': 6, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': -20, 'speed_y': 20, 'fps': 3, 'alpha': 255, 'fixed_location': False},
              {'character': character, 'action': 9, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 10, 'alpha': 255, 'fixed_location': True},
              {'character': character, 'action': 1, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 15, 'alpha': 255, 'fixed_location': False},]

    engine = engines.BattleAnimationSystem(script)
    return engine

def player_walk_up(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 21, 'frame': None, 'x': -85, 'y': 0, 'speed_x': -5, 'speed_y': 0, 'fps': 3, 'alpha': 255},]

    engine = engines.BattleAnimationSystem(script)
    return engine

def player_use_item(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 14, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 15, 'alpha': 255, 'sfx': setup.SFX['ting']},
              {'character': character, 'action': 14, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 10, 'alpha': 255},]

    engine = engines.BattleAnimationSystem(script)
    return engine

def player_use_magic(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 14, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 50, 'alpha': 255},
              {'character': character, 'action': 1, 'frame': 0, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 10, 'alpha': 255},]

    engine = engines.BattleAnimationSystem(script)
    return engine

# Enemy Animations
def enemy_hit(character):
    x = 1
    speed_x = 2
    script = [{'mode': 'unit', 'fast_rumble': True, 'enemy_mode': True},
              {'character': character, 'action': 0, 'frame': None, 'x': x, 'y': 0, 'speed_x': speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': -x, 'y': 0, 'speed_x': -speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': x, 'y': 0, 'speed_x': speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': -x, 'y': 0, 'speed_x': -speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': x, 'y': 0, 'speed_x': speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': -x, 'y': 0, 'speed_x': -speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': x, 'y': 0, 'speed_x': speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': -x, 'y': 0, 'speed_x': -speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': x, 'y': 0, 'speed_x': speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': -x, 'y': 0, 'speed_x': -speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': x, 'y': 0, 'speed_x': speed_x, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': 0, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0, 'fixed_location': True}]

    engine = engines.BattleAnimationSystem(script)
    return engine

def enemy_attack(character):
    script = [{'mode': 'unit', 'enemy_mode': True},
              {'character': character, 'action': 2, 'frame': None, 'x': 0, 'y': 0, 'fps': 2, 'speed_x': 0, 'speed_y': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': 0, 'y': 0, 'fps': 2, 'speed_x': 0, 'speed_y': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 2, 'frame': None, 'x': 0, 'y': 0, 'fps': 2, 'speed_x': 0, 'speed_y': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': 0, 'y': 0, 'fps': 2, 'speed_x': 0, 'speed_y': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 2, 'frame': None, 'x': 0, 'y': 0, 'fps': 2, 'speed_x': 0, 'speed_y': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},
              {'character': character, 'action': 0, 'frame': None, 'x': 0, 'y': 0, 'fps': 2, 'speed_x': 0, 'speed_y': 0, 'alpha': 255, 'flag_1': None, 'alpha_pts': 0},]

    engine = engines.BattleAnimationSystem(script)
    return engine

def enemy_dead(character):
    script = [{'mode': 'unit', 'enemy_mode': True},
              {'character': character, 'action': 0, 'frame': None, 'x': 0, 'y': 0, 'fps': -8, 'mask': character.animation[1], 'm_alpha': 190, 'm_fps': -3, 'sfx': setup.SFX['enemy_killed'], 'speed_x': 0, 'speed_y': 0, 'alpha': 255, 'flag_1': True, 'alpha_pts': 0},
             ]

    engine = engines.BattleAnimationSystem(script)
    return engine

def enemy_enter_battle(character):
    script = [{'mode': 'unit', 'enemy_mode': True},
              {'character': character, 'action': 0, 'frame': None, 'x': -400, 'y': 0, 'fps': 15, 'speed_x': 0, 'speed_y': 0, 'alpha': 255, 'fixed_location': True},
              {'character': character, 'action': 0, 'frame': None, 'x': 0, 'y': 0, 'fps': 10, 'speed_x': 40, 'speed_y': 0, 'alpha': 255, 'fixed_location': False},
              {'character': character, 'action': 0, 'frame': None, 'x': 0, 'y': 0, 'fps': 10, 'speed_x': 0, 'speed_y': 0, 'alpha': 255, 'fixed_location': True},
             ]

    engine = engines.BattleAnimationSystem(script)
    return engine

#UI Animations
def pointer(character):
    animation = setup.pointer_dict['1']
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': 25, 'y': -5, 'fps': 15, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 25, 'y': -5, 'fps': 15, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 2, 'x': 25, 'y': -5, 'fps': 15, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              ]

    engine = engines.BattleAnimationSystem(script, repeat=True)
    return engine

def cursor(mode):
    animation = make_cursor_animation()
    engine = engines.CursorSystem(animation, mode)
    return engine

def bounce_text(text, character, color=WHITE, sfx_on=False, size=24):
    sfx = None
    if sfx_on == True:
        sfx = setup.SFX['healing_sound1']
    else:
        sfx = None

    text_1, rect, drop_text = utils.storeText(str(text), color=color)
    animation = []
    animation.append(text_1)
    center = False

    if rect.width >= 60:
        x = rect.width / 3.5
    elif rect.width >= 30 and rect.width <= 49:
        x = rect.width / 1.2
    elif rect.width >= 50 and rect.width <= 59:
        x = rect.width / 2
    else:
        x = rect.width * 1.5

    #Dropset values
    drop_offset = 1 + (size // 15)
    drop_animation = drop_text
    drop_x = x + drop_offset

    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': x, 'y': -50, 'fps': 2, 'sfx': sfx, 'alpha': 255, 'animation_2': drop_animation, 'animation_2_unique': True, 'x_2': drop_x, 'y_2': -50 + drop_offset, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'rect_center': center},
              {'frame': 0, 'x': x, 'y': -25, 'fps': 1, 'sfx': None, 'alpha': 255, 'x_2': drop_x, 'y_2': -25 + drop_offset,  'center_on_screen': False, 'on_character': True, 'on_target': False, 'rect_center': center},
              {'frame': 0, 'x': x, 'y': 0, 'fps': 1, 'sfx': None, 'alpha': 255, 'x_2': drop_x, 'y_2': 0 + drop_offset,  'center_on_screen': False, 'on_character': True, 'on_target': False, 'rect_center': center},
              {'frame': 0, 'x': x, 'y': 90, 'fps': 1, 'sfx': None, 'alpha': 255, 'x_2': drop_x, 'y_2': 90 + drop_offset,  'center_on_screen': False, 'on_character': True, 'on_target': False, 'rect_center': center},
              {'frame': 0, 'x': x, 'y': 30, 'fps': 1, 'sfx': None, 'alpha': 255, 'x_2': drop_x, 'y_2': 30 + drop_offset,  'center_on_screen': False, 'on_character': True, 'on_target': False, 'rect_center': center},
              {'frame': 0, 'x': x, 'y': 90, 'fps': 1, 'sfx': None, 'alpha': 255, 'x_2': drop_x, 'y_2': 90 + drop_offset,  'center_on_screen': False, 'on_character': True, 'on_target': False, 'rect_center': center},
              {'frame': 0, 'x': x, 'y': 50, 'fps': 1, 'sfx': None, 'alpha': 255, 'x_2': drop_x, 'y_2': 50 + drop_offset,  'center_on_screen': False, 'on_character': True, 'on_target': False, 'rect_center': center},
              {'frame': 0, 'x': x, 'y': 90, 'fps': 1, 'sfx': None, 'alpha': 255, 'x_2': drop_x, 'y_2': 90 + drop_offset,  'center_on_screen': False, 'on_character': True, 'on_target': False, 'rect_center': center},
              {'frame': 0, 'x': x, 'y': 80, 'fps': 1, 'sfx': None, 'alpha': 255, 'x_2': drop_x, 'y_2': 80 + drop_offset,  'center_on_screen': False, 'on_character': True, 'on_target': False, 'rect_center': center},
              {'frame': 0, 'x': x, 'y': 90, 'fps': 15, 'sfx': None, 'alpha': 255, 'x_2': drop_x, 'y_2': 90 + drop_offset,  'center_on_screen': False, 'on_character': True, 'on_target': False, 'rect_center': center},
              ]

    engine = engines.BattleAnimationSystem(script, repeat=False)
    return engine

#SFX Animations
def weapon_swing(character):
    animation = make_weapon_animation(character)
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': 12, 'y': 0, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 13, 'y': 0, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 2, 'x': 13, 'y': -43, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 3, 'x': -39, 'y': -20, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 4, 'x': -39, 'y': 0, 'fps': 3, 'sfx': setup.SFX['sword_slash2'], 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},]

    engine = engines.BattleAnimationSystem(script)
    return engine

def weapon_swing_miss(character):
    animation = make_weapon_animation(character)
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': 12, 'y': 0, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 13, 'y': 0, 'fps': 5, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 2, 'x': 13, 'y': -43, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 3, 'x': -39, 'y': -20, 'fps': 5, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': None, 'x': -39, 'y': 0, 'fps': 3, 'sfx': setup.SFX['sword_slash1'], 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': None, 'x': -39, 'y': 0, 'fps': 20, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},]

    engine = engines.BattleAnimationSystem(script)
    return engine

#Magic Animations
def magic_use(character):
    animation = setup.magic_use_dict['1']
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': None, 'x': -25, 'y': -11, 'fps': 10, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': -25, 'y': -11, 'fps': 1, 'sfx': setup.SFX['blackmagic'], 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 1, 'x': -25, 'y': -11, 'fps': 1, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 2, 'x': -25, 'y': -11, 'fps': 1, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -25, 'y': -11, 'fps': 1, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -25, 'y': -11, 'fps': 1, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 5, 'x': -25, 'y': -11, 'fps': 1, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 6, 'x': -25, 'y': -11, 'fps': 1, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 7, 'x': -25, 'y': -11, 'fps': 1, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 8, 'x': -25, 'y': -11, 'fps': 1, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 9, 'x': -25, 'y': -11, 'fps': 1, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 10, 'x': -25, 'y': -11, 'fps': 1, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': -25, 'y': -11, 'fps': 30, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False},]

    engine = engines.BattleAnimationSystem(script)
    return engine

def heal_use(character):
    animation = setup.heal_use_dict[0]
    x = 117
    y = 60
    fps = 1
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': None, 'x': -x, 'y': -y, 'fps': 1, 'sfx': setup.SFX['white_magic'], 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 1, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 2, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 5, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 6, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 7, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 8, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 9, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False,},
              {'frame': 10, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 13, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 14, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 15, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': None, 'x': -x, 'y': -y, 'fps': 15, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False},]

    engine = engines.BattleAnimationSystem(script, repeat=False)
    return engine

def cure(character):
    animation = setup.cure_dict[0]
    x = 125
    y = 80
    fps = 1
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None, 'semi_goal': 25},
              {'frame': None, 'x': -x, 'y': -y, 'fps': 4, 'sfx': setup.SFX['healing_sound2'], 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 1, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 2, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 5, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 6, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 7, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 8, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 9, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False,},
              {'frame': 10, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 13, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 14, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 15, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': None, 'x': -x, 'y': -y, 'fps': 4, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 16, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 17, 'x': -x, 'y': -y, 'fps': fps, 'sfx': setup.SFX['healing_sound1'], 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 18, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 19, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 20, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 21, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 22, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 23, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 24, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': 25, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, },
              {'frame': None, 'x': -x, 'y': -y, 'fps': 5, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False},]

    engine = engines.BattleAnimationSystem(script, repeat=False)
    return engine

def fire(character):
    animation = setup.fire_dict['1']
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 2, 'x': 80, 'y': 5, 'fps': 3, 'sfx': setup.SFX['fire_1'], 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 0, 'x': 75, 'y': 5, 'fps': 3, 'frame_2': None, 'x_2': 60, 'y_2': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 0, 'x': 75, 'y': 5, 'fps': 3, 'frame_2': 2, 'x_2': 44, 'y_2': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 1, 'x': 75, 'y': 5, 'fps': 3, 'frame_2': 2, 'x_2': 44, 'y_2': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 1, 'x': 75, 'y': 5, 'fps': 3, 'frame_2': 0, 'x_2': 18, 'y_2': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 2, 'x': 58, 'y': 5, 'fps': 3, 'frame_2': 0, 'x_2': 18, 'y_2': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 2, 'x': 58, 'y': 5, 'fps': 3, 'frame_2': 0, 'x_2': 18, 'y_2': 5, 'frame_3': 2, 'x_3': -10, 'y_3': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 2, 'x': 58, 'y': 5, 'fps': 3, 'frame_2': 1, 'x_2': 24, 'y_2': 5, 'frame_3': 2, 'x_3': -10, 'y_3': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': 58, 'y': 5, 'fps': 3, 'frame_2': 1, 'x_2': 24, 'y_2': 5, 'frame_3': 2, 'x_3': -10, 'y_3': 5, 'sfx': setup.SFX['fire_1'], 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': 58, 'y': 5, 'fps': 3, 'frame_2': 1, 'x_2': 24, 'y_2': 5, 'frame_3': 0, 'x_3': -32, 'y_3': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': 58, 'y': 5, 'fps': 3, 'frame_2': 2, 'x_2': 7, 'y_2': 5, 'frame_3': 0, 'x_3': -32, 'y_3': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': 58, 'y': 5, 'fps': 3, 'frame_2': 2, 'x_2': 7, 'y_2': 5, 'frame_3': 1, 'x_3': -31, 'y_3': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': 58, 'y': 5, 'fps': 3, 'frame_2': None, 'x_2': 7, 'y_2': 5, 'frame_3': 1, 'x_3': -31, 'y_3': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': 58, 'y': 5, 'fps': 3, 'frame_2': None, 'x_2': 7, 'y_2': 5, 'frame_3': 2, 'x_3': -31, 'y_3': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': 58, 'y': 5, 'fps': 37, 'frame_2': None, 'x_2': 7, 'y_2': 5, 'frame_3': None, 'x_3': -31, 'y_3': 5, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},]

    engine = engines.BattleAnimationSystem(script)
    return engine

def snow_storm(character):
    animation = setup.snow_storm_dict['1']
    alpha = 255
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': -135, 'y': -100, 'fps': 3, 'sfx': setup.SFX['snow_wind'], 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 1, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 2, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 5, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 6, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 7, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 8, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 9, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 10, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 11, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 12, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 13, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 14, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 15, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 16, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 17, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 18, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 19, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 21, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 22, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 23, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 24, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 25, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 26, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 27, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 28, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': alpha, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': -135, 'y': -100, 'fps': 1, 'sfx': None, 'alpha': alpha, 'on_character': True, 'animation_2': flash_white_background(), 'play_animation': True},
              {'frame': 30, 'x': -135, 'y': -100, 'fps': 1, 'sfx': None, 'alpha': 255, 'on_character': True,'no_reset_animation_2': True},
              {'frame': 31, 'x': -135, 'y': -100, 'fps': 1, 'sfx': None, 'alpha': 255, 'on_character': True,},
              {'frame': 32, 'x': -135, 'y': -100, 'fps': 1, 'sfx': setup.SFX['snow_ice_hit'], 'alpha': 255, 'on_character': True,},
              {'frame': 33, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 255, 'on_character': True,},
              {'frame': 34, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 255, 'on_character': True,},
              {'frame': 35, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 255, 'on_character': True,},
              {'frame': 36, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 255, 'on_character': True,},
              {'frame': 37, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 255, 'on_character': True,},
              {'frame': 38, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 255, 'on_character': True,},
              {'frame': 39, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 255, 'on_character': True,},
              {'frame': 41, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 255, 'on_character': True,},
              {'frame': 42, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 255, 'on_character': True,},
              {'frame': 43, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 255, 'on_character': True,},
              {'frame': None, 'x': -135, 'y': -100, 'fps': 37, 'sfx': None, 'alpha': 255, 'on_character': True,},]

    engine = engines.BattleAnimationSystem(script)
    return engine

def bolting(character):
    animation = setup.bolting_dict['1']
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': -135, 'y': -100, 'fps': 3, 'sfx': setup.SFX['bolting_sparks'], 'alpha': 240, 'center_on_screen': True, 'on_character': False, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 1, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 240, 'center_on_screen': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 2, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 240, 'center_on_screen': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -135, 'y': -100, 'fps': 3, 'sfx': None, 'alpha': 240, 'center_on_screen': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -15, 'y': -204, 'fps': 3, 'sfx': None, 'alpha': 240, 'center_on_screen': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 5, 'x': 95, 'y': -204, 'fps': 3, 'sfx': None, 'alpha': 240, 'center_on_screen': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 6, 'x': -15, 'y': -204, 'fps': 3, 'sfx': None, 'alpha': 240, 'center_on_screen': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 7, 'x': -65, 'y': -204, 'fps': 3, 'sfx': None, 'alpha': 240, 'center_on_screen': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 8, 'x': 20, 'y': -204, 'fps': 3, 'sfx': None, 'alpha': 240, 'center_on_screen': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 9, 'x': -135, 'y': -204, 'fps': 3, 'sfx': None, 'alpha': 240, 'center_on_screen': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 10, 'x': 110, 'y': -204, 'fps': 3, 'sfx': None, 'alpha': 240, 'center_on_screen': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 11, 'x': -135, 'y': -204, 'fps': 3, 'sfx': None, 'alpha': 240, 'center_on_screen': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': -135, 'y': -100, 'fps': 50, 'sfx': None, 'alpha': 240, 'center_on_screen': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 15, 'x': -227, 'y': -350, 'fps': 1, 'sfx': setup.SFX['bolting_hit'], 'alpha': 240, 'center_on_screen': False, 'on_character': True, 'animation_2': flash_white_background(), 'play_animation': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 15, 'x': -227, 'y': -350, 'fps': 2, 'sfx': None, 'alpha': 240, 'center_on_screen': False, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD, 'no_reset_animation_2': True},
              {'frame': 16, 'x': -227, 'y': -350, 'fps': 2, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 17, 'x': -227, 'y': -350, 'fps': 2, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 18, 'x': -227, 'y': -350, 'fps': 2, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 19, 'x': -227, 'y': -350, 'fps': 2, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': -227, 'y': -350, 'fps': 37, 'sfx': None, 'alpha': 240, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              ]

    engine = engines.BattleAnimationSystem(script)
    return engine

def blizzaga(character, flip=False):
    if flip == True:
        animation = setup.flip_bliz_dict
    else:
        animation = setup.bliz_dict
    x = 125
    y = 190
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': -x, 'y': -y, 'fps': 2, 'sfx': setup.SFX['ice3'], 'alpha': 240, 'on_character': True,},
              {'frame': 1, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 2, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 5, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 6, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 7, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 8, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 9, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 10, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 13, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 14, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 15, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 16, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 17, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 18, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 19, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 20, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 21, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 22, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 23, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 24, 'x': -115, 'y': -250, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': 25, 'x': -115, 'y': -250, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': 26, 'x': -115, 'y': -250, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': 27, 'x': -115, 'y': -250, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': None, 'x': -x, 'y': -y, 'fps': 37, 'sfx': None, 'alpha': 240,},]

    engine = engines.BattleAnimationSystem(script)
    return engine

def haste(character):
    animation = setup.haste_dict[0]
    x = 185
    y = 95
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': -x, 'y': -y, 'fps': 2, 'sfx': setup.SFX['haste'], 'alpha': 240, 'on_character': True,},
              {'frame': 1, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 2, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 5, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 6, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 7, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 8, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 9, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 10, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 13, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 14, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 15, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 16, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 17, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 18, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 19, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 20, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 21, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 22, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 23, 'x': -x, 'y': -y, 'fps': 2, 'sfx': None, 'alpha': 240,},
              {'frame': 24, 'x': -x, 'y': -y, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': 25, 'x': -x, 'y': -y, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': 26, 'x': -x, 'y': -y, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': 27, 'x': -x, 'y': -y, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': 28, 'x': -x, 'y': -y, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': 29, 'x': -x, 'y': -y, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': 30, 'x': -x, 'y': -y, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': 31, 'x': -x, 'y': -y, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': 32, 'x': -x, 'y': -y, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': 33, 'x': -x, 'y': -y, 'fps': 3, 'sfx': None, 'alpha': 240,},
              {'frame': None, 'x': -x, 'y': -y, 'fps': 37, 'sfx': None, 'alpha': 240,},]

    engine = engines.BattleAnimationSystem(script)
    return engine

def bio(character):
    animation = setup.bio_dict[0]
    x = 200
    y = 130
    fps = 2
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': -x, 'y': -y, 'fps': fps, 'sfx': setup.SFX['bio'], 'alpha': 255, 'on_character': True,},
              {'frame': 1, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 2, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 5, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 6, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 7, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 8, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 9, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 10, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 13, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 14, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 15, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 16, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 17, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 18, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 19, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 20, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 21, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 21, 'x': -x, 'y': -y, 'fps': -5, 'sfx': None, 'alpha': 255, 'alpha_pts': 0, 'flag_1': True,},
              {'frame': None, 'x': -x, 'y': -y, 'fps': 25, 'sfx': None, 'alpha': 255, 'flag_1': False,},
              ]

    engine = engines.BattleAnimationSystem(script, repeat=False)
    return engine

def barrier(character):
    animation = setup.barrier_dict[0]
    x = 245
    y = 275
    fps = 2
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': -x, 'y': -y, 'fps': fps, 'sfx': setup.SFX['barrier'], 'alpha': 255, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD, 'sfx_volume': 0.25},
              {'frame': 1, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 2, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 2, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 1, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 0, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': -x, 'y': -y, 'fps': 25, 'sfx': None, 'alpha': 255, 'flag_1': False,},
              ]

    engine = engines.BattleAnimationSystem(script, repeat=True)
    return engine

def restore(character):
    animation = setup.restore_dict[0]
    x = 410
    y = 220
    fps = 2
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': -x, 'y': -y, 'fps': fps, 'sfx': setup.SFX['restore'], 'alpha': 255, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD, 'sfx_volume': 0.25},
              {'frame': 1, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 2, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 5, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 6, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 7, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 8, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 9, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 10, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 10, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 9, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 8, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 7, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 6, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 5, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 2, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 1, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': 0, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': -x, 'y': -y, 'fps': 25, 'sfx': None, 'alpha': 255,},
              ]

    engine = engines.BattleAnimationSystem(script, repeat=False)
    return engine

def poison(character):
    animation = setup.poison_dict[0]
    x = 70
    y = 77
    fps = 2
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': -x, 'y': -y, 'fps': fps, 'sfx': setup.SFX['poison'], 'alpha': 255, 'on_character': True,},
              {'frame': 1, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 2, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 5, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 6, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 7, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 8, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 9, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 10, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 13, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 14, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 15, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 16, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 17, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 18, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 19, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 20, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 21, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 22, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 23, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 24, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 25, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 26, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': 27, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255,},
              {'frame': None, 'x': -x, 'y': -y, 'fps': 35, 'sfx': None, 'alpha': 255,},
              ]

    engine = engines.BattleAnimationSystem(script, repeat=False)
    return engine

#Item Animations    
def potion_use(character):
    animation = setup.potion_dict['1']
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': 7, 'y': -35, 'fps': 6, 'sfx': setup.SFX['healing_sound0'], 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 7, 'y': -35, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 2, 'x': 7, 'y': -35, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 3, 'x': 7, 'y': -35, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 4, 'x': 7, 'y': -35, 'fps': 4, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 5, 'x': 7, 'y': -35, 'fps': 4, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 6, 'x': 7, 'y': -35, 'fps': 4, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': None, 'x': 7, 'y': -35, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 7, 'x': 7, 'y': -35, 'fps': 6, 'sfx': setup.SFX['healing_sound2'], 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 8, 'x': 7, 'y': -35, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 9, 'x': 7, 'y': -35, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 10, 'x': 7, 'y': -15, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': None, 'x': 7, 'y': -15, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 11, 'x': 0, 'y': -5, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 12, 'x': 7, 'y': -5, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 13, 'x': -7, 'y': -5, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': None, 'x': 7, 'y': -15, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              ]

    engine = engines.BattleAnimationSystem(script)
    return engine

def ether_use(character):
    animation = setup.ether_dict['1']
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': 7, 'y': -35, 'fps': 6, 'sfx': setup.SFX['healing_sound0'], 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 7, 'y': -35, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 2, 'x': 7, 'y': -35, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 3, 'x': 7, 'y': -35, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 4, 'x': 7, 'y': -35, 'fps': 4, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 5, 'x': 7, 'y': -35, 'fps': 4, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 6, 'x': 7, 'y': -35, 'fps': 4, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': None, 'x': 7, 'y': -35, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 7, 'x': 7, 'y': -35, 'fps': 6, 'sfx': setup.SFX['healing_sound2'], 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 8, 'x': 7, 'y': -35, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 9, 'x': 7, 'y': -35, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 10, 'x': 7, 'y': -15, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': None, 'x': 7, 'y': -15, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 11, 'x': 0, 'y': -5, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 12, 'x': 7, 'y': -5, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 13, 'x': 7, 'y': -5, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': None, 'x': 7, 'y': -15, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              ]

    engine = engines.BattleAnimationSystem(script)
    return engine

def dagger_hit(character):
    animation = setup.dagger_hit_dict['1']
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': 6, 'y': -16, 'fps': 3, 'sfx': setup.SFX['sword_hit2'], 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': -2, 'y': -16, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 2, 'x': -13, 'y': -16, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 3, 'x': -13, 'y': -16, 'fps': 9, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 4, 'x': -16, 'y': -16, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 5, 'x': -28, 'y': -16, 'fps': 3, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': None, 'x': -28, 'y': -16, 'fps': 1, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              ]

    engine = engines.BattleAnimationSystem(script)
    return engine

def sword_hit(character):
    animation = setup.sword_hit_dict['1']
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': 0, 'y': 14, 'fps': 2, 'sfx': setup.SFX['sword_hit2'], 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': -2, 'y': 7, 'fps': 1, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 2, 'x': -4, 'y': -1, 'fps': 1, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 3, 'x': -4, 'y': -9, 'fps': 1, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 4, 'x': 4, 'y': -29, 'fps': 1, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 5, 'x': 4, 'y': -39, 'fps': 1, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 6, 'x': 0, 'y': -45, 'fps': 1, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 7, 'x': -2, 'y': -54, 'fps': 1, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': None, 'x': -2, 'y': -54, 'fps': 1, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              ]

    engine = engines.BattleAnimationSystem(script)
    return engine 

def flash_white_background():
    animation = [make_colored_background(WHITE)]
    script = [{'mode': 'special_fx', 'animation': animation, 'character': None, 'target': None},
              {'frame': 0, 'x': 0, 'y': 0, 'fps': 25, 'sfx': None, 'alpha': 0, 'alpha_pts': 255, 'flag_1': True, 'center_on_screen': True, 'on_character': False, 'on_target': False},
              {'frame': 0, 'x': 0, 'y': 0, 'fps': -25, 'sfx': None, 'alpha': 255, 'alpha_pts': 0, 'flag_1': True, 'center_on_screen': True, 'on_character': False, 'on_target': False},
              ]

    engine = engines.BattleAnimationSystem(script)
    return engine 

def white_background():
    animation = [make_colored_background(WHITE)]
    script = [{'mode': 'special_fx', 'animation': animation, 'character': None, 'target': None},
              {'frame': 0, 'x': 0, 'y': 0, 'fps': 1, 'sfx': None, 'alpha': 255,  'center_on_screen': True, 'on_character': False, 'on_target': False},
              ]

    engine = engines.BattleAnimationSystem(script)
    return engine 

def revive_use(character):
    animation = setup.revive_dict['1']
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': 15, 'y': -50, 'fps': 2, 'sfx': setup.SFX['phoenix_down'], 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': 15, 'y': -50, 'fps': 4, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 3, 'y': -45, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': 15, 'y': -40, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 3, 'y': -35, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': 15, 'y': -30, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 3, 'y': -25, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': 15, 'y': -20, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 3, 'y': -15, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': 15, 'y': -10, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 3, 'y': -5, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': 15, 'y': 0, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 3, 'y': 5, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': 15, 'y': 10, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 3, 'y': 15, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': 15, 'y': 20, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 3, 'y': 25, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': 15, 'y': 30, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 3, 'y': 35, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 0, 'x': 15, 'y': 40, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 1, 'x': 3, 'y': 40, 'fps': 6, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': None, 'x': 15, 'y': 40, 'fps': 15, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 2, 'x': 15, 'y': 40, 'fps': 7, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 3, 'x': 11, 'y': 40, 'fps': 7, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 4, 'x': 15, 'y': 40, 'fps': 7, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': 5, 'x': 15, 'y': 40, 'fps': 7, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              {'frame': None, 'x': 15, 'y': 40, 'fps': 8, 'sfx': None, 'alpha': 255, 'center_on_screen': False, 'on_character': True, 'on_target': False},
              ]

    engine = engines.BattleAnimationSystem(script)
    return engine 

#Fade
fade = engines.Fade()

#Special Move Effects
def shock(character):
    animation = setup.shock_dict[0]
    x = -630
    y = -150
    fps = 1
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': None, 'x': x, 'y': y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'animation_2': character.melee_attack, 'animation_3': character.weapon_animation, 'play_animation': True, 'no_reset_animation_2': True},
              {'frame': 0, 'x': x, 'y': y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD, 'play_animation': True},
              {'frame': 1, 'x': x, 'y': y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD, 'play_animation': True},
              {'frame': 2, 'x': x, 'y': y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD, 'play_animation': True},
              {'frame': None, 'x': x, 'y': y, 'fps': 1, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'animation_4': white_background(), 'play_animation': True, 'blend_mode': pg.BLEND_RGBA_ADD},
              {'frame': None, 'x': 0, 'y': 0, 'fps': 1, 'sfx': None, 'alpha': 255,  'center_on_screen': True, 'on_character': False, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD, 'play_animation': True, 'cancel_animation4': True},
              {'frame': 3, 'x': x, 'y': y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD, 'play_animation': True},
              {'frame': 4, 'x': x, 'y': y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD, 'play_animation': True},
              {'frame': 5, 'x': x, 'y': y, 'fps': fps, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD, 'play_animation': True},
              {'frame': None, 'x': x, 'y': y, 'fps': 45, 'sfx': None, 'alpha': 200, 'center_on_screen': False, 'on_character': True, 'on_target': False, 'blend_mode': pg.BLEND_RGBA_ADD, 'play_animation': True},]

    engine = engines.BattleAnimationSystem(script, repeat=False)
    return engine

def swan_dance_player_animation(character):
    script = [{'mode': 'unit'},
              {'character': character, 'action': 21, 'frame': None, 'x': -85, 'y': 0, 'speed_x': -5, 'speed_y': 0, 'fps': 3, 'alpha': 255},
              {'character': character, 'action': 4, 'frame': 0, 'x': -85, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 3, 'alpha': 255},
              {'character': character, 'action': 7, 'frame': 0, 'x': -85, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 3, 'alpha': 255},
              {'character': character, 'action': 4, 'frame': 0, 'x': -85, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 3, 'alpha': 255},
              {'character': character, 'action': 7, 'frame': 0, 'x': -85, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 3, 'alpha': 255},
              {'character': character, 'action': 4, 'frame': 0, 'x': -85, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 30, 'alpha': 255},
              {'character': character, 'action': 14, 'frame': 0, 'x': -85, 'y': 0, 'speed_x': 0, 'speed_y': 0, 'fps': 15, 'alpha': 255},
              ]

    engine = engines.BattleAnimationSystem(script)
    return engine

#Skill Animations
def resolve(character):
    animation = setup.resolve_dict[0]
    x = 430
    y = 242
    fps = 1
    script = [{'mode': 'special_fx', 'animation': animation, 'character': character, 'target': None},
              {'frame': 0, 'x': -x, 'y': -y, 'fps': fps, 'sfx': setup.SFX['shell'], 'alpha': 255, 'on_character': True, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 1, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 2, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 3, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 4, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 5, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 6, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 7, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 8, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 9, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 10, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 11, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 12, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 13, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 14, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 15, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 16, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 17, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 18, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 19, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 20, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 21, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 22, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 23, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 24, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 25, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 26, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 27, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 28, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 29, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 30, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 31, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 32, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 33, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 34, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 35, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': 36, 'x': -x, 'y': -y, 'fps': fps, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              {'frame': None, 'x': -x, 'y': -y, 'fps': 30, 'sfx': None, 'alpha': 255, 'blend_mode': pg.BLEND_RGBA_ADD,},
              ]

    engine = engines.BattleAnimationSystem(script, repeat=True)
    return engine
