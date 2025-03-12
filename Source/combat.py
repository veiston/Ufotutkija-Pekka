import random
import config
from database import *
from player import update_player, get_current_player
from colorama import Fore, Style
from utilities import print_separator, input_press_enter, input_integer, waiting_action
from notifications import get_messages
from inventory import list_inventory
from creature import get_creature, creature_turn, how_is_the_creature_doing

def battle():
    fight = True
    creature = get_creature()
    print(f'Suddenly you are ambushed by {Fore.CYAN}{creature['name']}{Style.RESET_ALL}')
    input_press_enter('')

    while fight:

        #determine what colour the player health is displayed in
        if get_current_player()['hp']>=100:
            colour = Fore.GREEN
        else:
            colour = Fore.RED

        print(f'You have {colour}{get_current_player()['hp']} HP{Style.RESET_ALL} left')
        input_press_enter('')

        print('Choose your next action')
        print(f'1) Attack\n'
              f'2) Use item\n'
              f'3) Inspect\n')

        action = input_integer(get_messages("COMMON_PRINT_OPTION_NUMBER"))

        if action == 1:
            print_separator()

            print(f'You attack {creature['name']}')
            waiting_action()
            #adding random element to the normal attack
            attack = random.randint(get_current_player()['attack']-5, get_current_player()['attack']+5)
            creature['hp']-=attack
            print(f'{creature['name']} takes {Fore.RED}{attack} damage{Style.RESET_ALL}\n')

            how_is_the_creature_doing(creature) #is the thing alive or not and how much health it has
            input_press_enter('')

            turnChange = creature_turn(creature) #creature attack logic contained in creature.py

            if turnChange == 'win':
                return True
            elif turnChange == 'lose':
                return False

        elif action == 2:
            print_separator()
            item = list_inventory() #calling the inventory from inventory.py

            if item!='exit': #checks if you chose item instead of just exiting the inventory
                print_separator()

                if item['type'] == 'Healing':
                    #checking for overhealing
                    #let's add max health to the database in the future!
                    if get_current_player()['hp']+item['power']>=200:
                        healing = 200
                        healthGained = 200-get_current_player()['hp']
                    else:
                        healing = get_current_player()['hp']+item['power']
                        healthGained = item['power']
                    update_player('hp', healing, get_current_player()['id'])

                    print(f'You regain {Fore.GREEN}{healthGained}{Style.RESET_ALL} health')
                    input_press_enter('')

                else: #attack items
                    print(f'You throw {item["name"]} at {creature["name"]}!')
                    waiting_action()

                    if item['type'] == creature['weakness']:
                        attack = item['power']*2
                        print(f'{Fore.CYAN}{item["name"]} is very effective against {creature["name"]} and does double damage to it!{Style.RESET_ALL}\n')

                    else:
                        attack = item['power']

                    creature['hp']-=attack
                    print(f'{creature['name']} takes {Fore.RED}{attack} damage{Style.RESET_ALL}\n')

                    how_is_the_creature_doing(creature)
                    input_press_enter('')

                turnChange = creature_turn(creature) #creature will attack no matter the type of item you choose

                if turnChange == 'win':
                    return True
                elif turnChange == 'lose':
                    return False


        elif action ==3: #get a little flavour text and the creature type
            print_separator()
            print(creature['name'])
            print(creature['description'])
            print(f"\nWith your extensive knowledge of all things weird, you determine the creature is the {Fore.CYAN}{creature["type"]}{Style.RESET_ALL}-type and has {Fore.MAGENTA}{creature['hp']} HP{Style.RESET_ALL}")
            input_press_enter('')
            print_separator()

if __name__ == "__main__":
    battle()