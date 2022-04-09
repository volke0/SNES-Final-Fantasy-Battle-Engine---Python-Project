import pygame as pg 
import copy
import setup, utils, abilities
from vars import *

class BattleAnimationSystem:
    def __init__(self, script, character=None, target=None, repeat=False):
        self.script = script 
        self.character = character
        self.target = target
        self.repeat = repeat
        self.mode = None
        self.screen = setup.screen
        self.index = 1
        self.max_index = len(self.script) - 1

        self.animation = None
        self.action = None
        self.frame = None
        self.dx = 0
        self.dy = 0
        self.speed_x = None
        self.speed_y = None
        self.fps = None
        self.alpha = 255
        self.flag_1 = False
        self.alpha_goal = None
        self.sfx = None 
        self.center_on_screen = False
        self.on_character = False
        self.on_target = False
        self.rect_center = False

        self.x = None
        self.y = None
        self.battle_rect = None
        self.rect = None
        self.set_alpha = True
        self.no_repeat = False
        self.fixed_location = False
        self.fast_rumble_on = False
        self.frame_2 = None
        self.frame_3 = None
        self.dx_2 = 0
        self.dy_2 = 0
        self.dx_3 = 0
        self.dy_3 = 0
        self.animation_2 = None
        self.animation_3 = None
        self.animation_4 = None
        self.animation_2_unique = False
        self.play_animation = False
        self.blend_mode = 0

        #Mask Variables
        self.mask = None
        self.m_x = 0
        self.m_y = 0
        self.m_alpha = 255
        self.m_fps = 0
        self.set_m_alpha = True

        #Logic Variables
        self.start_repeat = False
        self.enemy_mode = False
        self.done_loading = False
        self.no_reset_animation_2 = False
        self.fixed_location_done = False
        self.skip_index = False
        self.timer_done = False
        self.timer = 0
        self.timer2 = 0
        self.semi_done = False
        self.done_x = False
        self.done_y = False
        self.sfx_timer = 2
        self.sfx_done = False
        self.done_moving = False
        self.done = False
        self.update_on = False
        self.initialize_meta_data = True
        self.semi_goal = 0
        self.setup_meta_data()
        self.initialize_variables()

    def next_index_sfx(self):
        self.sfx_done = False
        self.timer = 0
        self.frame_2 = None
        self.frame_3 = None
        self.timer_done = False
        self.index += 1

    def next_index_unit(self):
        self.timer = 0
        self.timer_done = False
        self.done_x = False
        self.done_y = False
        self.done_moving = False
        self.index += 1
        self.sfx_done = False
        self.fixed_location = False

    def play_other_animations(self):
        if self.play_animation == True:
            if self.animation_2.done == False:
                self.animation_2.play()
            if self.animation_3 != None:
                self.animation_3.play()
                if self.animation_2.done == True and self.animation_3.done == True and self.animation_4 == None:
                    self.timer_done = True
            if self.animation_4 != None:
                self.animation_4.play()
                if self.animation_2.done == True and self.animation_3.done == True and self.animation_4.done == True:
                    self.timer_done = True
            if self.animation_2.done == True and self.animation_3 == None:
                self.timer_done = True
        
    def play(self):
        if self.mode == 'unit':
            if self.timer_done == True and self.done_moving == True and self.done == False:
                self.next_index_unit()
        if self.mode == 'special_fx': 
            if self.timer_done == True and self.done == False:
                self.next_index_sfx()
        self.initialize_variables()
        self.play_other_animations()
        if self.skip_index == False:
            if self.mode == 'unit':
                self.unit_mode()
            if self.mode == 'special_fx':
                self.special_fx_mode()
            if self.timer >= self.fps:
                if self.flag_1 != True:
                    if self.animation_2 == None:
                        if self.animation_3 == None:
                            if self.animation_4 == None:
                                self.timer_done = True
                    if self.animation_2_unique == True:
                        self.timer_done = True
                    if self.no_reset_animation_2 == True:
                        self.timer_done = True
            if self.timer2 >= self.semi_goal:
                self.semi_done = True

            if self.sfx != None and self.done == False:
                if self.sfx_done == False:
                    self.sfx_timer = 2
                    self.sfx.play()
                    self.sfx_done = True

            if self.sfx_timer > 0:
                self.sfx_timer -= 1
            
            if self.timer_done == False:
                self.timer += 1

            if self.semi_done == False:
                self.timer2 += 1

            if self.flag_1 == True:
                if self.fps > 0:
                    if self.alpha < self.alpha_goal:
                        self.alpha += self.fps 
                    if self.alpha >= self.alpha_goal:
                        self.alpha += 0
                        self.m_alpha += 0  
                        self.timer_done = True
                        if self.character != None:
                            self.character.mask_on = False
                    else:
                        if self.m_fps > 0:
                            self.m_alpha += self.m_fps
                elif self.fps < 0:
                    if self.alpha > self.alpha_goal:
                        self.alpha += self.fps 
                    if self.alpha <= self.alpha_goal:
                        self.alpha += 0
                        self.m_alpha += 0 
                        self.timer_done = True
                        if self.character != None:
                            self.character.mask_on = False
                    else:
                        if self.m_fps < 0:
                            self.m_alpha += self.m_fps

            if self.index >= self.max_index:
                if self.repeat == False and self.timer_done == True:
                    if self.mode == 'unit':
                        if self.done_moving == True:
                            self.index = self.max_index
                            self.done = True
                    if self.mode == 'special_fx':
                        self.index = self.max_index
                        self.done = True
                elif self.repeat == True and self.timer_done == True:
                    self.sfx = None
                    self.index = 0
                    self.sfx_timer = 3
                    self.start_repeat = True

            if self.animation_2_unique == False:
                if self.animation_2 != None and self.animation_2.done == True:
                    if self.no_reset_animation_2 == False:
                        self.animation_2.reset()
                        self.play_animation = False   

    def reset(self):
        if self.done == True:
            self.done = False
            self.timer = 0
            self.timer_done = False
            self.done_x = False
            self.done_y = False
            self.done_moving = False
            self.fixed_location = False
            self.sfx_done = False
            self.frame_2 = None
            self.frame_3 = None
            self.play_animation = False
            if self.character != None:
                self.character.mask_on = False
            if self.animation_2_unique == False:
                if self.animation_2 != None:
                    self.animation_2.reset()
                if self.animation_3 != None:
                    self.animation_3.reset()
                if self.animation_4 != None:
                    self.animation_4.reset()
            self.index = 1

    def skip(self):
        if self.no_repeat == True and self.start_repeat == True:
            self.skip_index = True

    def skip_reset(self):
        if self.skip_index == True and self.no_repeat == True:
            self.index += 1
            self.timer = 0
            self.skip_index = False
            self.play()

    def update(self, character, target=None, dx=None, dy=None, fps=None):
        self.update_on = True
        self.character = character
        self.target = target
        if dx != None:
            self.dx = dx 
        if dy != None:
            self.dy = dy
        if fps != None:
            self.fps = fps

    def setup_meta_data(self):
        self.meta_data = self.script[0]
        self.mode = self.meta_data['mode']
        if self.initialize_meta_data == True:
            if 'character' in self.meta_data:
                self.character = self.meta_data['character']
            if 'target' in self.meta_data:
                self.target = self.meta_data['target']
            if 'animation' in self.meta_data:
                self.animation = self.meta_data['animation']
            if 'fast_rumble' in self.meta_data:
                self.fast_rumble_on = self.meta_data['fast_rumble']
            if 'semi_goal' in self.meta_data:
                self.semi_goal = self.meta_data['semi_goal']
            if 'enemy_mode' in self.meta_data:
                self.enemy_mode = self.meta_data['enemy_mode']
            self.initialize_meta_data = False

    def initialize_variables(self):
        self.index_dict = self.script[self.index]
        if 'no_repeat' in self.index_dict:
            self.no_repeat = self.index_dict['no_repeat']
            self.skip()
        else:
            self.no_repeat = False
        if 'character' in self.index_dict:
            self.character = self.index_dict['character']
        if 'action' in self.index_dict:
            if self.character.playable_character == True:
                self.action = str(self.index_dict['action'])
            else:
                self.action = self.index_dict['action']
        if 'frame' in self.index_dict:
            self.frame = self.index_dict['frame']
        if 'x' in self.index_dict:
            self.dx = self.index_dict['x']
        if 'y' in self.index_dict:
            self.dy = self.index_dict['y']
        if 'speed_x' in self.index_dict:
            self.speed_x = self.index_dict['speed_x']
        if 'speed_y' in self.index_dict:
            self.speed_y = self.index_dict['speed_y']
        if 'fps' in self.index_dict:
            self.fps = self.index_dict['fps']   
        if 'flag_1' in self.index_dict:
            self.flag_1 = self.index_dict['flag_1']
        if 'alpha' in self.index_dict:
            if self.flag_1 == True:
                if self.set_alpha == True:
                    self.alpha = self.index_dict['alpha']
                    self.set_alpha = False
            else:
                self.alpha = self.index_dict['alpha']
        if 'alpha_pts' in self.index_dict:
            self.alpha_goal = self.index_dict['alpha_pts']
        if 'sfx' in self.index_dict:
            self.sfx = self.index_dict['sfx']
        else:
            self.sfx = None
        if 'sfx_volume' in self.index_dict:
            self.sfx.set_volume(self.index_dict['sfx_volume'])
        if 'center_on_screen' in self.index_dict:
            self.center_on_screen = self.index_dict['center_on_screen']
        if 'on_character' in self.index_dict:
            self.on_character = self.index_dict['on_character']
        if 'on_target' in self.index_dict:
            self.on_target = self.index_dict['on_target']
        if 'rect_center' in self.index_dict:
            self.rect_center = self.index_dict['rect_center']
        if 'fixed_location' in self.index_dict:
            self.fixed_location = self.index_dict['fixed_location']
        if self.fixed_location != True:
            self.fixed_location = False
        if 'frame_2' in self.index_dict:
            self.frame_2 = self.index_dict['frame_2']
        if 'x_2' in self.index_dict:
            self.dx_2 = self.index_dict['x_2']
        if 'y_2' in self.index_dict:
            self.dy_2 = self.index_dict['y_2']
        if 'frame_3' in self.index_dict:
            self.frame_3 = self.index_dict['frame_3']
        if 'x_3' in self.index_dict:
            self.dx_3 = self.index_dict['x_3']
        if 'y_3' in self.index_dict:
            self.dy_3 = self.index_dict['y_3']
        if 'play_animation' in self.index_dict:
            self.play_animation = self.index_dict['play_animation']
        if 'animation_2' in self.index_dict:
            self.animation_2 = self.index_dict['animation_2']
        if 'no_reset_animation_2' in self.index_dict:
            if self.index_dict['no_reset_animation_2']:
                self.no_reset_animation_2 = True
        if 'blend_mode' in self.index_dict:
            self.blend_mode = self.index_dict['blend_mode']
        else:
            self.blend_mode = 0
        if 'animation_2_unique' in self.index_dict:
            self.animation_2_unique = self.index_dict['animation_2_unique']
        if 'animation_3' in self.index_dict:
            if self.animation_3 == None:
                self.animation_3 = self.index_dict['animation_3']
        if 'animation_4' in self.index_dict:
            if self.animation_4 == None:
                self.animation_4 = self.index_dict['animation_4']
        if 'cancel_animation4' in self.index_dict:
            if self.index_dict['cancel_animation4'] == True:
                self.animation_4 = None
        if 'mask' in self.index_dict:
            self.mask = self.index_dict['mask']
            if self.set_m_alpha == True:
                self.m_alpha = self.index_dict['m_alpha']
                self.set_m_alpha = False
            self.m_fps = self.index_dict['m_fps']

        if self.skip_index == False:
            if self.mode == 'unit':
                self.battle_rect = self.character.battle_rect
                self.x = self.dx + self.character.start[0]
                self.y = self.dy + self.character.start[1]
                if self.action != None:
                    self.character.action = self.action
                if self.frame != None:
                    self.character.frame = self.frame
                if self.alpha != None:
                    if self.character.playable_character == True:
                        self.character.animation = self.character.player_battle
                        if int(self.character.frame) >= len(self.character.animation[self.action]):
                            self.character.frame = 0
                        self.character.animation[self.character.action][int(self.character.frame)].set_alpha(self.alpha)
                    else:
                        self.character.animation[self.character.action].set_alpha(self.alpha)
            if self.mask != None:
                self.m_x = self.x
                self.m_y = self.y
                self.mask.set_alpha(self.m_alpha)

            if self.mode == 'special_fx':
                if self.on_character == True:
                    try:
                        self.x = self.dx + self.character.battle_rect[0]
                        self.y = self.dy + self.character.battle_rect[1]
                    except AttributeError:
                        print("You have no character loaded!")

                elif self.on_target == True:
                    self.x = self.dx + self.target.battle_rect[0]
                    self.y = self.dy + self.target.battle_rect[1]
                elif self.center_on_screen == True:
                    self.x = self.dx 
                    self.y = self.dy 
                if self.frame != None:
                    if self.rect_center == True:
                        self.rect = self.animation[self.frame].get_rect()
                        self.rect.center = (self.x, self.y)
                    else:
                        if self.action == None:
                            self.rect = self.animation[self.frame].get_rect()
                            self.rect.x = self.x 
                            self.rect.y = self.y 
                        else:
                            self.rect = self.animation[self.action][self.frame].get_rect()
                            self.rect.x = self.x
                            self.rect.y = self.y 
                    if self.action == None:
                        self.animation[self.frame].set_alpha(self.alpha)
                    else:
                        self.animation[self.action][self.frame].set_alpha(self.alpha)
        else:
            self.skip_reset()

    def initialize_other_variables(self, frame, dx, dy, alpha=255):
        animation = None
        if self.animation_2_unique == True:
            animation = self.animation_2
            animation.set_alpha(alpha)
        elif self.animation_2_unique == False:
            animation = self.animation[frame]
        x = dx + self.character.battle_rect[0]
        y = dy + self.character.start[1]

        return animation, x, y

    def unit_mode(self):
        if self.mask != None:
            self.screen.blit(self.mask, (self.m_x, self.m_y))
        if self.fast_rumble_on == False:
            self.normal_move()
        elif self.fast_rumble_on == True:
            self.fast_rumble()
        if self.done_x == True and self.done_y == True:
            self.done_moving = True
        if self.frame == None and self.enemy_mode == False:
            self.character.frame += 0.2

    def special_fx_mode(self):
        if self.mode == 'special_fx':
            if self.frame_2 != None or self.animation_2_unique == True:
                animation2, x2, y2 = self.initialize_other_variables(self.frame_2, self.dx_2, self.dy_2)
                self.screen.blit(animation2, (x2, y2), special_flags=self.blend_mode)

            if self.frame_3 != None:
                animation3, x3, y3 = self.initialize_other_variables(self.frame_3, self.dx_3, self.dy_3)
                self.screen.blit(animation3, (x3, y3), special_flags=self.blend_mode)

            if self.frame != None:
                if self.center_on_screen == True:
                    self.screen.blit(self.animation[self.frame], self.rect, special_flags=self.blend_mode)
                else:
                    if self.action == None:
                        self.screen.blit(self.animation[self.frame], (self.x, self.y), special_flags=self.blend_mode)
                    else:
                        self.screen.blit(self.animation[self.action][self.frame], (self.x, self.y), special_flags=self.blend_mode)
            # if self.mask != None:
            #     animation, x, y = self.initialize_other_variables(self.mask, self.m_x, self.m_y, self.m_alpha)
            #     self.screen.blit(animation, (x, y), special_flags=self.blend_mode)

    def normal_move(self):
        if self.done_x == False:
            if self.fixed_location != True:
                if self.speed_x > 0:
                    if self.battle_rect.x < self.x:
                        self.battle_rect.x += self.speed_x
                    elif self.battle_rect.x >= self.x:
                        self.done_x = True
                elif self.speed_x < 0:
                    if self.battle_rect.x > self.x:
                        self.battle_rect.x += self.speed_x
                    elif self.battle_rect.x <= self.x:
                        self.done_x = True
                elif self.speed_x == 0:
                    self.done_x = True
            elif self.fixed_location == True:
                self.battle_rect.x = self.x
                self.done_x = True

        if self.done_y == False:
            if self.fixed_location != True:
                if self.speed_y > 0:
                    if self.battle_rect.y < self.y:
                        self.battle_rect.y += self.speed_y
                    elif self.battle_rect.y >= self.y:
                        self.done_y = True 
                elif self.speed_y < 0:
                    if self.battle_rect.y > self.y:
                        self.battle_rect.y += self.speed_y
                    elif self.battle_rect.y <= self.y:
                        self.done_y = True
                elif self.speed_y == 0:
                    self.done_y = True
            elif self.fixed_location == True:
                self.battle_rect.y = self.y
                self.done_y = True

    def fast_rumble(self):
        if self.done_x == False:
            if self.fixed_location != True:
                if self.speed_x > 0:
                    if self.battle_rect.x < self.x:
                        self.battle_rect.x += self.speed_x
                    if self.battle_rect.x >= self.x:
                        self.done_x = True
                if self.speed_x < 0:
                    if self.battle_rect.x > self.x:
                        self.battle_rect.x += self.speed_x
                    if self.battle_rect.x <= self.x:
                        self.done_x = True
                if self.speed_x == 0:
                    self.done_x = True
            elif self.fixed_location == True:
                self.battle_rect.x = self.x
                self.done_x = True

        if self.done_y == False:
            if self.fixed_location != True:
                if self.speed_y > 0:
                    if self.battle_rect.y < self.y:
                        self.battle_rect.y += self.speed_y
                    if self.battle_rect.y >= self.y:
                        self.done_y = True 
                if self.speed_y < 0:
                    if self.battle_rect.y > self.y:
                        self.battle_rect.y += self.speed_y
                    if self.battle_rect.y <= self.y:
                        self.done_y = True
                elif self.speed_y == 0:
                    self.done_y = True
            elif self.fixed_location == True:
                self.battle_rect.y = self.y
                self.done_y = True


