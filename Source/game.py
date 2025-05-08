from colorama import Fore, Style
from utilities import type_writer, print_separator, input_press_enter, input_integer, clear_screen
from player import *
from notifications import get_messages
from travel import travel
from shop import shop

def run_game():
    initialize_game()
    print_separator()
    show_main_menu()


def initialize_game():
    print(get_messages("START_WELCOME"))
    input_press_enter(get_messages("START_PRESS_ENTER_START"))

    user_name = input(get_messages("START_ENTER_YOUR_NAME"))

    # Ensure player level is set to 1 after creating the player
    current_player = get_current_player()
    if current_player:
        if user_name:
            update_player("name", user_name, current_player["id"])
        update_player("player_level", 1, current_player["id"])
        update_player("money", 00, current_player["id"])
    
    print_separator()
    print(get_messages("START_HELLO_USER_NAME"))
    input_press_enter(get_messages("COMMON_PRESS_ENTER_CONTINUE"))
    print(get_messages("START_EMAIL_NOTIFICATION"))
    input_press_enter(get_messages("START_PRESS_ENTER_EMAIL"))
    type_writer(get_messages("START_EMAIL_TEXT"), 0.02)
    input_press_enter(get_messages("COMMON_PRESS_ENTER_CONTINUE"))
    print(get_messages("START_NOKIA"))
    update_data_in_database(f'INSERT INTO inventory(player_id, item) VALUES ({current_player["id"]}, "Nokia");')
    input_press_enter(get_messages("COMMON_PRESS_ENTER_CONTINUE"))

def show_main_menu():
    while True:
        clear_screen()
        print(get_messages("MAIN_WHAT_TO_DO"))
        print(f"1. {Fore.MAGENTA}{get_messages("MAIN_SHOP")}{Style.RESET_ALL}")
        print(f"2. {Fore.GREEN}{get_messages("MAIN_TRAVEL")}{Style.RESET_ALL}")

        choice = input_integer(get_messages("COMMON_PRINT_OPTION_NUMBER"))

        if choice == 1:
            shop()
        elif choice == 2:
            travel()
        else:
            print(get_messages("COMMON_WRONG_INPUT"))

run_game()
