import pygame as pg 
import setup, utils, animations
import copy, random
from vars import *

class Inventory:
    def __init__(self):
        self.inventory = {}
        self.added = False

    def add_item(self, item):
        item = copy.deepcopy(item)
        if item.name in self.inventory:
            self.inventory[item.name][0]['amount'] += 1
        else:
            self.inventory.update({item.name: [{'item': item, 'amount': 1}]})

    def use_item(self, item):
        for option in range(len(self.inventory)):
            if option not in self.inventory:
                continue
            else:
                if self.inventory[option][0]['name'] == item.name:
                    self.inventory[option][0]['item'].use()
                if self.inventory[option][0]['item'].uses <= 0:
                    self.inventory[option][0]['amount'] -= 1
                    self.inventory[option][0]['item'].uses = self.inventory[option][0]['item'].max_uses
                if self.inventory[option][0]['amount'] <= 0:
                    self.inventory.pop(option)
                else:
                    continue

    def make_initial_inventory(self, item_list):
        for index in range(len(item_list)):
            item = copy.deepcopy(item_list[index]['item'])
            if len(self.inventory) > 0:
                for option in range(len(self.inventory)):
                    if self.inventory[option][0]['name'] == item.name:
                        self.inventory[option][0]['amount'] += item_list[index]['amount']
                        self.added = True
                    else:
                        continue
            else:
                self.inventory.update({index: [{'name': item.name, 'item': item, 'description': item.description, 'amount': item_list[index]['amount']}]})
                self.added = True
            if self.added == False:
                self.inventory.update({len(self.inventory): [{'name': item.name, 'item': item, 'description': item.description, 'amount': item_list[index]['amount']}]})
            self.added = False

class Item:
    def __init__(self, script):
        self.script = script
        self.name = self.script['name']
        self.type = self.script['type']
        self.sub_type = None
        self.sub_type = self.script['sub_type']
        self.description = self.script['description']

class Potion(Item):
    def __init__(self, script):
        super().__init__(script)
        self.script = script
        self.uses = None
        self.max_uses = None 
        self.mp_cost = None
        self.hp_cost = None
        self.hp_restore = None
        self.mp_restore = None
        self.revive = False
        self.intialize_variables()

    def use(self):
        self.uses -= 1    

    def intialize_variables(self):
        if 'uses' in self.script:
            self.uses = self.script['uses']
            self.max_uses = self.uses
        if 'mp_cost' in self.script:
            self.mp_cost = self.script['mp_cost']
        if 'hp_cost' in self.script:
            self.hp_cost = self.script['hp_cost']
        if 'hp_restore' in self.script:
            self.hp_restore = self.script['hp_restore']
        if 'mp_restore' in self.script:
            self.mp_restore = self.script['mp_restore']
        if 'revive' in self.script:
            self.revive = self.script['revive']

class Magic(Potion):
    def __init__(self, script, character, target):
        super().__init__(script)
        self.script = script
        self.character = character
        self.target = target

        #Information
        self.description = None
        self.mp_cost = 0

        self.base_damage = 0
        self.magic_scaling = 0
        self.total_damage = 0
        self.heal_hp = False
        self.heal_mp = False

        #Buffs
        self.is_buff = False
        self.buff = None
        self.buff_apply_chance = 0
        self.buff_rng = random.randint(0,100)
        
        self.animation = None

        self.intialize_magic_variables()
        self.intialize_magic_animations()

    def intialize_magic_variables(self):
        if 'base_damage' in self.script:
            self.base_damage = self.script['base_damage']
        if 'user_mag' in self.script:
            self.magic_scaling = self.script['user_mag']
        if 'heal_hp' in self.script:
            self.heal_hp = self.script['heal_hp']
        if 'heal_mp' in self.script:
            self.heal_mp = self.script['heal_mp']
        if 'is_buff' in self.script:
            self.is_buff = self.script['is_buff']
        if self.is_buff == True:
            if 'chance' in self.script['buff']:
                self.buff_apply_chance = self.script['buff']['chance']
            else:
                self.buff_apply_chance = 100
            # print(f'buff chance: {self.buff_apply_chance}')
            # print(f'buff rng: {self.buff_rng}')
            # print(self.buff_rng <= self.buff_apply_chance)
            if self.buff_rng <= self.buff_apply_chance:
                self.buff = Buffs(self.script['buff'], self.target, user=self.character)
            else:
                self.buff = None
        if 'description' in self.script:
            self.description = self.script['description']
        if 'mp_cost' in self.script:
            self.mp_cost = self.script['mp_cost']
        if 'type' in self.script:
            self.type = self.script['type']
        if 'sub_type' in self.script:
            self.sub_type = self.script['sub_type']
        self.magic_scaling = (self.character.magic * self.character.level * self.base_damage) / 32
        if self.character.playable_character == True:
            self.total_damage = round((self.base_damage * 4) + self.magic_scaling)
        else:
            self.total_damage = round(((self.base_damage/2) + self.magic_scaling))
        self.total_damage = self.total_damage * (random.randint(224,255)/256) + 1

    def intialize_magic_animations(self):
        if self.script['name'] == 'Fire 1':
            self.animation = animations.fire(self.target)
        if self.script['name'] == 'Blizzard 2':
            self.animation = animations.blizzaga(self.target)
        if self.script['name'] == 'Blizzard 3':
            self.animation = animations.snow_storm(self.target)   
        if self.script['name'] == 'Bolting':
            self.animation = animations.bolting(self.target)
        if self.script['name'] == 'Cure':
            self.animation = animations.cure(self.target)
        if self.script['name'] == 'Haste':
            self.animation = animations.haste(self.target)
        if self.script['name'] == 'Bio':
            self.animation = animations.bio(self.target)
        if self.script['name'] == 'Cleanse':
            self.animation = animations.restore(self.target)