class CursorSystem:
    def __init__(self, animation, mode='battle'):
        self.screen = setup.screen
        self.animation = animation
        self.mode = mode

        #Input
        self.input_stream = None
        self.update_on = False

        #Sound Effects
        self.select_click = setup.SFX['click']
        self.back_click = setup.SFX['click2']
        self.cant_click = setup.SFX['cantclick']

        #Cursor Variables
        self.direction = 'right'
        self.rect = self.animation[0].get_rect()

        #Character Variables
        self.character = None
        self.first_enemy = 0
        self.first_player = 0
        self.enemy_targets = {}
        self.player_targets = {}
        self.multi_target = False
        self.multi_enemy_targets = False
        self.multi_player_targets = False
        self.target_everyone = False
        self.selected_target = False
        self.switch_character = False

        #Menu Variables
        self.sub_mode = 'menu'
        self.index_x = 0
        self.index_y = 0
        self.temp_index = 0
        self.spacing = 0
        self.item_text_spacing = 0
        self.back = False
        self.aw_coord = (130, 444) #Ability window coordinates
        self.offset = [(self.aw_coord[0] - 40), (self.aw_coord[1] + 12)]
        self.menu_options = {0: ''}
        self.item_options = {0: ''}
        self.magic_options = {0: ''}
        self.special_options = {0: ''}
        self.character_magic_options = {0: ''}
        self.menu_index = 0
        self.item_index = 0 
        self.magic_index = 0
        self.single_mode = False
        self.dual_mode = False
        self.item_options_done = False
        self.use_blue_screen = False

        #Mode Variables
        self.character_mode = False
        self.menu_mode = False
        self.item_mode = False
        self.magic_mode = False
        self.specials_mode = False

        #Selection Variables
        self.selection = None
        self.menu_selection = None
        self.target_selection = None
        self.item_selection = None
        self.magic_selection = None
        self.specials_selection = None

        #Battle Variables
        self.battle_won = False


    def play(self):
        if self.update_on == True:
            if self.direction == 'right':
                animation = self.animation[0]
            else:
                animation = self.animation[1] #Left direction animation
            self.screen.blit(animation, self.rect)

    def generate_menu(self):
        if self.mode == 'battle':
            self.battle_menu()

    def battle_menu(self):
        blue = None
        if self.menu_mode == True:
            for index in range(len(self.menu_options)):
                if isinstance(self.menu_options[index], str):
                    x = self.aw_coord[0] + 20
                    y = self.aw_coord[1] + 10
                    color = WHITE
                    utils.drawText(self.screen, self.menu_options[index], x, y + (index * 32), color=color)
        if self.use_blue_screen == True:
            blue = pg.Surface((501, 144)) #Used to fill the menu portion; this is used so that options don't appear out of the menu box
            blue.fill(BLUE)
            blue_coord = (6, 450)
            self.populate_menu(blue)
            self.screen.blit(blue, blue_coord)

    def populate_menu(self, blue):
        if self.item_mode == True:
            for index in range(len(self.item_options)):
                x = 65
                y = 12 + self.item_text_spacing
                utils.drawText(blue, self.item_options[index], x, y + (index * 32))
            if self.item_index not in abilities.player_inventory.inventory:
                self.item_index = 0
            description = abilities.player_inventory.inventory[self.item_index][0]['description'].split("[.]")
            for index in range(len(description)):
                x = 522
                y = 460 + (index * 32)
                utils.drawText(self.screen, description[index], x, y, font_size=20)
        if self.dual_mode == True:
            option_x = 65
            option_y = 12
            limit = 2
            count = 0
            spacing_y = 0
            options = None
            name = None
            description = None
            cost = None
            current_resource = None
            resource_name = None

            if self.magic_mode == True:
                self.magic_options = abilities.make_master_item_list(abilities.magic_list, character=self.character, target=self.character)
                self.character_magic_options = self.character.magic_list
                options = self.character_magic_options
                if self.magic_options[self.magic_index].name == self.character_magic_options[self.magic_index]:
                    description = self.magic_options[self.magic_index].description.split("[.]")
                    cost = self.magic_options[self.magic_index].mp_cost
                    current_resource = self.character.current_mp
                    resource_name = 'MP'
            if self.specials_mode == True:
                print(self.magic_index)
                self.special_options = self.character.specials_list
                options = self.special_options
                description = self.special_options[self.magic_index].description.split("[.]")
                cost = self.special_options[self.magic_index].sp_cost
                current_resource = self.character.special_gauge
                resource_name = 'SP'
            for index in range(len(options)):
                if count == limit:
                    option_x = 65
                    spacing_y +=1
                    count = 0
                if self.specials_mode == True:
                    name = f'{self.special_options[index].name}'
                if self.magic_mode == True:
                    name = self.character_magic_options[index]
                utils.drawText(blue, name, option_x, (option_y + (spacing_y *32)), font_size=20)
                option_x = 310
                count += 1

            #Drawing description
            if description != None:
                for index in range(len(description)):
                    x = 522
                    y = 490 + (index * 32)
                    utils.drawText(self.screen, description[index], x, y, font_size=20)
            x = 522
            y = 460
            #Drawing Resource Cost Display
            utils.drawText(self.screen, f'{resource_name}: {cost}', x, y, font_size=20)
            utils.drawText(self.screen, f'Current {resource_name}: {current_resource}', (x + 100), y, font_size=20)

    def update_battle(self, inputStream, target_options, enemy_targets, player_targets, character):
        self.update_on = True
        #Update all target information
        self.enemy_targets = enemy_targets
        self.player_targets = player_targets
        self.target_options = target_options
        self.input_stream = inputStream
        #Update character info
        self.character = character
        if self.character != None:
            if self.character.is_dead == False:
                self.update_menu()
                self.battle_cursor_handler()

    def update_menu(self):
        if self.menu_mode == True:
            for option in range(len(self.character.ability_list)):
                self.menu_options.update({option: self.character.ability_list[option]})
            if self.menu_selection == 'Attack':
                if self.sub_mode == 'menu':
                    self.sub_mode = 'target'
                    self.selection = None
                    self.index_y = self.first_enemy
            if self.menu_selection == 'Special':
                self.sub_mode = 'specials'
                self.index_y = 0
                self.index_x = 0
                self.magic_index = 0
            if self.menu_selection == 'Magic':
                self.sub_mode = 'magic'
                self.index_y = 0
                self.index_x = 0
                self.magic_index = 0
            if self.menu_selection == 'Items':
                self.sub_mode = 'item'
                self.index_y = 0
                self.item_index = 0
            #Battle won conditionals
            if self.battle_won == True:
                self.sub_mode = 'battle_won'
        self.back_button_logic()
        self.update_submodes()

    def back_button_logic(self):
        if self.back == True:
            self.direction = 'right'
            self.item_selection = None
            if self.menu_mode == True and self.character_mode == True:
                self.sub_mode = 'menu'
                self.character_mode = False
                self.index_y = self.menu_index
                self.menu_selection = None
                self.multi_player_targets = False
                self.multi_enemy_targets = False
                self.multi_target = False
            if self.item_mode == True and self.character_mode == False:
                self.sub_mode = 'menu'
                self.index_y = self.menu_index
                self.menu_selection = None
            if self.item_mode == True and self.character_mode == True:
                self.sub_mode = 'item'
                self.character_mode = False
                self.index_y = self.item_index

            if self.magic_mode == True and self.character_mode == False:
                self.sub_mode = 'menu'
                self.magic_mode = False
                self.menu_selection = None
            if self.magic_mode == True and self.character_mode == True:
                self.sub_mode = 'magic'
                self.character_mode = False

            if self.specials_mode == True and self.character_mode == False:
                self.sub_mode = 'menu'
                self.specials_mode = False
                self.menu_selection = None
            if self.specials_mode == True and self.character_mode == True:
                self.sub_mode = 'specials'
                self.character_mode = False
                self.multi_player_targets = False
                self.multi_enemy_targets = False
                self.multi_target = False
            self.back = False

    def update_submodes(self):
        if self.sub_mode == 'menu':
            self.menu_mode = True
            self.character_mode = False
            self.specials_mode = False 
            self.magic_mode = False
            self.item_mode = False
            self.single_mode = True
            self.dual_mode = False
            self.use_blue_screen = False
            self.item_options_done = True
        if self.sub_mode == 'target':
            self.character_mode = True
            self.single_mode = True
        if self.sub_mode == 'specials':
            self.specials_mode = True
            self.dual_mode = True
            self.single_mode = False
            self.menu_mode = False
            self.use_blue_screen = True
        if self.sub_mode == 'magic':
            self.magic_mode = True
            self.dual_mode = True
            self.single_mode = False
            self.menu_mode = False
            self.use_blue_screen = True
        if self.sub_mode == 'item':
            self.update_item_list()
            self.item_options_done = False
            self.item_mode = True
            self.single_mode = True
            self.dual_mode = False
            self.menu_mode = False
            self.use_blue_screen = True

    def update_item_list(self):
        for option in range(len(abilities.player_inventory.inventory)):
            if option not in abilities.player_inventory.inventory:
                self.item_options.update({option: ''})
            elif self.item_options_done == True:
                # if len(self.item_options) != len(abilities.player_inventory.inventory):
                #     self.item_options.update({(len(self.item_options)- 1): ''})
                pass
            else:
                item_name = abilities.player_inventory.inventory[option][0]['name']
                amount = abilities.player_inventory.inventory[option][0]['amount']
                self.item_options.update({option: f'{item_name} x{amount}'})

    def battle_cursor_handler(self):
        self.mini_reset()
        options = self.option_select()
        self.single_window_menu_mode(options)
        self.dual_window_menu_mode(options)
        self.command_handler(options)

    def command_handler(self, options):
        #Keyboard Commands
        key = None
        if self.input_stream.keyboard.isKeyPressed(pg.K_RIGHT):
            key = 'right'
        elif self.input_stream.keyboard.isKeyPressed(pg.K_LEFT):
            key = 'left'
        elif self.input_stream.keyboard.isKeyPressed(pg.K_DOWN):
            key = 'down'
        elif self.input_stream.keyboard.isKeyPressed(pg.K_UP):
            key = 'up'
        elif self.input_stream.keyboard.isKeyPressed(pg.K_x):
            key = 'x'
        elif self.input_stream.keyboard.isKeyPressed(pg.K_s):
            key = 's'
        elif self.input_stream.keyboard.isKeyPressed(pg.K_z):
            key = 'z'
        
        if self.mode == 'battle':
            self.battle_commands(key, options)

    #Battle Commands
    def battle_commands(self, key, options):
        if self.battle_won == False:
            self.single_mode_battle_commands(key, options)
            self.dual_mode_battle_commands(key, options)
            #Universal Battle Commmands
            if key == 'x': # Main select button
                if self.sub_mode == 'menu':
                    self.menu_selection = options[self.index_y]
                    self.select_click.play()
                if self.sub_mode == 'target':
                    self.selected_target = True
                    if self.multi_target == True:
                        self.target_selection = options
                    else:
                        self.target_selection =  [options[self.index_y]]
                    self.select_click.play()
                if self.sub_mode == 'item':
                    self.item_selection = abilities.player_inventory.inventory[self.item_index][0]['item']
                    self.sub_mode = 'target'
                    self.index_y = self.first_player
                    self.select_click.play()
                if self.sub_mode == 'magic':
                    if options[self.magic_index].name != self.character_magic_options[self.magic_index]:
                        self.cant_click.play()
                    else:
                        if self.character.stats['current_mp'] < options[self.magic_index].mp_cost:
                            self.cant_click.play()
                        else:
                            self.sub_mode = 'target'
                            self.magic_selection = options[self.magic_index].name
                            if options[self.magic_index].sub_type == 'black':
                                self.index_y = self.first_enemy
                            elif options[self.magic_index].sub_type == 'white':
                                self.index_y = self.first_player
                            elif options[self.magic_index].sub_type == 'buff':
                                self.index_y = self.first_player
                            self.select_click.play()
                if self.sub_mode == 'specials':
                    special = self.special_options[self.magic_index]
                    if self.character.special_gauge >= special.sp_cost:
                        self.sub_mode = 'target'
                        if special.multi_target == True:
                            self.multi_target = True
                            self.index_y = 0
                        if special.target_type == 'enemy':
                            self.multi_enemy_targets = True
                        if special.target_type == 'player':
                            self.multi_player_targets = True
                        else:
                            self.index_y = self.first_enemy
                        self.specials_selection = special
                        self.select_click.play()
            elif key == 'z':
                self.back_click.play()
                if self.sub_mode != 'menu':
                    self.back = True
            elif key == 's':
                self.switch_character = True

                #Unknown purpose at the moment
                if self.sub_mode == 'target':
                    if self.index_y not in self.target_options:
                        self.sub_mode = 'menu'

    #For dual mode commands
    def dual_mode_battle_commands(self, key, options):
        if self.dual_mode == True and self.character_mode == False:
            if key == 'right':
                if self.magic_index % 2 == 0:
                    self.magic_index += 1
                    if self.magic_index >= len(self.magic_options):
                        self.magic_index -= 1
                    else:
                        self.index_x = 1
                        self.temp_index = 1
                else:
                    self.magic_index -= 1
                    self.index_x = 0
                self.select_click.play()
            elif key == 'left':
                if self.magic_index % 2 != 0:
                    self.magic_index -= 1
                    if self.magic_index >= len(self.magic_options):
                        self.magic_index -= 1
                    else:
                        self.index_x = 0
                        self.temp_index = 0
                else:
                    self.magic_index += 1
                    self.index_x = 1
                    if self.magic_index >= len(self.magic_options):
                        self.magic_index -= 1
                        self.index_x = 0
                    self.temp_index = 1
                self.select_click.play()
            elif key == 'up':
                self.index_y = (self.magic_index - 2) % len(options)
                self.magic_index = self.index_y
                if self.index_y % 2 != 0:
                    self.index_y -= 1
                self.select_click.play()
            elif key == 'down':
                if self.index_x == 1:
                    if len(self.magic_options) % 2 != 0:
                        if self.magic_index >= len(self.magic_options) - 2:
                            self.magic_index -= 4
                if self.magic_index >= len(self.magic_options) - 1:
                    if self.index_x == 0:
                        self.magic_index = 0
                        self.index_y = self.magic_index
                else:
                    self.index_y = (self.magic_index + 2) % len(options)
                    self.magic_index = self.index_y
                    if self.index_y % 2 != 0:
                        self.index_y -= 1
                self.select_click.play()

    def single_mode_battle_commands(self, key, options):
        if self.dual_mode == False or self.character_mode == True:
            if key == 'right':
                if self.multi_target == False:
                    if self.character_mode == True:
                        self.index_y = self.first_player
                        self.select_click.play()
            elif key == 'left':
                if self.multi_target == False:
                    if self.character_mode == True:
                        self.index_y = self.first_enemy
                        self.select_click.play()
            elif key == 'up':
                if self.multi_target == False:
                    self.index_y = (self.index_y - 1) % len(options)
                    if options[self.index_y] == '':
                        self.index_y = (self.index_y - 1) % len(options)
                    self.select_click.play()
                    if self.sub_mode == 'item':
                        if self.index_y == len(options) - 1:
                            self.item_text_spacing = -self.index_y * 32
                        else:
                            self.item_text_spacing = -self.index_y * 32
                    self.item_index = self.index_y
            elif key == 'down':
                if self.multi_target == False:
                    self.index_y = (self.index_y + 1) % len(options)
                    if options[self.index_y] == '':
                        self.index_y = (self.index_y + 1) % len(options)
                    self.select_click.play()
                    if self.sub_mode == 'item':
                        if self.index_y == 0:
                            self.item_text_spacing = self.index_y * 32
                        else:
                            self.item_text_spacing = -self.index_y * 32
                        self.item_index = self.index_y

    def single_window_menu_mode(self, options):
        if self.dual_mode == False or self.character_mode == True:
            if self.menu_mode == True and self.character_mode == False:
                self.spacing = 32
                self.direction = 'right'
                self.rect.x = self.offset[0]
                self.rect.y = self.offset[1] + (self.index_y * self.spacing)
            elif self.character_mode == True:
                target = []
                if self.multi_enemy_targets == True:
                    for index in range(len(self.enemy_targets)):
                        target.append(self.enemy_targets[index])
                else:
                    target.append(self.target_options[self.index_y])
                for index in range(len(target)):
                    if target[index].playable_character == True:
                        self.direction = 'right'
                        self.first_player = 0
                        self.rect.x = target[index].battle_rect.x - 40
                        self.rect.y = target[index].battle_rect.y + 50
                    else:
                        self.direction = 'left'
                        if self.multi_enemy_targets == True:
                            self.first_enemy = 0
                        #else the cursor handler on the battle_scene end will determine the first enemy
                        self.rect.x = target[index].battle_rect.x + 90
                        self.rect.y = target[index].battle_rect.y + 50

            elif self.item_mode == True:
                self.rect.x = self.offset[0] - 80
                self.rect.y = (self.offset[1] + 10)

    def dual_window_menu_mode(self, options):
        if self.dual_mode == True and self.single_mode == False:
            self.direction = 'right'
            self.rect.x = (self.offset[0] - 80) + (self.index_x * 245)
            self.rect.y = (self.offset[1] + 7) + (self.index_y * 16)

    def mini_reset(self):
        self.selection = None
        self.target_selection = None
        self.selected_target = False
        self.switch_character = False

    def option_select(self):
        options = None
        if self.menu_mode == True and self.character_mode == False:
            options = self.menu_options
            return options
        elif self.item_mode == True and self.character_mode == False:
            options = self.item_options
            return options
        elif self.magic_mode == True and self.character_mode == False:
            options = self.magic_options
            return options
        elif self.specials_mode == True and self.character_mode == False:
            options = self.special_options
            return options
        elif self.character_mode == True:
            if self.multi_enemy_targets == True:
                options = self.enemy_targets
                return options
            elif self.multi_player_targets == True:
                options = self.player_targets
                return options
            else:
                options = self.target_options
                return options

    def reset(self):
        self.sub_mode = 'menu'
        self.index_y = 0
        self.back = False
        self.selection = None
        self.target_selection = None
        self.menu_selection = None
        self.item_selection = None
        self.magic_selection = None
        self.selected_target = False
        self.menu_options = {0: ''}
        self.first_enemy = 0 
        self.first_player = 0
        self.update_on = False
        self.switch_character = False
        self.magic_mode = False
        self.specials_mode = False
        self.use_blue_screen = False
        self.multi_target = False
        self.multi_enemy_targets = False
        self.multi_player_targets = False

