import time
import sys
import random
from database import *
from player import update_player, get_current_player
from colorama import Fore, Style
from utilities import type_writer, print_separator, input_press_enter, input_integer
from notifications import get_messages
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

def waiting_action():
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(1)

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
        print('tööt')
        return creature
    else:
        print('tuut')
        return {}
#print(get_data_from_database(getCreature))
#print(get_current_player()['location_ident'])
#print(get_current_player()['hp'])

def Battle():
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
            type_writer(f'You attack {creature['name']}', 0.03)
            waiting_action()
            attack = random.randint(get_current_player()['attack']-5, get_current_player()['attack']+5)
            creature['hp']-=attack
            print(f'{creature['name']} takes {Fore.RED}{attack} damage{Style.RESET_ALL}\n')
            print(f'{creature["name"]} {creature["hp"]} HP')
            input_press_enter('')

            if creature['hp']<=0:
                fight = False
                print('victory')
            else:
                print(f'{creature['name']} attacks!')
                waiting_action()
                attack = random.randint(creature['attack']-5, creature['attack']+5)
                update_player('hp', get_current_player()['hp'] - attack, 1)
                print(f'You take {Fore.RED}{attack} damage{Style.RESET_ALL}\n')
                input_press_enter('')

                if get_current_player()['hp']<=0:
                    fight = False
                    print('kualit')
        elif action == 2:
            print('itemit')
        elif action ==3:
            print(creature['description'])




Battle()
#player = get_current_player()
#print(get_current_player()['hp'])
#update_player('hp', get_current_player()['hp']-10, 1)
#print(get_current_player()['hp'])

