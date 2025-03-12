# gambling.py
# TODO In the shop the player selects “earn money” and is directed here. Here they see a list of games and the option to choose one. The game files or functions or whatever need to be imported

import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
from utilities import *
from colorama import Fore, Style
from snake_game import play_snake
from poker import play_poker
from blackjack import play_blackjack
from player import get_current_player

player = get_current_player()
selection_of_games = ['Blackjack', 'Snake', 'Poker', 'Exit']

# Main function to call from shop
def menu():
    choice = int
    while choice != 4:
        print_separator()
        print(f'Welcome to the gambling corner!\nHere you can turn your {Fore.MAGENTA}💵 money 💵 {Style.RESET_ALL}into.. MORE MONEY!')
        # time.sleep(0.5)

        # Print game selection
        i=0
        for game in selection_of_games:
            i += 1
            print(str(i) + '. ' + game)
        print_separator()

        # Check game choice and laucnh said-
        choice = input_integer('\nWhat do you want to play?\n')
        if choice == 1:
            play_blackjack(player)
        elif choice == 2:
            play_blackjack(player)
        elif choice == 3:
            play_poker(player)
        elif choice == 4:
            continue
        else:
            'No such option. Sorry mate.'
            menu()
    


# Test function
if __name__ == "__main__":
    menu()
