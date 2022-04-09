import pygame as pg 
import characters as c
import setup, utils, abilities
import random
from vars import *

def make_enemy_list(name_list):
    enemy_list = []
    for index in range(len(name_list)):
        enemy_list.append(c.Enemy(setup.EN_GFX, setup.screen, name_list[index], name_list))
    return enemy_list

#Enemy Characters
goblin1_dict = {'name': 'goblin1', 'ingame_name': 'Goblin A', 'job': 'Goblin', 'growths': None,
                'stats': [{'level': 1, 'hp': 3550, 'mp': 30, 'strength': 60, 'magic': 5, 'skill': 40, 'speed': 32,
                           'luck': 0, 'defense': 40, 'resistance': 5}],
                'equipment': [{0: 'iron_dagger', 1: None, 2: None, 3: None, 4: None}],
                'ability_list': {0: {'name': 'Bio', 'magic': True, 'rng': random.randint(0, 100)}, 1: {'name': 'Attack', 'rng': random.randint(0, 100)}},
                'ai_script': [{'use_ability': {0: 35, 1: 90}},
                             ]
                }

#Playable Characters
glenys_dict = {'name': 'glenys', 'ingame_name': 'Glenys', 'job': 'Swordsman', 'growths': None,
               'stats': [{'level': 1, 'hp': 175, 'mp': 50, 'strength': 73, 'magic': 25, 'skill': 45, 'luck': 10,
                          'speed': 65, 'defense': 50, 'resistance': 20}],
               'equipment': [{0: 'iron_sword', 1: None, 2: None, 3: None, 4: None}],
               'ability_list': ['Attack', 'Special', 'Magic', 'Items'],
               'magic_learned': ['Fire 1', 'Haste'],
               'specials_learned': {0: abilities.shock},
               'battle_tile_size': [32,32],
               'palettes': {'haste': haste_palette, 'poison': glenys_poison_palette}}

peachy_dict = {'name': 'peachy', 'ingame_name': 'Lizette', 'job': 'Fashionista', 'growths': None,
               'stats': [{'level': 5, 'hp': 105, 'mp': 250, 'strength': 45, 'magic': 62, 'skill': 30, 'luck': 10,
                          'speed': 48, 'defense': 40, 'resistance': 45}],
               'equipment': [{0: 'iron_wand', 1: None, 2: None, 3: None, 4: None}],
               'ability_list': ['Attack', 'Special', 'Magic', 'Items'],
               'magic_learned': ['Fire 1', 'Blizzard 2', 'Blizzard 3', 'Bolting', 'Cure', 'Cleanse'],
               'specials_learned': {0: abilities.swan_dance},
               'battle_tile_size': [27,32],
               'palettes': {'haste': haste_palette, 'poison': peachy_poison_palette}}

#Player List
player_party_list = [c.Player(setup.PC_GFX, setup.screen, glenys_dict), c.Player(setup.PC_GFX, setup.screen, peachy_dict)]

#Enemy Formation list
enemy_list = [c.Enemy(setup.EN_GFX, setup.screen, goblin1_dict)]