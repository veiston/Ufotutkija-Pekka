# game.py

from colorama import Fore, Style
from utilities import type_writer, print_separator, input_press_enter, input_integer
from player import *
from notifications import get_messages
from travel import travel
from shop import shop

# run_game function first initializes the game (player’s name, Melvin’s letter), then shows menu (travel or shop)
def run_game():
    initialize_game()
    print_separator() # utility function print_separator, see utilities.py
    show_main_menu()

def initialize_game():
    print(get_messages("START_WELCOME"))
    input_press_enter(get_messages("START_PRESS_ENTER_START"))
    
    set_player_name()
    
    # Ensure player level is set to 1 after creating the player
    current_player = get_current_player()
    if current_player:
        update_player("player_level", 1, current_player["id"])
    
    print_separator()
    print(get_messages("START_HELLO_USER_NAME"))
    input_press_enter(get_messages("COMMON_PRESS_ENTER_CONTINUE"))
    print(get_messages("START_EMAIL_NOTIFICATION"))
    input_press_enter(get_messages("START_PRESS_ENTER_EMAIL"))
    type_writer(get_messages("START_EMAIL_TEXT"), 0.03)
    input_press_enter(get_messages("COMMON_PRESS_ENTER_CONTINUE"))

def set_player_name():
    user_name = input(get_messages("START_ENTER_YOUR_NAME"))
    if user_name:
        update_player("name", user_name)

def show_main_menu():
    while True:
        print(get_messages("MAIN_WHAT_TO_DO"))
        print(f"1. {Fore.GREEN}{get_messages("MAIN_TRAVEL")}{Style.RESET_ALL}")
        print(f"2. {Fore.MAGENTA}{get_messages("MAIN_SHOP")}{Style.RESET_ALL}")

        choice = input_integer(get_messages("COMMON_PRINT_OPTION_NUMBER"))

        if choice == 1:
            travel()
        elif choice == 2:
            shop()
        else:
            print(get_messages("COMMON_WRONG_INPUT"))

run_game()
