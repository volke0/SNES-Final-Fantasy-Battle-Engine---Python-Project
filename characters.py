import pygame as pg 
import utils, setup, animations, abilities, bars, inventory_system, ai
import random
from vars import *

class Character:
    def __init__(self, GFX, screen):
        self.gfx = GFX
        self.screen = screen
        self.ingame_name = 'Generic Person'
        self.job = 'Villager'
        self.playable_character = False

        #Equipment
        self.equipment = {0: None, 1: None, 2: None, 3: None, 4: None}

        #Stats
        self.base_stats = self.intialize_base_stats()
        self.stats = self.base_stats
        self.ability_list = ['Attack', 'Abilities', 'Items']

        #Battle Variables
        self.action_counter = 0
        self.ready = False
        self.waiting = False
        self.fighting = False
        self.is_dead = False
        self.using_magic = False
        self.turn = 0
        self.damage_calculation_done = False
        self.item_done = False
        self.buff_done = False

        #Mask
        self.mask_on = False

        #Player List
        self.player_list = []

        #Enemy List 
        self.enemy_list = []

        #Stats
        self.level = 1
        self.hp = self.stats['hp']
        self.current_hp = self.hp
        self.mp = self.stats['mp']
        self.current_mp = self.mp
        self.strength = self.stats['strength']
        self.magic = self.stats['magic']
        self.speed = self.stats['speed']
        self.defense = self.stats['defense']
        self.resistance = self.stats['resistance']
        self.luck = self.stats['luck']
        self.skill = self.stats['skill']
        self.hit_chance = 0
        self.avoid = 0
        self.crit_chance = 0
        self.crit_dmg = 50

        #Buff Variables
        self.buffs = {}
        self.icon_index = 0
        self.buff_wait = False

        #Skills
        self.skills = {}

    def intialize_base_stats(self, level=1, hp=40, mp=30, strength=35, mag=5, spd=15, defense=20, res=15, 
                                luck=5, skill=30):
        stats = {'lvl': level, 'hp': hp, 'mp': mp, 'current_hp': hp, 'current_mp': mp,
                 'strength': strength, 'magic': mag, 'speed': spd, 'defense': defense, 'resistance': res, 
                 'luck': luck, 'skill': skill}
        return stats

