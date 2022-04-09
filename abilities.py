import pygame as pg 
import setup, utils, animations, inventory_system
from vars import *

def melee_attack(character, target):
	hit = None
	var = [{'cost_hp': 0, 'cost_mp': 0, 'base_dmg': character.strength}]
	if character.equipment[0] == 'iron_sword' or character.equipment[0] == 'iron_wand':
		hit = animations.sword_hit(target)
	elif character.equipment[0] == 'iron_dagger':
		hit = animations.dagger_hit(target)
	return hit, var

def item_use(item, text, character, target):
    item_animation = None
    heal_text = None
    if item == 'Potion' or item == 'High Potion' or  item == 'Mega Potion':
        item_animation = animations.potion_use(target)
        heal_text = animations.bounce_text(text, target, color=LIGHT_GREEN, sfx_on=True)
    if item == 'Ether' or item == 'High Ether' or  item == 'Mega Ether':
        item_animation = animations.ether_use(target)
        heal_text = animations.bounce_text(text, target, color=LIGHT_BLUE, sfx_on=True)
    if item == 'Revive':
        item_animation = animations.revive_use(target)
        heal_text = animations.bounce_text(text, target, color=LIGHT_GREEN, sfx_on=True)

    return item_animation, heal_text

def make_master_item_list(item_list, name=None, character=None, target=None, real_magic=False):
    master_list = []
    for index in range(len(item_list)):
        item_script = item_list[index]
        if item_script['type'] == 'potion':
            item = inventory_system.Potion(item_script)
            master_list.append(item)
        if item_script['type'] == 'magic':
            if real_magic == True:
                if name == item_script['name']:
                    magic = inventory_system.Magic(item_script, character, target)
                    master_list.append(magic)
            else:
                magic = inventory_system.Magic(item_script, character, target)
                master_list.append(magic)
    return master_list


#Buffs/Debuffs
poison = {'name': 'Poison', 'icon': setup.BUFF_GFX['poison'], 'DoT': 21, 'DoT_type': 'magic', 'mask': 'poison', 'type': 'DoT', 'turns': 5, 'chance': 99}
haste = {'name': 'Haste', 'speed': {'num': 0.30, 'math_type': 'percent'}, 'mask': 'haste', 'type': 'buff', 'turns': 5}
cleanse = {'name': 'Cleanse', 'removes_buff': ['Poison', 'Curse', 'Blind']}
core_up_3 = {'name': 'Core Up III', 'attack': {'num': 2.0, 'math_type': 'percent'}, 'magic': {'num': 2.0, 'math_type': 'percent'}, 'skill': {'num': 2.0, 'math_type': 'percent'}, 
             'speed': {'num': 2.0, 'math_type': 'percent'}, 'luck': {'num': 2.0, 'math_type': 'percent'}, 'defense': {'num': 2.0, 'math_type': 'percent'}, 
             'resistance': {'num': 2.0, 'math_type': 'percent'}, 'mask': 'core_buff_3','type': 'buff', 'turns': 'manual'}

#Special
shock = {'name': 'Shock', 'level': 1, 'sp_cost': 0, 'type': 'damage', 'damage_type': 'magic', 'base_damage': 75, 'power': 3.60, 'crit_dmg': 250, 'crit_rate': 50, 'hit': 50,
         'description': 'Shocks all foes, dealing[.]massive magic damage.', 'multi_target': True, 'target_type': 'enemy'}
swan_dance = {'name': 'Dance of the Swan', 'level': 1, 'sp_cost': 0, 'type': 'white', 'base_damage': 31, 'damage_type': 'magic', 'power': 1.40, 'heal_type': 'hp', 'buff': cleanse, 
              'description': "A beautiful dance that[.]recovers all allies' HP[.]and cleanses debuffs.", 'multi_target': True, 'target_type': 'player'}