class TextEngine:
    """docstring for TextEngine"""
    def __init__(self, text_script):
        self.text_script = text_script
        self.text = self.text_script['text']
        self.size = self.text_script['size']
        self.x = self.text_script['x']
        self.y = self.text_script['y']
        self.text_x = None
        self.text_y = None
        self.type = self.text_script['type']

        self.fps = 0
        self.align = 'center'

        #Set fps
        if self.type == 'info':
            self.fps = self.text_script['fps']

        self.rect = None
        self.screen = setup.screen

        #Load textbox
        self.textbox = None
        self.dialogue_box = setup.UI_GFX['dialoguebox']
        self.info_box = setup.UI_GFX['info_box']

        if self.type == 'info':
            self.textbox = self.info_box
            self.rect = self.textbox.get_rect()
        else:
            self.textbox = self.dialogue_box
            self.rect = self.textbox.get_rect()

        if self.type == 'dialogue':
            self.text_x = self.text_script['text_x']
            self.text_y = self.text_script['text_y']
        if self.type == 'info':
            self.text_x = 486 / 2
            self.text_y = float(65 / 2)

        #Setup alignment
        if self.type == 'dialogue':
            self.align = 'topleft'
            self.rect.topleft = (self.x, self.y)
        else:
            self.rect.center = (self.x, self.y)

        #Logic Variables
        self.done = False

    def run(self):
        if self.done == False:
            if self.type == 'info':
                width = 486
                height = 65
            blue = pg.Surface((width, height))
            blue.fill(BLUE)
            utils.drawText(blue, self.text, self.text_x, self.text_y, self.align, self.size)
            self.screen.blit(self.textbox, self.rect)
            self.screen.blit(blue, (7 + self.rect.x, 7 + self.rect.y))

            if self.fps > 0:
                self.fps -= 1
            else:
                self.done = True

