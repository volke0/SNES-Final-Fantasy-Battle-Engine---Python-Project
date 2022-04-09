import pygame as pg
import os 
from vars import *

pg.font.init()

def get_default_font():
  return 'resources/fonts/ARIAL.ttf'

def drawText(screen, text, x, y, align='topleft', font_size=24, color=WHITE):
    font = pg.font.Font(get_default_font(), font_size)
    dropshadow_offset = 1 + (font_size // 15)
    # make the overlay text
    text_image = font.render(text, True, color)
    # make rect for the text
    text_rectangle = text_image.get_rect()
    if align == 'topleft':
        text_rectangle.topleft = (x, y)
    if align == 'center':
        text_rectangle.center = (x, y)
    # make the drop shadow 
    dropshadow_text = font.render(text, True, BLACK)
    screen.blit(dropshadow_text, (text_rectangle.x + dropshadow_offset, text_rectangle.y + dropshadow_offset) )
    # draw the actual text now
    screen.blit(text_image, text_rectangle)

def storeText(text, font_size=24, color=WHITE):
    font = pg.font.Font(get_default_font(), font_size)
    text_image = font.render(text, True, color)
    text_rectangle = text_image.get_rect()

    dropshadow_text = font.render(text, True, BLACK)

    return text_image, text_rectangle, dropshadow_text

def load_all_gfx(directory, colorkey=BLACK, accept=('.png', '.jpg', '.bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic) # get the name and extension
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
        else:
            img = None
        graphics[name] = img 
    return graphics 

def create_single_images_animation(directory, scale, colorkey=BLACK, accept=('.png', '.jpg', '.bmp', '.gif')):
    gfx = []
    flip_gfx = []
    for image in os.listdir(directory):
        name, ext = os.path.splitext(image)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, image))
            img = pg.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
            img.set_colorkey(colorkey)
        else:
            pass
        gfx.append(img)
        # temp_img = pg.transform.flip(weapon_animation[0], True, False)
        # temp_img.set_colorkey(BLACK)
        img = pg.transform.flip(img, True, False)
        img.set_colorkey(colorkey)
        flip_gfx.append(img)
    return gfx, flip_gfx

def load_all_sfx(directory, accept=('.wav', '.ogg', '.mp3')):
    sounds = {}
    for sound in os.listdir(directory):
        name, ext = os.path.splitext(sound) # get the name and extension of the sound
        if ext.lower() in accept:
            snd = pg.mixer.Sound(os.path.join(directory, sound))
        sounds[name] = snd 
    return sounds

def load_all_music(directory, accept=('.wav', '.ogg', '.mp3')):
    sounds = {}
    for sound in os.listdir(directory):
        name, ext = os.path.splitext(sound) # get the name and extension of the sound
        if ext.lower() in accept:
            snd = pg.mixer.music.load(os.path.join(directory, sound))
        sounds[name] = snd 
    return sounds

def create_player_animation_dict(name, GFX, battle_width=32, battle_height=32):
    player_dict = {}

    #Overworld Sprites
    sprite_names1 = ['face_down', 'face_left', 'face_right', 'face_up']
    frame_list1 = [3, 3, 3, 3]

    #Battle Sprites
    sprite_names2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
    frame_list2 = create_quick_framelist(sprite_names2, 3)

    #Portraits
    sprite_names3 = ['Portrait']
    frame_list3 = [1]

    overworld = make_player_overworld_animations(f'{name}1', GFX, CHARACTER_TILESIZE_1, sprite_names1, frame_list1)
    battle = make_player_battle_animations(f'{name}2', GFX, battle_width, battle_height, sprite_names2, frame_list2)
    portrait = make_player_portrait(f'{name}3', GFX, CHARACTER_TILESIZE_3, CHARACTER_TILESIZE_3, sprite_names3, frame_list3)
    return overworld, battle, portrait 

def create_background_dict(name, GFX, rows, columns, scale):
    bg_names = ['plains', 'forest1', 'forest2', 'forest3', 'swamp1', 'swamp2', 'river1', 'river2',
                'shore', 'dungeon1', 'dungeon2', 'dungeon3', 'dungeon4', 'dungeon5', 'dungeon6', 'dungeon7',
                'tomb1', 'tomb2', 'cave1', 'cave2', 'cave3', 'cave4', 'lavacave1', 'lavacave2', 'icecave1',
                'sandcave1', 'desert1', 'desert2', 'town1', 'ship1', 'space_vortex1']
    frame_list = create_quick_framelist(bg_names)
    backgrounds = make_player_portrait(name, GFX, 520, 260, bg_names, frame_list, rows, columns, scale)
    return backgrounds

def create_weapon_dict(name, GFX, rows, columns, scale):
    rows = 11
    columns = 16
    weapon_names = ['iron_axe', 'silver_axe', 'hand_axe', 'halberd', 'iron_hammer', 'silver hammer',
                    'heavy_hammer', '0', 'short_sword', 'knife1', 'knife2', 'knife3', 'knife4', '1',
                    'numb_chuck1', 'numb_chuck2', '', 'wooden_wand', 'iron_wand', 'staff1', 'staff2',
                    'staff3', 'staff4', '2', 'long_sword1', 'iron_sword', 'silver_sword', 'rune_sword',
                    'rapier', 'green_rapier', 'broad_sword1', 'broad_sword2', 'broad_sword3', 
                    'green_sword', 'cobolt_sword', 'scimicar', 'bent_sword', 'red_rapier', 'bane_sword',
                    'exacilibur']
    frame_list = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 12, 5, 5, 6, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4,
                  4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    weapons = make_player_portrait(name, GFX, 58, 48, weapon_names, frame_list, rows, columns, scale)
    return weapons

def create_enemy_battle_dict(GFX, scale):
    rows = 1
    columns = 9

    name_list = ['goblin1', 'goblin2', 'wolf1', 'wolf2', 'wolf3', 'wolf4'] 
    name = 'enemies'
    frame_list = create_quick_framelist(name_list, 1)
    enemies = make_player_portrait(name, GFX, 45, 38, name_list, frame_list, rows, columns, scale)
    return enemies 

def create_sfx_gfx_dict(name, GFX, width, height, rows, columns, scale):
    sfx_name_list = ['1']
    num = create_quick_name_list(rows, columns)
    frame_list = create_quick_framelist(sfx_name_list, (num))
    sfx = make_player_portrait(name, GFX, width, height, sfx_name_list, frame_list, rows, columns, scale)
    return sfx


def make_player_overworld_animations(name, spritesheet_dict, tilesize, sprite_names, frame_list):
    img = spritesheet_dict[name]
    resolution_rect = img.get_rect().size 
    rows = 4 
    columns = 3
    scale = 2 
    color_key = BLACK
    img = SpriteSheet(img, scale, color_key, tilesize, tilesize)
    animation_dict = img.create_animation_dict(sprite_names, columns, rows, frame_list)
    return animation_dict

def make_player_battle_animations(name, spritesheet_dict, width, height, sprite_names, frame_list):
    img = spritesheet_dict[name]
    resolution_rect = img.get_rect().size 
    rows = 7
    columns = 9
    scale = 3
    color_key = BLACK
    animation_test = False
    
    img = SpriteSheet(img, scale, color_key, width, height)
    animation_dict = img.create_animation_dict(sprite_names, columns, rows, frame_list, animation_test)
    return animation_dict

def make_player_portrait(name, spritesheet_dict, height, width, sprite_names, frame_list, rows=1, columns=1, scale=2):
    img = spritesheet_dict[name]
    resolution_rect = img.get_rect().size 
    color_key = BLACK
    animation_dict = {}
    img = SpriteSheet(img, scale, color_key, height, width)
    animation_dict = img.create_animation_dict(sprite_names, columns, rows, frame_list)
    return animation_dict

def create_quick_framelist(names, num=1):
    frame_list = []
    for name in range(len(names)):
        frame_list.append(num)
    return frame_list

def create_quick_name_list(rows, columns):
    temp_list = []
    num = rows * columns 
    return num

class SpriteSheet:
    def __init__(self, image, scale, color, width, height):
        self.sheet = image 
        self.scale = scale 
        self.color = color 
        self.width = width 
        self.height = height 

    def get_image(self, frame_x, frame_y):
        image = pg.Surface((self.width, self.height), pg.SRCALPHA)
        image.blit(self.sheet, (0, 0), ((frame_x * self.width), (frame_y * self.height), self.width,
                   self.height))
        image = pg.transform.scale(image, (self.width * self.scale, self.height * self.scale))
        image.set_colorkey(self.color)
        return image 

    def create_animation_dict(self, names, columns, rows, frame_list, animation_test=False):
        step_x = 0
        step_y = 0 

        animation_dict = {}

        for name in range(len(names)):
            frame = frame_list[name]
            temp_img_list = []
            for _ in range(frame):
                temp_img_list.append(self.get_image(step_x, step_y))
                step_x += 1
                if step_x >= columns:
                    step_x = 0
                    step_y += 1

            animation_dict.update({names[name]: temp_img_list})

        return animation_dict

        