class Specials:
    def __init__(self, script, character):
        self.script = script
        self.character = character
        self.name = self.script['name']
        self.target = None

        #Parameters
        self.sp_cost = 0
        self.base_damage = 0
        self.total_damage = 0
        self.heal_hp = False
        self.heal_mp = False
        self.level = 0
        self.type = 'damage'
        self.damage_type = 'physical'
        self.hit = 0
        self.crit_dmg = 0
        self.crit_rate = 0

        self.is_buff = False
        self.buff = []
        self.power = 0
        self.description = None
        self.multi_target = False
        self.target_type = 'enemy'

        self.animation = []
        self.vfx_animation = []
        self.vfx_index = 0
        self.vfx_index2 = 0
        self.other_effects = False
        self.animation_done = False
        self.fps = 30
        self.timer = 0

        self.intialize_variables()

    def intialize_variables(self):
        if 'level' in self.script:
            self.level = self.script['level']
        if 'sp_cost' in self.script:
            self.sp_cost = self.script['sp_cost']
        if 'type' in self.script:
            self.type = self.script['type']
        if 'damage_type' in self.script:
            self.damage_type = self.script['damage_type']
        if 'power' in self.script:
            self.power = self.script['power']
        if 'is_buff' in self.script:
            self.is_buff = self.script['is_buff']
        if 'description' in self.script:
            self.description = self.script['description']
        if 'multi_target' in self.script:
            self.multi_target = self.script['multi_target']
        if 'target_type' in self.script:
            self.target_type = self.script['target_type']
        if 'base_damage' in self.script:
            self.base_damage = self.script['base_damage']
        if 'hit' in self.script:
            self.hit = self.script['hit']
        if 'crit_dmg' in self.script:
            self.crit_dmg = self.script['crit_dmg']
        if 'crit_rate' in self.script:
            self.crit_rate = self.script['crit_rate']
        if 'heal_type' in self.script:
            if self.script['heal_type'] == 'hp':
                self.heal_hp = True
            if self.script['heal_type'] == 'mp':
                self.heal_mp
            if self.script['heal_type'] == 'both':
                self.heal_hp = True
                self.heal_mp = True

        self.calculate_damage()

    def calculate_damage(self):
        damage_name = 0
        if self.damage_type == 'magic':
            damage_name = self.character.magic
        elif self.damage_type == 'strength':
            damage_name = self.character.strength
        self.total_damage = (self.base_damage * self.level * 4) + (self.power * damage_name) + damage_name

    def prepare(self, target_list=None):
        if self.name == 'Shock':
            self.animation = animations.shock(self.character)
        if self.name == 'Dance of the Swan':
            self.animation = animations.swan_dance_player_animation(self.character)
            self.other_effects = True
            for index in range(len(target_list)):
                self.vfx_animation.append(animations.cure(target_list[index]))
        if 'buff' in self.script:
            for index in range(len(target_list)):
                self.buff.append(Buffs(self.script['buff'], target_list[index], user=self.character))


    def play(self):
        self.animation.play()

    def reset(self):
        self.animation = []
        self.vfx_animation = []
        self.vfx_index = 0
        self.vfx_index2 = 0

