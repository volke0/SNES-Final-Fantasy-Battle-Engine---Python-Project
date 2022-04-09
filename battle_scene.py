import pygame as pg 
import setup, bars, players, utils, animations, abilities
import battle_system as b 
import random
import os
from vars import *

class BattleScene:
    def __init__(self):
        self.bg_gfx = setup.BG_GFX
        self.scale = 2
        self.screen = setup.screen

        #Graphics
        self.background_dict = utils.create_background_dict('b1', self.bg_gfx, 8, 4, self.scale)
        self.battle_window = setup.UI_GFX['battle_menu']
        self.ability_window = setup.UI_GFX['equipbox']
        self.item_window = setup.UI_GFX['magic_menu']
        self.blue_cover = setup.UI_GFX['blue_cover']

        #Rectangles
        self.ability_rect = self.ability_window.get_rect()

        #Coordinates
        self.border = self.scale * -24, self.scale * -16
        self.bg_coord = (-34 * self.scale) + self.border[0], self.border[1] - 20
        self.bw_coord = (0, 444)
        self.aw_coord = (130, 444)
        self.ab_coord = [625, 458]

        #Cursor Variables
        self.cursor_on = False
        self.cursor_switch_mode = False

        #Menu Variables
        self.menu_options = {}
        self.target_options = {}
        self.enemy_target_options = {}
        self.max_action_counter = MAX_ACTION_VALUE
        self.battle_menu = False
        self.item_menu = False
        self.attack_mode = False
        self.buff_index = 0

        #Sounds 
        self.cursor_click = setup.SFX['click']
        self.ready_sound = setup.SFX['ready_sound']
        self.cant_click = setup.SFX['cantclick']

        #Music
        pg.mixer.music.load(os.path.join('resources', 'music', 'ff6_battle_theme.ogg'))
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.55)
        self.victory_music_on = False

        #Player Variables
        self.party = players.player_party_list
        self.character_index = 0
        self.character = self.party[self.character_index]

        self.start_1 = [600, 160]
        self.player_index = 0
        
        #Enemy Variables
        self.enemy_list = players.enemy_list
        self.enemy_formation = [self.enemy_list[0]]
        self.enemy = self.enemy_formation[0]
        self.enemy_spacing = [100, 150]
        self.enemy_start1 = [200, 150]
        self.enemy_index = 0

        #Battle Variables
        self.enter_battle = True
        self.mode = 'game'
        self.ready_queue = {}
        self.rdy_q_index = 0
        self.q_rdy = False
        self.battle_q_rdy = False
        self.battle_ready = False
        self.battle_won = False
        self.turn_counter = 0
        self.flash_special_bar = False

        self.queue = {}
        self.battle_queue = []
        self.counter = 0
        self.select_mode = 'menu'
        self.target = None
        self.battle_done = False
        self.all_units = [self.party, self.enemy_formation]
        self.character_select_mode = False
        self.queue_popped = False
        self.want_to_pop = False

        #Time Variables 
        self.current_time = 0
        self.battle_timer = 4000 # 1 secs(s)
        self.queue_timer = 500 # 0.5 sec(s)

        #Setup functions
        self.set_mode() # Sets up the mode to battle mode for each character in the player's party
        self.setup_players()
        self.setup_enemies()
        self.test_counter = 0

        #Animations
        self.cursor = animations.cursor('battle')
        self.character_pointer = None
        #self.resolve_animation = animations.resolve(self.character)
        self.fade = animations.fade
        self.fade_in = True

    def update(self):
        if self.mode == 'game':
            self.update_target_dict()
            self.timers(1000, 500)
            self.check_battle_won()

    def input(self, inputStream):
        if self.mode == 'game':
            if self.cursor_on == True:
                self.cursor.update_battle(inputStream, self.target_options, self.enemy_formation, self.party, self.character)

    def draw(self, screen):
        screen.fill(BLACK)
        screen.blit(self.background_dict['forest1'][0], self.bg_coord)
        screen.blit(self.battle_window, self.bw_coord)
        if self.mode == 'debug':
            self.debug_mode()
        if self.mode == 'game':
            self.game_mode(screen)

    def set_mode(self):
        for member in self.party:
            member.setup_animation('battle')

    def debug_mode(self):
        self.character = self.party[self.character_index]
        self.character.draw(35)
        self.enemy.draw()
        if self.character.entrance.done == True:
            #self.resolve_animation.play()
            pass

    def game_mode(self, screen):
        self.draw_battlers(screen)
        self.draw_battle()

        if self.battle_won == True:
            #utils.drawText(self.screen, 'YOU WON!', 300, 300)
            pass

    def draw_battlers(self, screen):
        #Draw the enemies
        for enemy in range(len(self.enemy_formation)):
            self.enemy = self.enemy_formation[enemy]
            self.enemy.draw()

            #Update Player and Enemy lists in the character object
            self.enemy.player_list = self.party
            self.enemy.enemy_list = self.enemy_formation
            utils.drawText(screen, f'{self.enemy.ingame_name}', 20, 458, font_size=15)

            if self.enemy.entrance.done == True:
                self.update_status(self.enemy, screen, enemy)

        #Draw the playable characters 
        for member in range(len(self.party)):
            #Text Setup
            text_spacing = 35 * member

            #Setting up the selected character from the party 
            self.character = self.party[member]
            max_hp = self.character.hp
            current_hp = self.character.current_hp
            
            self.character.draw(text_spacing)

            #Update Player and Enemy lists in the character object
            self.character.player_list = self.party
            self.character.enemy_list = self.enemy_formation

            name_text_coord = [330, (458 + text_spacing)]
            hp_text_coord = [505, (458 + text_spacing)]
            utils.drawText(screen, self.character.ingame_name, name_text_coord[0], name_text_coord[1], font_size=22)
            utils.drawText(screen, f'{current_hp} / {max_hp}', hp_text_coord[0], hp_text_coord[1], font_size=22)
            self.character.action_bar.draw(screen, self.character.action_counter, 150, 15)
            self.character.special_bar.draw(screen, self.character.special_gauge, 150, 5, RED, flash_color=RED)

            if self.character.entrance.done == True:
                self.update_status(self.character, screen)

        #Update buffs on all characters
        self.update_buffs()

    def draw_battle(self):
        if self.battle_q_rdy == True:
            if len(self.battle_queue) > 0:
                if self.battle_won == False:
                    if self.battle_queue[0].character.is_dead == True:
                        self.battle_status()
                    elif self.battle_queue[0].character.is_dead == False:
                        if self.battle_queue[0].character.buff_wait == False:
                            self.battle_queue[0].fight()
                        if self.battle_queue[0].battle_done == True:
                            self.battle_status()

    def update_status(self, character, screen, index=0):
        self.update_action_counter(character)
        self.update_special_guage(character)
        self.update_character_animations(character)
        self.win_con()
        #print(self.target_options)
        if character.current_hp <= 0:
            character.is_dead = True
            if character.playable_character == False:
                if character.dead.done == True and character.deleted == False:
                    character.deleted = True
                    self.enemy_formation.pop(index)
        if self.battle_won == False:
            self.check_characters(character, screen)
            
    def update_action_counter(self, character):
        if character.is_dead == False:
            if character.action_counter < self.max_action_counter:
                formula = ((65 * (character.speed + 20)) / 22)
                character.action_counter = character.action_counter + formula
            if character.action_counter >= self.max_action_counter:
                character.ready = True
            else:
                character.ready = False

    def update_special_guage(self, character):
        if character.playable_character == True:
            if character.special_gauge >= character.max_special_gauge:
                pass

    def update_queue(self, character):
        if self.q_rdy == True:
            self.ready_queue.update({character.ingame_name: character})
            ready_list = list(self.ready_queue.keys())
            if self.rdy_q_index >= len(self.ready_queue):
                self.rdy_q_index = len(self.ready_queue) - 1
            name = ready_list[self.rdy_q_index]
            if character.waiting == False:
                self.queue.update({name: self.ready_queue[name]})

    def generate_menu(self, screen):
        self.cursor_handler()
        self.character_pointer.play()

    def pop_queue(self, character):
        if character.ingame_name in self.queue:
            self.queue.pop(character.ingame_name)
            self.cursor_on = False
            self.rdy_q_index = (self.rdy_q_index + 1) % len(self.ready_queue)
            self.cursor.reset()
            self.attack_mode = False
            self.select_mode = 'menu'

    def pop_ready_queue(self, character):
        if character.ingame_name in self.ready_queue:
            self.ready_queue.pop(character.ingame_name)

    def generate_target_dict(self):
        count = 0
        self.all_units = [self.party, self.enemy_formation]
        for index in range(len(self.all_units)):
            for option in range(len(self.all_units[index])):
                self.target_options.update({count: self.all_units[index][option]})
                count += 1
        #Check for the first enemy in the target options
        for index in range(len(self.target_options)):
            if self.target_options[index].playable_character == False:
                self.enemy_index = index 
                break
        #Check for the first player in the target options
        for index in range(len(self.target_options)):
            if self.target_options[index].playable_character == True:
                self.player_index = index 
                break

    def timers(self, battle_time, queue_time):
        self.current_time = pg.time.get_ticks()
        if self.current_time >= self.battle_timer:
            self.battle_q_rdy = True
        if self.battle_q_rdy == True:
            self.battle_timer = self.current_time + battle_time
        if self.current_time >= self.queue_timer:
            self.q_rdy = True
        if self.q_rdy == True:
            self.queue_timer = self.current_time + queue_time
        # print(f'current timer: {self.current_time}')
        # print(f'battle timer: {self.battle_timer}')
    
    def update_character_animations(self, character):
        if character.playable_character == True:
            if character.waiting == True and character.fighting == False and self.battle_won == False:                    
                if character.using_magic == True:
                    character.magic_wait.play()
                else:
                    character.melee_wait.play()
            elif character.is_dead == True and self.battle_won == False:
                character.dead.play()
            elif character.current_hp <= round(character.hp * .30) and character.is_dead == False:
                if character.fighting == False:
                    character.low_hp.play()
            elif self.battle_won == True:
                character.victory_dance.play()
            else:
                if character.fighting == False:
                    character.stand.play()
        else:
            if character.is_dead == True:
                character.dead.play()
    
    def battle_status(self):
        if self.battle_queue[0].character.playable_character == True:
            self.pop_ready_queue(self.battle_queue[0].character)
        self.battle_queue.pop(0)
        self.battle_q_rdy = False

    def update_target_dict(self):
        self.generate_target_dict()
        for index in range(len(self.target_options)):
            if self.target_options[index].playable_character == False:
                enemy = self.target_options[index]
                if enemy.deleted == True:
                    self.target_options.pop(index)

    def cursor_handler(self):
        if self.cursor_on == False:
            self.cursor.reset()
            self.ready_sound.play()
            self.character_pointer = animations.pointer(self.character)
            if self.enemy_index in self.target_options:
                self.cursor.first_enemy = self.enemy_index
        self.cursor_on = True

        if self.cursor.switch_character == True:
            self.want_to_pop = True

        if self.cursor.selected_target == True:
            if self.cursor.target_selection != None:
                if self.character.waiting == False:
                    target = self.cursor.target_selection
                    if self.cursor.menu_selection == 'Attack':
                        if target is not self.character:
                            self.character.waiting = True
                            self.battle_queue.append(b.BattleSystem(self.cursor.menu_selection, self.character, self.cursor.target_selection))
                    if self.cursor.menu_selection == 'Items':
                        if self.cursor.item_selection.revive == True:
                            for index in range(len(self.cursor.target_selection)):
                                if self.cursor.target_selection[index].is_dead == True:
                                    self.character.waiting = True
                                    abilities.player_inventory.use_item(self.cursor.item_selection)
                                    self.battle_queue.append(b.BattleSystem(self.cursor.menu_selection, self.character, self.cursor.target_selection, self.cursor.item_selection))
                                else:
                                    self.cursor.back = True
                                    self.cant_click.play()
                        else:
                            self.character.waiting = True
                            abilities.player_inventory.use_item(self.cursor.item_selection)
                            self.battle_queue.append(b.BattleSystem(self.cursor.menu_selection, self.character, self.cursor.target_selection, item=self.cursor.item_selection))
                    if self.cursor.menu_selection == 'Magic':
                        self.character.waiting = True
                        self.character.using_magic = True
                        magic = []
                        for index in range(len(self.cursor.target_selection)):
                            magic.append(abilities.make_master_item_list(abilities.magic_list, name=self.cursor.magic_selection, character=self.character, target=self.cursor.target_selection[index], real_magic=True))
                        self.battle_queue.append(b.BattleSystem(self.cursor.menu_selection, self.character, self.cursor.target_selection, magic=magic))

                    if self.cursor.menu_selection == 'Special':
                        self.character.waiting = True
                        self.battle_queue.append(b.BattleSystem(self.cursor.menu_selection, self.character, self.cursor.target_selection, special=self.cursor.specials_selection))

        if self.cursor.item_mode == True or self.cursor.magic_mode == True or self.cursor.specials_mode == True:
            self.screen.blit(self.item_window, self.bw_coord)

        self.cursor.generate_menu()
        self.cursor.play()

    def win_con(self):
        if len(self.enemy_formation) <= 0:
            self.battle_won = True

    def check_characters(self, character, screen):
        if character.playable_character == True:
            if character.ready == True and character.is_dead == False:
                self.update_queue(character)
            if len(self.queue) > 0:
                for character in self.queue:
                    self.character = self.queue[character]
                    if self.character.waiting == False: 
                        if self.character.is_dead == False:
                            screen.blit(self.ability_window, self.aw_coord)
                            self.battle_menu = True
                            self.generate_menu(screen)
                        else:
                            self.want_to_pop = True
            if self.character.waiting == True or self.want_to_pop == True:
                self.pop_queue(self.character)
                self.want_to_pop = False
        else:
            if character.ready == True and character.is_dead == False:
                if character.waiting == False:
                    self.enemy = character
                    self.enemy.battle_AI(self.party)
                    if self.enemy.ai.done == True:
                        # print(self.enemy.ai.choice)
                        self.battle_queue.append(b.BattleSystem(self.enemy.ai.choice, self.enemy, self.enemy.ai.target_choice, magic=self.enemy.ai.magic))
                        self.enemy.waiting = True

    def setup_players(self):
        for member in range(len(self.party)):
            self.character = self.party[member]
            spacing = [(30 * member), (50 * member)]
            start = [self.start_1[0] + spacing[0], self.start_1[1] + spacing[1]]
            self.character.set_start(start)
            self.character.enter_battle = False

    def setup_enemies(self):
        for member in range(len(self.enemy_formation)):
            self.enemy = self.enemy_formation[member]
            self.enemy.set_start(self.enemy_start1)
            self.enemy.enter_battle = False

    def check_battle_won(self):
        if self.battle_won == True:
            self.cursor.battle_won = True
            if self.victory_music_on == False:
                pg.mixer.music.unload()
                pg.mixer.music.load(os.path.join('resources', 'music', 'ff6_victory.ogg'))
                pg.mixer.music.play(-1)
                pg.mixer.music.set_volume(0.85)
                self.victory_music_on = True

    def update_buffs(self):
        for _, character in self.target_options.items():
            if len(character.buffs) != 0:
                self.display_buffs(character)
                for _, buff in character.buffs.items():
                    if buff.done == False:
                        if buff.opening_animation_done == False:
                            character.buff_wait = True
                        else:
                            character.buff_wait = False
                        buff.use()
                        # print(f'turn: {buff.character.turn}')
                        # print(f'max turns: {buff.max_turns}')
                    elif buff.done == True:
                        break
                if buff.done == True:
                    character.mask_on = False
                    character.buffs.pop(buff.name)

    def display_buffs(self, character):
        keys_list = list(character.buffs.keys())
        index_list = list(character.buffs.values())
        icon_key_list =  []
        for index in range(len(index_list)):
            if index_list[index].icon != None:
                icon_key_list.append(index_list[index])
        if character.icon_index >= (len(character.buffs)):
            character.icon_index = 0
        key = keys_list[character.icon_index]
        if character.buffs[key].icon != None:
            if character.buffs[key].fps > character.buffs[key].timer or len(icon_key_list) == 1:
                if character.playable_character == True:
                    if character.fighting == False:
                        character.buffs[key].display_icons()
                        character.buffs[key].timer += 1
                else:
                    character.buffs[key].display_icons()
                    character.buffs[key].timer += 1
            else:
                character.buffs[key].timer = 0
                character.icon_index += 1
        else:
            character.icon_index += 1