class Player(Character):
    def __init__(self, GFX, screen, script):
        super().__init__(GFX, screen)
        self.gfx = GFX
        self.screen = screen
        self.script = script

        #Character Basic Info
        self.name = None
        self.ingame_name = None
        self.job = None
        self.playable_character = True
        self.weapon_dict = setup.weapon_dict
        self.battle_width = 32
        self.battle_height = 32

        #Character Stats
        self.level = 1
        self.hp = 0
        self.current_hp = 0
        self.mp = 0
        self.current_mp = 0
        self.strength = 0
        self.magic = 0
        self.skill = 0
        self.speed = 0
        self.luck = 0
        self.defense = 0
        self.resistance = 0
        self.special_gauge = 0
        self.exp = 0
        self.max_special_gauge = 10

        #Character Growth Rates
        self.growths = {}

        #Character Abilities
        self.ability_list = []
        self.magic_learned = []

        #Player Equipment
        self.equipment = {0: None, 1: None, 2: None, 3: None, 4: None}

        #Player Palettes
        self.palettes = None

        #Create Character
        self.make_character()
        self.specials_learned = self.script['specials_learned']
        self.specials_list = None
        self.make_specials_list()
        self.weapon = self.equipment[0]

        #Player Specific Palette
        self.palette = self.gfx[f'{self.name}_palette']

        #Player Dictionaries
        self.player_overworld, self.player_battle, self.player_portrait = utils.create_player_animation_dict(self.name, self.gfx, self.battle_width, self.battle_height)

        #Player Rectangles
        self.overworld_rect = self.player_overworld['face_down'][0].get_rect()
        self.battle_rect = self.player_battle['1'][0].get_rect()
        self.portrait_rect = self.player_portrait['Portrait'][0].get_rect()


        #Player Stats and Abilities
        self.base_stats = self.intialize_base_stats(level=self.level, hp=self.hp, mp=self.mp, strength=self.strength, mag=self.magic, spd=self.speed, 
                                                     defense=self.defense, res=self.resistance, luck=self.luck, skill=self.skill)

        self.stats = self.base_stats

        #Party Position
        self.party_index = 0

        #Animations
        self.animation = self.player_battle
        self.action = '1'
        self.frame = 0

        #Battle Variables
        self.enter_battle = True
        self.fight_ready = False
        self.ready = False
        self.waiting = False
        self.action_counter = 0
        self.start = [0, 0]
        self.is_dead = False

        #Mask Variables
        self.mask_on = False
        self.generate_mask = True
        self.mask_name = None
        self.mask_in_done = False
        self.mask_out_done = True
        self.mask_alpha = 0
        self.mask_fps = 5

        #Battle Animations
        self.stand = animations.player_stand(self)
        self.melee_wait = animations.player_melee_wait(self)
        self.melee_attack = animations.player_attack_melee(self)
        self.walk_back = animations.player_walk_back(self)
        self.hit = animations.player_hit(self)
        self.low_hp = animations.player_low_hp(self)
        self.dead = animations.player_dead(self)
        self.victory_dance = animations.player_victory_dance(self)
        self.entrance = animations.player_enter_battle(self)
        self.walk_up = animations.player_walk_up(self)
        self.use_item = animations.player_use_item(self)
        self.weapon_animation = None
        self.use_magic = animations.player_use_magic(self)
        self.magic_wait = animations.player_magic_wait(self)

        #Bars
        self.ab_coord = [625, 458]
        self.action_bar = None
        self.special_bar = None
        self.flash_special_bar = False

        #Create Magic List
        self.magic_list = self.get_magic_list()

    def make_palette_mask(self, mask, color=[RED], pixel_location=[0], distance=0):
        #Get the color you want to change and unmap it
        palette_pxarray = pg.PixelArray(self.palette)
        mapped = []
        unmap = []
        for index in range(len(pixel_location)):
            y = pixel_location[index][0]
            x = pixel_location[index][1]
            mapped.append(palette_pxarray[y][x])
            unmap.append(self.palette.unmap_rgb(mapped[index]))
        #Next copy the entire animation dict and replace the chosen pixel color with another color
        for action in range(len(self.animation)):
            num = action + 1
            temp_list = []
            for frame in range(len(self.animation[str(num)])):
                pixel_array = pg.PixelArray(self.animation[str(num)][frame])
                frame = pixel_array.make_surface()
                frame.get_alpha()
                frame.set_colorkey(BLACK)
                pixel_array.close()
                frame_array = pg.PixelArray(frame)
                for k in range(len(unmap)):
                    frame_array.replace(unmap[k], color[k], distance=distance)
                frame_array.close()
                frame.get_alpha()
                temp_list.append(frame)

            mask.update({str(num): temp_list})
        palette_pxarray.close()

    def make_character(self):
        self.name = self.script['name']
        self.ingame_name = self.script['ingame_name']
        self.job = self.script['job']

        #Stats
        self.level = self.script['stats'][0]['level']
        self.hp = self.script['stats'][0]['hp']
        self.current_hp = self.hp
        self.mp = self.script['stats'][0]['mp']
        self.current_mp = self.mp
        self.strength = self.script['stats'][0]['strength']
        self.magic = self.script['stats'][0]['magic']
        self.speed = self.script['stats'][0]['speed']
        self.defense = self.script['stats'][0]['defense']
        self.resistance = self.script['stats'][0]['resistance']
        self.luck = self.script['stats'][0]['luck']
        self.skill = self.script['stats'][0]['skill']

        #Growths
        #N/A

        #Equipment
        self.equipment = self.script['equipment'][0]

        #Abilities
        self.ability_list = self.script['ability_list']
        self.magic_learned = self.script['magic_learned']

        #Art/Animations
        self.battle_width = self.script['battle_tile_size'][0]
        self.battle_height = self.script['battle_tile_size'][1]

        #Palettes
        self.palettes = self.script['palettes']


    def update_stats(self, temp=True, hp=0, mp=0, strength=0, magic=0, speed=0, defense=0, resistance=0, luck=0, skill=0):
        #Stats
        if temp == True:
            self.hp += hp
            self.mp += mp
            self.strength += strength
            self.magic += magic
            self.speed += speed
            self.defense += defense
            self.resistance += resistance
            self.luck += luck
            self.skill += skill
        else:
            self.base_stats['hp'] += hp
            self.base_stats['mp'] += mp
            self.base_stats['strength'] += strength
            self.base_stats['magic'] += magic
            self.base_stats['speed'] += speed
            self.base_stats['defense'] += defense
            self.base_stats['resistance'] += resistance
            self.base_stats['luck'] += luck
            self.base_stats['skill'] += skill

    def update(self):
        pass

    def draw(self, text_spacing):
        self.frame_manager()
        if self.entrance.done == False:
            self.entrance.play()
            self.action_bar = bars.ActionBar(self.ab_coord[0], (self.ab_coord[1] + text_spacing), MAX_ACTION_VALUE)
            self.special_bar = bars.ActionBar(self.ab_coord[0], (self.ab_coord[1] + 17 + text_spacing), MAX_SPECIAL_VALUE)
        self.screen.blit(self.animation[self.action][int(self.frame)], self.battle_rect)
        if self.mask_on == True:
            self.play_mask()

    def play_mask(self):
        mask = {}
        palette = None
        if self.mask_name.lower() == 'haste':
            palette = self.palettes['haste']
        if self.mask_name.lower() == 'poison':
            palette = self.palettes['poison']
        self.make_palette_mask(mask, palette['p'], pixel_location=palette['location'], distance=0)
        if 'effect' in palette:
            if palette['effect'] == 'glow':
                if self.mask_out_done == True:
                    self.mask_alpha += self.mask_fps
                if self.mask_in_done == True:
                    self.mask_alpha -= self.mask_fps
                if self.mask_alpha > 255:
                    self.mask_in_done = True
                    self.mask_out_done = False
                elif self.mask_alpha < 0:
                    self.mask_out_done = True
                    self.mask_in_done = False
        else:
            self.mask_alpha = 255

        mask[self.action][int(self.frame)].set_alpha(self.mask_alpha)
        self.screen.blit(mask[self.action][int(self.frame)], self.battle_rect)

    def set_start(self, start):
        if self.enter_battle == True:
            self.battle_rect.x = start[0]
            self.battle_rect.y = start[1]
            self.start = [start[0], start[1]]
            self.weapon_animation = animations.weapon_swing(self)

    #Setup the animation for the player
    def setup_animation(self, mode):
        if mode == 'overworld':
            self.animation = self.player_overworld
            self.action = 'face_down'
        if mode == 'battle':
            self.animation = self.player_battle
            self.action = '1'

    def frame_manager(self):
        if int(self.frame) >= len(self.animation[self.action]):
            self.frame = 0

    def get_magic_list(self):
        base_magic_list = abilities.make_master_item_list(abilities.magic_list, character=self, target=self)
        temp_dict = {}
        for index in range(len(base_magic_list)):
            done = False
            for i in range(len(self.magic_learned)):
                if done == False:
                    if base_magic_list[index].name == self.magic_learned[i]:
                        temp_dict.update({index: self.magic_learned[i]})
                        done = True
                    else:
                        temp_dict.update({index: ''})
        return temp_dict

    def make_specials_list(self):
        temp_dict = {}
        for index in range(len(self.specials_learned)):
            special_move = inventory_system.Specials(self.specials_learned[index], character=self)
            temp_dict.update({index: special_move})
        self.specials_list = temp_dict