#Magic
magic_list = [{'name': 'Fire 1', 'type': 'magic', 'sub_type': 'black', 'base_damage': 21, 'mp_cost': 5, 'description': 'Deals small fire damage[.]to an enemy.'},
              {'name': 'Blizzard 2', 'type': 'magic', 'sub_type': 'black', 'base_damage': 62, 'mp_cost': 25, 'description': 'Deals adequate ice damage[.]to an enemy.'},
              {'name': 'Blizzard 3', 'type': 'magic', 'sub_type': 'black', 'base_damage': 122,  'mp_cost': 34, 'description': 'Deals massive ice damage[.]to an enemy.',},
              {'name': 'Bolting', 'type': 'magic', 'sub_type': 'black', 'base_damage': 150, 'mp_cost': 1, 'description':'Rift your foes asunder;[.]insta-kill foes.'},
              {'name': 'Cure', 'type': 'magic', 'sub_type': 'white', 'heal_hp': True, 'base_damage': 10, 'mp_cost': 5, 'description': 'Heal one ally for a small amount of HP.'},
              {'name': 'Haste', 'type': 'magic', 'sub_type': 'buff', 'is_buff': True, 'buff': haste, 'mp_cost': 15, 'description': "Buffs the target's speed[.]for 5 turns.", },
              {'name': 'Bio', 'type': 'magic', 'sub_type': 'black', 'base_damage': 34, 'mp_cost': 10, 'description': "Unleash the power of[.]microbes on your foes.", 'is_buff': True, 'buff': poison},
              {'name': 'Cleanse', 'type': 'magic', 'sub_type': 'white', 'mp_cost': 15, 'is_buff': True, 'buff': cleanse, 'description': 'Removes some debuffs[.]from the target.'}
              ]

#Items
item_list = [{'name': 'Potion', 'type': 'potion', 'sub_type': 'healing', 'uses': 1, 'mp_cost': 0, 'hp_cost': 0, 'hp_restore': 50, 'mp_restore': 0, 'description': "Heals the target's HP by 50."},
             {'name': 'High Potion', 'type': 'potion', 'sub_type': 'healing', 'uses': 1, 'mp_cost': 0, 'hp_cost': 0, 'hp_restore': 250, 'mp_restore': 0, 'description': "Heals the target's HP by [.]250."},
             {'name': 'Mega Potion', 'type': 'potion', 'sub_type': 'healing', 'uses': 1, 'mp_cost': 0, 'hp_cost': 0, 'hp_restore': 500, 'mp_restore': 0, 'description': "Heals the target's HP by [.]500."},
             {'name': 'Ether', 'type': 'potion', 'sub_type': 'healing', 'uses': 1, 'mp_cost': 0, 'hp_cost': 0, 'hp_restore': 0, 'mp_restore': 50, 'description': "Heals the target's MP by 50."},
             {'name': 'High Ether', 'type': 'potion', 'sub_type': 'healing', 'uses': 1, 'mp_cost': 0, 'hp_cost': 0, 'hp_restore': 0, 'mp_restore': 250, 'description': "Heals the target's MP by [.]250."},
             {'name': 'Mega Ether', 'type': 'potion', 'sub_type': 'healing', 'uses': 1, 'mp_cost': 0, 'hp_cost': 0, 'hp_restore': 0, 'mp_restore': 500, 'description': "Heals the target's MP by [.]500."},
             {'name': 'Revive', 'type': 'potion', 'sub_type': 'healing', 'uses': 1, 'mp_cost': 0, 'hp_cost': 0, 'hp_restore': 150, 'mp_restore': 0, 'revive': True, 'description': "Revives the target [.]and heals for 50 HP."}]

#Item List
master_item_list = make_master_item_list(item_list)

player_inventory = inventory_system.Inventory()

inventory_dict = [{'item': master_item_list[0], 'amount': 5}, {'item': master_item_list[1], 'amount': 1}, {'item': master_item_list[2], 'amount': 1}, {'item': master_item_list[3], 'amount': 1},
                  {'item': master_item_list[4], 'amount': 1}, {'item': master_item_list[5], 'amount': 1}, {'item': master_item_list[6], 'amount': 1}, {'item': master_item_list[0], 'amount': 5}]
player_inventory.make_initial_inventory(inventory_dict)


