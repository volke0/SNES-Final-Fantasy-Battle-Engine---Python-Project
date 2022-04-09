import pygame as pg 
import setup, utils, abilities, animations, engines
import random, copy 
from vars import *

class BattleSystem:
    def __init__(self, option, character, target, item=None, magic=None, special=None):
        self.option = option
        self.character = character
        self.target = target
        self.item = item
        self.magic = magic
        self.special = special
        self.last_target = len(self.target)-1

        self.ability_done = False
        self.battle_done = False
        self.screen = character.screen

        #Logic Variables
        self.skip_battle = False

        #Calculation Flags
        self.hit_calculation_done = False
        self.damage_calculation_done = False
        self.hit = []
        self.miss = []
        self.crit = []
        self.hit_done = False
        self.item_done = False
        self.buff_done = False
        self.heal_hp = False
        self.heal_mp = False
        self.revive = False
        self.vfx_enabled = False

        #Calculation Variables
        self.attack_dict = []
        self.hit_rate = 0
        self.dodge_rate = []
        self.hit_chance = []
        self.crit_chance = 0 
        self.base_damage = None
        self.damage = []
        self.heal_amount = 0
        self.mp_cost = 0

        #Text
        self.damage_text = []
        self.miss_text = 'Miss'
        self.text_box = None

        #Animations
        self.weapon_hit = None
        self.weapon_miss = []
        self.weapon_slash_hit = []
        self.damage_animation = []
        self.miss_animation = []
        self.bounce_text = []
        self.white_flash = animations.flash_white_background()
        self.item_animation = None
        self.heal_text = []
        self.magic_use_animation = animations.magic_use(self.character)
        self.heal_use_animation = animations.heal_use(self.character)
        self.weapon_animation = None
 
        #RNG Variables
        self.hit_rng = 0
        self.dmg_rng = None
        self.crit_rng = None

        #Indexing
        self.hit_index = 0
        self.buff_index = 0

        #Initalize Variables
        self.intialize()
       
        hp = self.target[0].current_hp
        #Debugging Stuff
        # print(f'name: {self.character.ingame_name}')
        # print(f'target: {self.target[0].ingame_name}')
        # print(f'hit chance: {self.hit_chance}')
        # # print(f'hp: {hp}')
        # print(f'crit_chance: {self.crit_chance}')
        # print(f'damage: {self.damage}')
    
    def intialize(self):
        self.prepare_special()
        for index in range(len(self.target)):
            target = self.target[index]
            self.miss_animation.append(animations.bounce_text(self.miss_text, target))
            self.initialize_weapon(target, index)
            self.hit_calculation(target, index)
            self.damage_calculation(target, index)
            # print(self.hit)
            # print(self.miss)
            # print(self.dodge_rate)
            # print(self.hit_chance)

    def prepare_special(self):
        if self.special != None:
            self.special.prepare(self.target)

    def use_ability(self, target, index):
        if self.option == 'Attack':
            self.basic_attack(target, index)
        if self.option == 'Items':
            self.text_box.run()
            if self.text_box.done == True:
                self.item_mode(target, index)
        if self.option == 'Magic':
            self.text_box.run()
            if self.text_box.done == True:
                if self.skip_battle == True:
                    if self.character.playable_character == False:
                        self.reset_enemy()
                    else:
                        self.reset_player()
                else:
                    self.magic_mode(target, index)
        if self.option == 'Special':
            self.text_box.run()
            if self.text_box.done == True:
                self.specials_mode()

    def fight(self):
        for index in range(len(self.target)):
            target = self.target[index]
        if self.battle_done == False:
            self.use_ability(target, index)

    def reset_player(self):
        if self.option == 'Items':
            if self.bounce_text.done == True:
                self.player_general_reset()
        else:
            self.player_general_reset()

    def player_general_reset(self):
        self.general_reset()
        if self.character.special_gauge < self.character.max_special_gauge:
            self.character.special_gauge += 1
        else:
            self.character.special_gauge += 0
        if self.special != None:
            self.special.reset()
        self.character.walk_up.reset()
        self.character.weapon_animation.reset()
        self.character.use_item.reset()
        self.character.use_magic.reset()
        self.character.melee_attack.reset()
        self.character.walk_back.reset()
        self.character.fighting = False
        self.character.ready = False
        self.character.waiting = False
        self.character.using_magic = False
        self.character.action_counter = 0
        self.battle_done = True

    def reset_enemy(self):
        self.general_reset()
        self.character.attacking.reset()
        self.character.ready = False
        self.character.waiting = False
        self.character.action_counter = 0
        self.character.ai.reset()
        self.battle_done = True

    def general_reset(self):
        for index in range(len(self.target)):
            self.target[index].damage_calculation_done = False
            self.target[index].hit.reset()
            self.target[index].item_done = False
            self.target[index].buff_done = False
        #Add to the unit's turn counter:
        self.character.turn += 1

    def hit_calculation(self, target, index):
        if self.option == 'Attack' or self.option == 'Magic' or (self.option == 'Special' and self.special.type == 'damage'):
            self.dodge_rate.append(round(((target.luck) + target.avoid), 2))
            self.hit_rate = ((self.character.skill * 2) + (self.character.luck / 2)) + self.character.hit_chance
            if self.special != None:
                self.hit_rate += self.special.hit

            self.hit_chance.append(round(((self.hit_rate - self.dodge_rate[index]))))
            if self.hit_chance[index] > 100:
                self.hit_chance[index] = 100

            self.hit_rng = (round(random.uniform(0, 1), 2)) * 100
            if self.hit_rng <= self.hit_chance[index]:
                self.hit.append(True)
                self.miss.append(False) 
            else:
                self.miss.append(True)
                self.hit.append(False)

    def damage_calculation(self, target, index):
        self.dmg_rng = round(random.uniform(0.75, 1), 2)
        if self.option == 'Attack':
            if self.hit[index] == True:
                damage = self.base_damage
                damage = damage - target.defense
                self.damage.append((damage) * self.dmg_rng)
                self.damage[index] = round(self.damage[index])

                #Calculate if you land a crit or not
                self.crit_chance = (self.character.skill/2) + self.character.crit_chance
                self.crit_rng = round(random.uniform(0, 100), 2)
                if self.crit_rng <= self.crit_chance:
                    self.crit.append(True)
                    self.damage[index] = (round(self.damage[index] * 3))  
                else:
                    self.crit.append(False)
                if self.damage[index] < 0:
                    self.damage[index] = 0   
                self.damage_text.append(str(self.damage[index]))
                self.damage_animation.append(animations.bounce_text(self.damage_text[index], target))
            else:
                self.damage_animation.append(animations.bounce_text('Miss', target))
                self.crit.append(False)
        if self.option == 'Items':
            #Set up textbox
            text_script = {'text': str(self.item.name), 'size': 30, 'type': 'info', 'fps': 45, 'x': SCREEN_WIDTH/2, 'y': 40}
            self.text_box = engines.TextEngine(text_script)
            #Set up item parameters
            if self.item.hp_restore > 0:
                self.heal_hp = True
                self.heal_amount = self.item.hp_restore
            if self.item.mp_restore > 0:
                self.heal_mp = True
                self.heal_amount = self.item.mp_restore
            if self.item.revive == True:
                self.revive = True

            self.base_damage = self.item.hp_cost
            self.mp_cost = self.item.mp_cost
            self.character.current_mp -= self.mp_cost
            self.item_animation, self.bounce_text = abilities.item_use(self.item.name, str(self.heal_amount), self.character, target)
        if self.option == 'Magic':
            #Set up textbox
            if self.character.playable_character == False:
                text_script = None
                if self.character.current_mp < self.magic[0][0].mp_cost:
                    text_script = {'text': "Out of MP!", 'size': 30, 'type': 'info', 'fps': 70, 'x': SCREEN_WIDTH/2, 'y': 40}
                    self.skip_battle = True
                else:
                    text_script = {'text': str(self.magic[0][0].name), 'size': 30, 'type': 'info', 'fps': 45, 'x': SCREEN_WIDTH/2, 'y': 40}
                self.text_box = engines.TextEngine(text_script)
            else:
                text_script = {'text': str(self.magic[0][0].name), 'size': 30, 'type': 'info', 'fps': 45, 'x': SCREEN_WIDTH/2, 'y': 40}
                self.text_box = engines.TextEngine(text_script)
            #Determine what type of magic you are using
            if self.magic[index][0].sub_type == 'black':
                self.mp_cost = self.magic[index][0].mp_cost
                if self.hit[index] == True:
                    self.damage.append(round((self.magic[index][0].total_damage * (255 - target.resistance)/256) + 1))
                    self.damage_text.append(str(self.damage[index]))
                    self.damage_animation.append(animations.bounce_text(self.damage_text[index], target))
                    #Calculate if you land a crit or not
                    self.crit_chance = (self.character.skill/2) + self.character.crit_chance
                    self.crit_rng = round(random.uniform(0, 100), 2)
                    if self.crit_rng <= self.crit_chance:
                        self.crit.append(True)
                        self.damage[index] = (round(self.damage[index] * 3))  
                    else:
                        self.crit.append(False)
                    if self.damage[index] < 0:
                        self.damage[index] = 0
                else:
                    self.damage_animation.append(animations.bounce_text('Miss', target))
                    self.crit.append(False)
                self.mp_calculations()

            if self.magic[index][0].sub_type == 'white':
                if self.magic[index][0].heal_hp == True:
                    self.heal_hp = True
                if self.magic[index][0].heal_mp == True:
                    self.heal_mp = True
                self.heal_amount = round(self.magic[index][0].total_damage)
                self.mp_cost = self.magic[index][0].mp_cost
                self.heal_text.append(str(self.heal_amount))
                self.bounce_text.append(animations.bounce_text(self.heal_text[index], target, color=LIGHT_GREEN))
                self.mp_calculations()

            if self.magic[index][0].sub_type == 'buff':
                self.mp_cost = self.magic[index][0].mp_cost
                self.mp_calculations()

        if self.option == 'Special':
            #Set up textbox
            text_script = {'text': str(self.special.name), 'size': 30, 'type': 'info', 'fps': 45, 'x': SCREEN_WIDTH/2, 'y': 40}
            self.text_box = engines.TextEngine(text_script)
            if self.special.type == 'damage':
                if self.hit[index] == True:
                    if self.special.damage_type == 'magic':
                        self.damage.append((self.special.total_damage - target.resistance) * self.dmg_rng)
                        self.damage[index] = round(self.damage[index])
                    #Calculate if you land a crit or not
                    self.crit_chance = (self.character.skill/2) + self.special.crit_rate + self.character.crit_chance
                    self.crit_rng = round(random.uniform(0, 100), 2)
                    if self.crit_rng <= self.crit_chance:
                        self.crit.append(True)
                        crit_dmg = (self.character.crit_dmg + self.special.crit_dmg)/100
                        print(f'crit_dmg: {crit_dmg}')
                        self.damage[index] = (round(self.damage[index] * crit_dmg)) 
                    else:
                        self.crit.append(False)
                    if self.damage[index] < 0:
                        self.damage[index] = 0   
                    self.damage_text.append(str(self.damage[index]))
                    self.damage_animation.append(animations.bounce_text(self.damage_text[index], target))
                else:
                    self.damage_text.append('Miss')
                    self.damage_animation.append(animations.bounce_text(self.damage_text[index], target))
            if self.special.type == 'white':
                if self.special.heal_hp == True:
                    self.heal_hp = True
                if self.special.heal_mp == True:
                    self.heal_mp = True
                self.heal_amount = round(self.special.total_damage)
                self.heal_text.append(str(self.heal_amount))
                self.bounce_text.append(animations.bounce_text(self.heal_text[index], target, color=LIGHT_GREEN))
            self.character.special_gauge -= self.special.sp_cost

    def mp_calculations(self):
        self.character.current_mp -= self.mp_cost
        if self.character.current_mp <= 0:
            self.character.current_mp = 0

    def initialize_weapon(self, target, index):
        if self.option == 'Attack' or self.special != None:
            if self.character.playable_character == True:
                self.weapon_hit = animations.weapon_swing(self.character)
                self.weapon_animation = self.weapon_hit
                self.weapon_miss.append(animations.weapon_swing_miss(self.character))
            temp1, temp2 = abilities.melee_attack(self.character, target)
            self.weapon_slash_hit.append(temp1)
            self.attack_dict.append(temp2)
            self.base_damage = self.attack_dict[index][0]['base_dmg']

    def hp_calculation(self, target, index):
        if target.damage_calculation_done == False:
            hp = target.current_hp - self.damage[index]
            if hp < 0:
                hp = 0 
            target.current_hp = hp
            target.damage_calculation_done = True 

    def basic_attack(self, target, index):
        if self.character.playable_character == True:
            if self.ability_done == False:
                self.character.fighting = True
                self.character.melee_attack.play()
                if self.character.melee_attack.done == True and self.character.weapon_animation.done == True or self.character.melee_attack.done and self.weapon_miss[index].done == True:
                    self.ability_done = True

            if self.hit[index] == True and self.hit_done == False:
                self.character.weapon_animation.play()
            elif self.miss[index] == True and self.hit_done == False:
                self.weapon_miss[index].play()

            if self.ability_done == True:
                if self.hit[index] == True:
                    self.weapon_slash_hit[index].play()
                    self.target[index].hit.play()
                    if self.target[index].hit.done == True and self.weapon_slash_hit[index].done == True:
                        self.damage_animation[index].play()
                        if self.damage_animation[index].done == True:
                            self.hp_calculation(target, index)
                elif self.miss[index] == True:
                    self.miss_animation[index].play()
                if self.damage_animation[self.last_target].done == True or self.miss_animation[self.last_target].done == True:
                    self.hit_done = True

            if self.hit_done == True:
                self.white_flash.reset()
                self.character.walk_back.play()
                if self.character.walk_back.done == True:
                    self.reset_player()
        else:
            if self.ability_done == False:
                self.character.attacking.play()
                if self.character.attacking.done == True:
                    self.ability_done = True
            if self.ability_done == True:
                if self.hit[index] == True:
                    self.weapon_slash_hit[index].play()
                    self.target[index].hit.play()
                if self.target[index].hit.done == True and self.weapon_slash_hit[index].done == True:
                    self.damage_animation[index].play()
                    if self.damage_animation[index].done == True:
                        self.hp_calculation(target, index)
                elif self.miss[index] == True:
                    self.miss_animation[index].play()
                if self.damage_animation[self.last_target].done == True or self.miss_animation[self.last_target].done == True:
                    self.hit_done = True

                if self.hit_done == True:
                    self.white_flash.reset()
                    self.reset_enemy()
        if self.crit[index] == True:
            self.white_flash.play()
            if self.white_flash.done == True:
                self.crit[index] = False

    def item_mode(self, target, index):
        if self.character.playable_character == True:
            if self.ability_done == False:
                self.character.fighting = True
                self.character.walk_up.play()
                if self.character.walk_up.done == True:
                    self.character.use_item.play()
                    if self.character.use_item.done == True:
                        self.ability_done = True
            if self.ability_done == True:
                self.item_animation.play()
                if self.item_animation.done == True:
                    if target.item_done == False:
                        self.bounce_text.play()
                    if target.item_done == False and self.bounce_text.done == True:
                        self.heal_logic(target)
            if target.item_done == True:
                self.character.walk_back.play()
                if self.character.walk_back.done == True:
                    self.reset_player()

    def magic_mode(self, target, index):
        if self.character.playable_character == True:
            if self.ability_done == False:
                self.character.fighting = True
                self.character.walk_up.play()
                if self.character.walk_up.done == True:
                    self.character.use_magic.play()
                    if self.magic[index][0].sub_type == 'black' or self.magic[index][0].sub_type == 'buff':
                        self.magic_use_animation.play()
                        if self.magic_use_animation.done == True and self.character.use_magic.done == True:
                            self.ability_done = True
                    if self.magic[index][0].sub_type == 'white':
                        self.heal_use_animation.play()
                        if self.heal_use_animation.done == True and self.character.use_magic.done == True:
                            self.ability_done = True
        if self.character.playable_character == False:
            self.ability_done = True

        if self.ability_done == True:
            if self.magic[index][0].sub_type == 'black':
                self.black_magic(target, index)
            if self.magic[index][0].sub_type == 'white':
                self.white_magic(target, index)
            if self.magic[index][0].sub_type == 'buff':
                self.buff('magic', target, index)

    def specials_mode(self):
        if self.ability_done == False:
            self.character.fighting = True
            self.special.play()
        if self.special.animation.done == True:
            if self.special.other_effects == True:
                if self.special.vfx_index <= len(self.special.vfx_animation) - 1:
                    self.vfx_enabled = True
                    for index in range(len(self.special.vfx_animation)):
                        if index == 0:
                            self.special.vfx_animation[index].play()
                        else:
                            if self.special.vfx_animation[index-1].semi_done == True:
                                self.special.vfx_animation[index].play()
                    # self.special.vfx_animation[self.special.vfx_index].play()
                    # if self.special.vfx_animation[self.special.vfx_index].semi_done == True:
                    #     self.special.vfx_index += 1
                    # self.special.timer += 1
                    # if self.special.timer >= self.special.fps:
                    #     self.special.vfx_index += 1
                    #     self.special.timer = 0

        if self.special.type == 'damage':
            if self.hit_done == False:
                if self.hit[self.hit_index] == True:
                    if self.vfx_enabled == True:
                        if self.special.vfx_animation[self.hit_index].done == True:
                            self.apply_damage()
                    else:
                        if self.special.animation.done == True:
                            self.apply_damage()
                else:
                    if self.special.animation.done == True:
                        self.apply_damage()
                if self.damage_animation[self.last_target].done == True:
                    self.hit_done = True
            self.end()
        if self.special.type == 'white':
            if self.item_done == False:
                if self.hit_index <= len(self.target) - 1:
                    if self.vfx_enabled == True:
                        if self.special.vfx_animation[self.hit_index].done == True:
                            self.apply_special_healing()
                    else:
                        if self.special.animation.done == True:
                            self.apply_special_healing()
                if self.bounce_text[self.last_target].done == True:
                    self.item_done = True
            self.end()

    def apply_special_healing(self):
        if self.special.heal_hp == True or self.special.heal_mp == True:
            target = self.target[self.hit_index]
            self.bounce_text[self.hit_index].play()
            if target.item_done == False and self.bounce_text[self.hit_index].done == True:
                self.heal_logic(target)
                self.hit_index += 1

    def apply_damage(self):
        for index in range(len(self.target)):
            if self.hit[index] == True:
                self.damage_animation[index].play()
                if self.damage_animation[index].done == True:
                    target = self.target[index]
                    self.hp_calculation(target, index)
                    self.crit_display(index)
            if self.miss[index] == True:
                self.damage_animation[index].play()
        
    def end(self):
        if self.hit_done == True or self.item_done == True:
            self.ability_done = True
            if len(self.special.buff) > 0:
                for index in range(len(self.target)):
                    target = self.target[index]
                    buff = self.special.buff[index]
                    self.buff_logic(buff, target)
                    index += 1
            self.character.walk_back.play()
            if self.character.walk_back.done == True:
                self.reset_player()

    def crit_display(self, index):
        if self.crit[self.hit_index] == True:
            self.white_flash.play()
            if self.white_flash.done == True:
                self.crit[self.hit_index] = False

    def heal_logic(self, target):
        if self.heal_hp == True:
            if target.is_dead == False or self.revive == True:
                if target.current_hp + self.heal_amount > target.hp:
                    target.current_hp = target.hp
                else:
                    target.current_hp += self.heal_amount
            if self.revive == True:
                target.is_dead = False
                target.waiting = False
                target.ready = False
                target.action_counter = 0
            target.item_done = True

        if self.heal_mp == True:
            if target.is_dead == False:
                if target.current_mp + self.heal_amount > target.mp:
                    target.current_mp = target.mp
                else:
                    target.current_mp += self.heal_amount
            target.item_done = True

    def black_magic(self, target, index):
        if self.hit[index] == True and self.hit_done == False:
            self.magic[index][0].animation.play()
            if self.magic[index][0].animation.done == True:
                self.damage_animation[index].play()
                if self.damage_animation[index].done == True:
                    self.hp_calculation(target, index)
        if self.miss[index] == True and self.hit_done == False:
            self.miss_animation[index].play()
        if self.damage_animation[index].done == True or self.miss_animation[index].done == True:
            self.hit_done = True
        if self.hit_done == True:
            self.white_flash.reset()
            if self.magic[index][0].buff != None and self.hit[index] == True:
                buff = self.magic[index][0].buff 
                self.buff_logic(buff, target)
            if self.character.playable_character == True:
                self.character.walk_back.play()
                if self.character.walk_back.done == True:
                    self.reset_player()
            else:
                self.reset_enemy()

        if self.crit[index] == True:
            self.white_flash.play()
            if self.white_flash.done == True:
                self.crit[index] = False

    def white_magic(self, target, index):
        self.magic[index][0].animation.play()
        if self.magic[index][0].animation.done == True:
            if self.item_done == False and self.buff_done == False:
                if self.magic[index][0].heal_hp == True or self.magic[index][0].heal_mp == True:
                    self.bounce_text[index].play()
                    if target.item_done == False and self.bounce_text[self.last_target].done == True:
                        self.heal_logic(target)
                else:
                    target.item_done = True
                if self.magic[index][0].buff != None:
                    buff = self.magic[index][0].buff
                    self.buff_logic(buff, target)
                else:
                    target.buff_done = True
        if self.target[self.last_target].item_done == True and self.target[self.last_target].buff_done == True:
            self.character.walk_back.play()
            if self.character.walk_back.done == True:
                self.reset_player()

    def buff(self, mode, target, index):
        if mode == 'magic':
            self.magic[index][0].animation.play()
            if self.magic[index][0].animation.done == True:
                if self.item_done == False:
                    buff = self.magic[index][0].buff 
                    self.buff_logic(buff, target)
        if mode == 'special':
            self.special.animation.play()
            if self.item_done == False:
                buff = self.special.buff
                self.buff_logic(buff, target)

        if self.target[self.last_target].buff_done == True:
            self.character.walk_back.play()
            if self.character.walk_back.done == True:
                self.reset_player()

    def buff_logic(self, buff, target):
        if buff.removes_buff == True:
            for index in range(len(buff.buff_removal_list)):
                name = buff.buff_removal_list[index]
                if name in target.buffs:
                    target.buffs[name].done = True
                else:
                    pass
            target.buff_done = True
        else:
            target.buffs.update({buff.name: buff})
            target.buff_done = True

        if self.target[self.last_target].buff_done == True:
            self.buff_done = True