import time
import sys
import random
import config
from database import *
from player import update_player, get_current_player
from colorama import Fore, Style
from utilities import type_writer, print_separator, input_press_enter, input_integer, waiting_action
from notifications import get_messages
from inventory import *
#KDEN

"""
query = (
    f'SELECT creature.name, creature_types.hp, creature_types.attack, creature.creature_type, creature.description '
    f'FROM creature '
    f'INNER JOIN creature_types '
    f'ON creature.creature_type = creature_types.name '
    f'WHERE creature.location_ident = "{get_current_player()["location_ident"]}";')
print(get_data_from_database(query))
"""





def get_creature():
    query = (f'SELECT creature.name, creature_types.hp, creature_types.attack, creature_types.weakness, creature.creature_type, creature.description '
             f'FROM creature '
             f'INNER JOIN creature_types '
             f'ON creature.creature_type = creature_types.name '
             f'WHERE creature.location_ident = "{get_current_player()["location_ident"]}";')
    result = get_data_from_database(query)
    if result:
        columns = ["name", "hp", "attack", "weakness", "type", "description"]
        creature_data = result[0]
        creature = {columns[i]: creature_data[i] for i in range(len(columns))}
        return creature
    else:
        return {}

def creature_turn(creature):
    if creature['hp'] <= 0:
        config.tossNokia = False
        print('victory')
        return 'win'

    else:
        print(f'{creature['name']} attacks!')
        waiting_action()
        attack = random.randint(creature['attack'] - 5, creature['attack'] + 5)
        update_player('hp', get_current_player()['hp'] - attack, get_current_player()['id'])
        print(f'You take {Fore.RED}{attack} damage{Style.RESET_ALL}\n')
        input_press_enter('')

        if get_current_player()['hp'] <= 0:
            config.tossNokia = False
            print('kualit')
            return 'lose'
#print(get_data_from_database(getCreature))
#print(get_current_player()['location_ident'])
#print(get_current_player()['hp'])




def battle():
    fight = True
    creature = get_creature()
    print(f'Suddenly you are ambushed by {Fore.CYAN}{creature['name']}{Style.RESET_ALL}')
    input_press_enter('')

    while fight:
        print(f'You have {Fore.LIGHTGREEN_EX}{get_current_player()['hp']} HP{Style.RESET_ALL} left')
        input_press_enter('')
        print('Choose your next action')
        print(f'1) Attack\n'
              f'2) Use item\n'
              f'3) Inspect')

        action = input_integer(get_messages("COMMON_PRINT_OPTION_NUMBER"))

        if action == 1:
            print_separator()

            print(f'You attack {creature['name']}')
            waiting_action()
            attack = random.randint(get_current_player()['attack']-5, get_current_player()['attack']+5)
            creature['hp']-=attack
            print(f'{creature['name']} takes {Fore.RED}{attack} damage{Style.RESET_ALL}\n')
            print(f'{creature["name"]} {creature["hp"]} HP')
            input_press_enter('')

            turnChange = creature_turn(creature)
            print(turnChange)
            if turnChange == 'win':
                #fight = False
                return True
            elif turnChange == 'lose':
                return False

        elif action == 2:
            print_separator()
            item = list_inventory()

            if item!='exit':
                if item['type'] == 'Healing':
                    update_player('hp', get_current_player()['hp']+item['power'], get_current_player()['id'])
                    print(f'Yo regain {Fore.GREEN}{item["power"]}{Style.RESET_ALL} health')
                    input_press_enter('')

                else:
                    print(f'You throw {item["name"]} at {creature["name"]}!')
                    waiting_action()

                    if item['type'] == creature['weakness']:
                        attack = item['power']*2

                    else:
                        attack = item['power']

                    creature['hp']-=attack
                    print(f'{creature['name']} takes {Fore.RED}{attack} damage{Style.RESET_ALL}\n')
                    print(f'{creature["name"]} {creature["hp"]} HP')
                    input_press_enter('')

                turnChange = creature_turn(creature)
                if turnChange == 'win':
                    return True
                elif turnChange == 'lose':
                    return False


        elif action ==3:
            print_separator()
            print(creature['description'])
            print(creature['hp'])
            print(creature['type'])


#config.tossNokia = True
#list_inventory()

"""
inventory = get_inventory()

for i in range(len(inventory)):
    print(i+1)
    print(inventory[i]['item'])
"""
print(battle())
#player = get_current_player()
#print(get_current_player()['hp'])
#update_player('hp', get_current_player()['hp']-10, 1)
#print(get_current_player()['hp'])