class Enemy(Character):
    def __init__(self, GFX, screen, script):
        super().__init__(GFX, screen)
        self.gfx = GFX
        self.screen = screen
        self.script = script

        #Names 
        self.name = None
        self.palettes = {'Goblin A': [(255, 196, 211), ((24, 24, 24))]}
        self.ingame_name = None

        #Character Stats
        self.level = 1
        self.hp = 0
        self.current_hp = 0
        self.mp = 0
        self.current_mp = 0
        self.strength = 0
        self.magic = 0
        self.skill = 0
        self.speed = 0
        self.luck = 0
        self.defense = 0
        self.resistance = 0

        #Equipment
        self.equipment = None

        #Abilities
        self.ability_list = None
        self.ai_script = None

        #Create Enemy
        self.make_enemy()

        #Enemy Specific Palette
        self.palette = self.gfx[f'{self.name}_palette']

        #Enemy Dictionaries
        self.animation_dict = utils.create_enemy_battle_dict(self.gfx, 3)

        #Enemy Rectangles
        self.battle_rect = self.animation_dict[self.name][0].get_rect()

        #Enemy Stats 
        self.base_stats = self.intialize_base_stats(hp=self.hp, mp=self.mp, strength=self.strength, mag=self.magic, skill=self.skill, spd=self.speed, luck=self.luck,
                                                    defense=self.defense, res=self.resistance)
        self.stats = self.base_stats

        #Battle Variables
        self.enter_battle = True
        self.action = 0
        self.start = [0, 0]
        self.animation = self.animation_dict[self.name]
        self.is_dead = False
        self.done = False
        self.deleted = False

        #Battle Animations
        self.attacking = None
        self.hit = None
        self.dead = None
        self.set_palette()
        self.action = 0
        self.entrance = animations.enemy_enter_battle(self)

        #AI
        self.ai = None
        self.ai_done = False
        
    def draw(self):
        if self.entrance.done == False:
            self.entrance.play()
        self.screen.blit(self.animation[self.action], self.battle_rect)
        
    def set_start(self, start):
        if self.enter_battle == True:
            self.battle_rect.x = start[0]
            self.battle_rect.y = start[1]
            self.start = [start[0], start[1]]

    def make_enemy(self):
        self.name = self.script['name']
        self.ingame_name = self.script['ingame_name']
        self.job = self.script['job']

        #Stats
        self.level = self.script['stats'][0]['level']
        self.hp = self.script['stats'][0]['hp']
        self.current_hp = self.hp
        self.mp = self.script['stats'][0]['mp']
        self.current_mp = self.mp
        self.strength = self.script['stats'][0]['strength']
        self.magic = self.script['stats'][0]['magic']
        self.speed = self.script['stats'][0]['speed']
        self.defense = self.script['stats'][0]['defense']
        self.resistance = self.script['stats'][0]['resistance']
        self.luck = self.script['stats'][0]['luck']
        self.skill = self.script['stats'][0]['skill']

        #Growths
        #N/A

        #Equipment
        self.equipment = self.script['equipment'][0]

        #Abilities
        self.ability_list = self.script['ability_list']
        self.ai_script = self.script['ai_script']

    def update_stats(self, temp=True, hp=0, mp=0, strength=0, magic=0, speed=0, defense=0, resistance=0, luck=0, skill=0):
        #Stats
        if temp == True:
            self.hp += hp
            self.mp += mp
            self.strength += strength
            self.magic += magic
            self.speed += speed
            self.defense += defense
            self.resistance += resistance
            self.luck += luck
            self.skill += skill
        
    def set_palette(self):
        #Get the color you want to change and unmap it
        palette_pxarray = pg.PixelArray(self.palette)
        mapped = []
        unmap = []
        pixels = [[0,0], [1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0], [8,0], [9,0], [10,0], [11,0], [12,0], [13,0], [14,0], [15,0], [0,1], [1,1], [2,1]]
        for index in range(len(pixels)):
            x = pixels[index][1]
            y = pixels[index][0]
            mapped.append(palette_pxarray[y][x])
            unmap.append(self.palette.unmap_rgb(mapped[index]))

        death_palette = setup.EN_GFX['death_palette']
        death_pxarray = pg.PixelArray(death_palette)
        d_mapped = []
        d_unmap = []
        for index in range(len(pixels)):
            x = pixels[index][1]
            y = pixels[index][0]
            d_mapped.append(death_pxarray[y][x])
            d_unmap.append(death_palette.unmap_rgb(d_mapped[index]))

        #Next make the death animation
        death_animation = self.animation[self.action].copy()
        pixel_array = pg.PixelArray(death_animation)
        for k in range(len(unmap)):
            pixel_array.replace(unmap[k], D_MEDIUM_PURPLE, distance=0)
        pixel_array.close()
        death_animation.get_alpha()
        death_animation.set_colorkey(BLACK)
        self.animation.append(death_animation)

        #Next make the hitting animation
        attacking_animation = self.animation[self.action].copy()
        pixel_array = pg.PixelArray(attacking_animation)
        pixel_array.replace(unmap[15], (WHITE), distance=0.5)
        pixel_array.replace(unmap[3], (PSEUDO_BLACK), distance=0.4)
        pixel_array.close()

        #Close out the other arrays
        death_pxarray.close()
        palette_pxarray.close()

        #Append the attacking animation and make the rest of the enemy animations
        attacking_animation.get_alpha()
        attacking_animation.set_colorkey(BLACK)
        self.animation.append(attacking_animation)
        self.hit = animations.enemy_hit(self)
        self.attacking = animations.enemy_attack(self)
        self.dead = animations.enemy_dead(self)

    def battle_AI(self, party):
        if self.ai_done == False:
            self.ai = ai.AI(self.ai_script, self, party)
            self.ai_done = True
        else:
            self.ai.play()
