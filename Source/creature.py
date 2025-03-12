import random
import config
from database import *
from player import update_player, get_current_player
from colorama import Fore, Style
from utilities import print_separator, input_press_enter, waiting_action
from notifications import get_messages
from inventory import *

#fetching the creature data from the database into a dictionary
#no need to change the creature's stats in the database
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
    #is it dead
    if creature['hp'] <= 0:
        config.tossNokia = False #fetching the Nokia off the ground
        return 'win'

    else:
        print(f'{creature['name']} attacks!')
        waiting_action()
        attack = random.randint(creature['attack'] - 5, creature['attack'] + 5)
        update_player('hp', get_current_player()['hp'] - attack, get_current_player()['id'])
        print(f'You take {Fore.RED}{attack} damage{Style.RESET_ALL}\n')
        input_press_enter('')
        print_separator()

        if get_current_player()['hp'] <= 0:
            config.tossNokia = False #even if you die you get your Nokia back
            update_player('hp', 200, get_current_player()['id']) #also resetting back to max health. you lose your items though
            return 'lose'

def how_is_the_creature_doing(creature):
    if creature['hp'] >= 0:
        print(f'{creature["name"]} has {Fore.MAGENTA}{creature["hp"]} HP{Style.RESET_ALL} left')
    else:
        print(f'{creature["name"]} has died')