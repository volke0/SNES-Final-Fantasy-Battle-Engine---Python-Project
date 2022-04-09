import pygame as pg
import utils, setup, abilities, inventory_system
import random
from vars import *

class AI:
    def __init__(self, script, character, targets):
        self.script = script
        self.character = character
        self.targets = targets

        self.ability_dict = self.character.ability_list
        self.index = 0
        self.max_index = len(self.script) - 1
        self.magic = None

        #Logic Variables
        self.target_choice = []
        self.ab_choice = None
        self.ab_done = False
        self.target_done = False
        self.choice = None
        self.done = False

        #RNG
        self.pick_rng = None

        self.initialize_variables()

    def initialize_variables(self):
        self.pick_rng = random.randint(0, 100)

    def play(self):
        if self.done == False:
            if self.ab_done == False:
                if self.index >= len(self.script):
                    self.ab_done = True
                if 'use_ability' in self.script[self.index]:
                    ability_list = self.script[self.index]['use_ability']
                    for index, rng in ability_list.items():
                        rng_chance = ability_list[index]
                        if self.ability_dict[index]['rng'] <= rng_chance:
                            self.ab_choice = self.ability_dict[index]
                            # print(self.ab_choice)
                            self.ab_done = True
                            break
                        else:
                            self.ab_choice = self.ability_dict[0]
                            self.ab_done = True

            if self.target_done == False:
                index = random.randint(0, (len(self.targets) - 1))
                self.target_choice.append(self.targets[index])
                self.target_done = True

            if self.ab_done == True and self.target_done == True:
                if 'magic' in self.ab_choice:
                    magic = []
                    self.ab_choice = self.ab_choice['name']
                    # print(self.ab_choice)
                    # print(self.character)
                    for index in range(len(self.target_choice)):
                        magic.append(abilities.make_master_item_list(abilities.magic_list, name=self.ab_choice, character=self.character, target=self.target_choice[index], real_magic=True))
                    self.magic = magic
                    self.choice = 'Magic'
                    self.done = True
                elif self.ab_choice['name'] == 'Attack':
                    self.choice = 'Attack'
                    self.done = True

    def reset(self):
        self.done = False
        self.ab_done = False
        self.target_done = False
        self.target_choice = []
        for index in range(len(self.ability_dict)):
            self.ability_dict[index]['rng'] = random.randint(0, 100) 
