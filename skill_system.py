import pygame as pg
import setup, utils, animations
import inventory_system as inv_sys
import battle_system as bat_sys
from vars import *

#script = {'name': 'Resolve', 'type': 'combat', 'sub_type': 'buff', 'buff': [buff_core_stats], 'target_type': 'self', 'activation': 'hp', 'threshold': {'type': 'percent', 'trigger': 'below', 'amount': 50}}
class SkillSystem:
    def __init__(self, character, script):
        self.character = character
        self.script = script

        self.type = self.script['type']
        self.sub_type = self.script['sub_type']

        self.buff_list = []
        self.activation = None
        self.threshold = None
        self.target_type = None

        #Logic Variables
        self.activate = False

        self.initialize_skill()

    def initialize_skill(self):
        if self.sub_type == 'buff':
            for index in range(len(self.script['buff'])):
                self.buff_list.append(self.script['buff'][index])
        self.activation = self.script['activation']
        self.threshold = self.script['threshold']
        self.target_type = self.script['target_type']

    def use(self):
        if self.type == 'combat':
            self.battle_mode()
        elif mode == 'map':
            pass

    def battle_mode(self):
        stat = self.get_activation_stat()
        if self.threshold['trigger'] == 'below':
            if stat <= self.threshold['amount']:
                self.activate = True
            else:
                self.activate = False
        if self.threshold['trigger'] == 'above':
            if stat >= self.threshold['amount']:
                self.activate = True
            else:
                self.activate = False
        self.use()

    def get_activation_stat(self):
        stat = 0
        if self.activation == 'hp':
            if self.threshold['type'] == 'percent':
                stat = round(self.character.current_hp / self.character.hp) * 100
            if self.threshold['type'] == 'flat':
                stat = self.character.current_hp
        return stat

    def use(self):
        if self.activate == True:
            pass
            

    # def apply_buffs(self):
    #     if self.add_buff == True:
    #         for index in range(len(self.buff_list)):
    #             target = None
    #             if self.target_type == 'self':
    #                 target = [self.character]
    #             elif self.target_type == 'allies':
    #                 if self.character.playable_character == True:
    #                     target = self.character.player_list
    #                 else:
    #                     target = self.character.enemy_list
    #             elif self.target_type == 'enemies':
    #                 if self.character.playable_character == True:
    #                     target = self.character.enemy_list
    #                 else:
    #                     target = self.character.player_list
    #             for i in range(len(target)):
    #                 buff = inv_sys.Buffs(self.buff_list[index], target[i])
    #                 target[i].buffs.update({buff.name: buff})
    #         self.add_buff = False