class Buffs:
    def __init__(self, script, character, user=None):
        self.script = script
        self.character = character
        self.user = user

        self.screen = setup.screen

        self.name = None
        self.type = None
        self.mask = None
        self.icon = None
        self.removes_buff = False
        self.buff_removal_list = []

        #Icon Variables
        self.fps = 90
        self.timer = 0

        self.hp = 0
        self.attack = 0
        self.magic = 0
        self.skill = 0
        self.speed = 0
        self.luck = 0
        self.defense = 0
        self.resistance = 0

        #Logic
        self.manual = False

        self.turn = self.character.turn

        #Overtime buffs/debuffs
        self.hot = 0
        self.dot = 0
        self.dot_type = None
        self.dot_done = False

        #Text
        self.damage_text = None
        self.text_animation = None

        #Animations
        self.opening_animation = None
        self.opening_animation_done = False
        self.animation = None

        #Original Stats
        self.stats = {}
        self.modified_stats = {}

        self.max_turns = 0
        self.done = False
        self.intialize_variables()

    def intialize_variables(self):
        self.stats = {'hp': self.character.hp,
                      'strength': self.character.strength,
                      'magic': self.character.magic,
                      'skill': self.character.skill,
                      'speed': self.character.speed,
                      'luck': self.character.luck,
                      'defense': self.character.defense,
                      'resistance': self.character.resistance,
                      }
        self.modified_stats = {'hp': self.character.hp,
                               'strength': self.character.strength,
                               'magic': self.character.magic,
                               'skill': self.character.skill,
                               'speed': self.character.speed,
                               'luck': self.character.luck,
                               'defense': self.character.defense,
                               'resistance': self.character.resistance,
                               }
        if 'name' in self.script:
            self.name = self.script['name']
        if 'type' in self.script:
            self.type = self.script['type']
        if 'hp' in self.script:
            self.modified_stats['hp'] = self.calculate_stat('hp')
        if 'attack' in self.script:
            self.modified_stats['attack'] = self.calculate_stat('attack')
        if 'magic' in self.script:
            self.modified_stats['magic'] = self.calculate_stat('magic')
        if 'skill' in self.script:
            self.modified_stats['skill'] = self.calculate_stat('skill')
        if 'speed' in self.script:
            self.modified_stats['speed'] = self.calculate_stat('speed')
        if 'luck' in self.script:
            self.modified_stats['luck'] = self.calculate_stat('luck')
        if 'defense' in self.script:
            self.modified_stats['defense'] = self.calculate_stat('defense')
        if 'resistance' in self.script:
            self.modified_stats['resistance'] = self.calculate_stat('resistance')
        if 'turns' in self.script:
            if self.script['turns'] == 'manual':
                self.manual = self.script['manual']
            else:
                self.max_turns = self.script['turns'] + self.turn
        if 'mask' in self.script:
            self.mask = self.script['mask']
        if 'DoT' in self.script:
            self.dot = self.script['DoT']
        if 'DoT_type' in self.script:
            self.dot_type = self.script['DoT_type']
        if 'icon' in self.script:
            self.icon = self.script['icon']
        if 'removes_buff' in self.script:
            self.removes_buff = True
            for index in range(len(self.script['removes_buff'])):
                self.buff_removal_list.append(self.script['removes_buff'][index])
        if 'animation' in self.script:
            self.animation = self.script['animation']

        #Visuals
        if self.name == 'Poison':
            self.opening_animation = animations.poison(self.character)

    def calculate_stat(self, name):
        stat = self.script[name]['num']
        math_type = self.script[name]['math_type']
        if math_type == 'percent':
            return (stat * self.stats[name]) + self.stats[name]
        if math_type == 'flat':
            return stat + self.stats[name]

    def opening_visuals(self):
        if self.opening_animation.done == False:
            self.opening_animation.play()
        else:
            self.opening_animation_done = True
            
    def use(self):
        if self.opening_animation != None:
            self.opening_visuals()
        else:
            self.opening_animation_done = True
            self.character.buff_wait = False
        if self.opening_animation_done == True:
            if self.animation != None:
                self.animation.play()
            if self.character.turn <= self.max_turns or (self.manual == True and self.done == False):
                if self.mask != None:
                    self.character.mask_on = True
                    self.character.mask_name = self.name
                self.update_stats()
            if self.type == 'DoT':
                if self.dot_type == 'magic':
                    if self.character.turn == self.turn + 1:
                        self.magic_damage_calculation()
                        self.turn += 1
                        self.dot_done = True
                    if self.dot_done == True:
                        if self.text_animation != None:
                            self.text_animation.play()
                            if self.text_animation.done == True:
                                self.dot_done = False

            if self.character.turn > self.max_turns or self.done == True:
                self.restore_original_stats()
                self.done = True

    def display_icons(self):
        if self.icon != None:
            if self.opening_animation_done == True:
                x = self.character.battle_rect.x + (self.character.battle_rect.width/2.95)
                y = self.character.battle_rect.y - (self.character.battle_rect.height/3.1)
                self.screen.blit(self.icon, (x, y))

    def update_stats(self):
        self.character.hp = self.modified_stats['hp']
        self.character.strength = self.modified_stats['strength']
        self.character.magic = self.modified_stats['magic']
        self.character.skill = self.modified_stats['skill']
        self.character.speed = self.modified_stats['speed']
        self.character.luck = self.modified_stats['luck']
        self.character.defense = self.modified_stats['defense']
        self.character.resistance = self.modified_stats['resistance']

    def restore_original_stats(self):
        self.character.hp = self.stats['hp']
        self.character.strength = self.stats['strength']
        self.character.magic = self.stats['magic']
        self.character.skill = self.stats['skill']
        self.character.speed = self.stats['speed']
        self.character.luck = self.stats['luck']
        self.character.defense = self.stats['defense']
        self.character.resistance = self.stats['resistance']

    def magic_damage_calculation(self):
        scaling_damage = (self.dot * (self.user.magic/2) * self.user.level) / 32
        total_damage = (self.dot * 1.5) + scaling_damage
        total_damage = round(total_damage * (random.randint(224,255)/256) + 1)

        total_damage -= self.character.resistance
        if total_damage < 0:
            total_damage = 0
        self.character.current_hp -= total_damage
        self.damage_text = str(total_damage)
        self.text_animation = animations.bounce_text(self.damage_text, self.character)