class Fade:
    def __init__(self, color=BLACK):
        bg = pg.Surface(SCREEN_SIZE)
        bg.set_alpha(255)
        bg.fill(color)
        self.background = bg
        self.screen = setup.screen
        self.alpha = 255
        self.setup_done = False
        self.goal = 0
        self.timer_done = False
        self.in_done = False
        self.out_done = False
        self.fade_in = None

        self.done = False

    def play(self, fade_in, speed=5):
        self.fade_in = fade_in
        if self.fade_in == True:
            self._in(speed)
        elif self.fade_in == False:
            self.out(speed)
        self.background.set_alpha(self.alpha)
        self.screen.blit(self.background, (0, 0))

    def _in(self, speed=5):
        if self.setup_done == False or self.out_done == True:
            self.reset()
            self.alpha = 0
            self.goal = 255
            self.setup_done = True

        if self.in_done == False:
            if self.timer_done == True:
                self.in_done = True
            if self.alpha < self.goal:
                self.alpha += speed
            elif self.alpha >= self.goal:
                self.alpha += 0
                self.timer_done = True

    def out(self, speed=5):
        if self.setup_done == False or self.in_done == True:
            self.reset()
            self.alpha = 255
            self.goal = 0
            self.setup_done = True

        if self.out_done == False:
            if self.timer_done == True:
                self.out_done = True
            if self.alpha > self.goal:
                self.alpha -= speed
            elif self.alpha <= self.goal:
                self.alpha += 0
                self.timer_done = True

    def reset(self):
        self.timer_done = False 
        self.setup_done = False
        self.in_done = False
        self.out_done = False