# game.py

from colorama import Fore, Style

from Source.player import get_current_player
from utilities import type_writer, print_separator, input_press_enter, input_integer
from player import reset_player, add_player
from travel import travel
from shop import shop

def run_game():
    initialize_game()
    print_separator()
    show_main_menu()

def initialize_game():
    # Now we have only one player at a time, so we reset our database on every new game
    reset_player()

    print("WeLc0ME TO UF0tutkiJA!")
    input_press_enter("Press ENTER to start")

    new_user_name = input("Enter your name (otherwise you will be Pekka): ")
    add_player(new_user_name)

    print_separator()
    
    player = get_current_player()

    print(f"Hello, {player['name']}, our best UFO hunter! \nYou've become a legend in paranormal investigations, but now...\nWell... You're stuck in your office, bored and waiting for something exciting...")
    input_press_enter("Press ENTER to continue")

    print(f"\nOh wait!\n{player['name']}, you hear a notification from your email inbox... Open it?")
    input_press_enter("Press ENTER to open the email")

    type_writer(f"""
        Date: 03 Sept 1999
        Sender: Mel_UFO-Investigator_77

        Yo, {player['name']}, it's your buddy MELVIN from Evergreen!1! Hope you still REMEMBER me, space cowboy
        anyways, i just cant believe what im seeing... its NOT normal! noooo way. This is... PARA-NORMAL, and its HUUUGE. 
        Like, REALLY f*cked up. I NEED your help here, at Evergreen!
        We need 2 meet @ {Fore.GREEN}Denver International Airport{Style.RESET_ALL} tomorrow evening.
        plz dont be late. dont tell anyone about this.

        Cya,
        Melvin
        P.S. I''ve added {Fore.MAGENTA}$100{Style.RESET_ALL} to your bank account for your plane ticket!1! HURRY UP!!
        """, 0.03)
    input_press_enter("Press ENTER to continue")


def show_main_menu():
    while True:
        print("Well, what do you want to do next?")
        print(f"1. {Fore.GREEN}{"Go to the airport"}{Style.RESET_ALL}")
        print(f"2. {Fore.MAGENTA}{"Buy equipment"}{Style.RESET_ALL}")

        choice = input_integer("Print number of option: ")

        if choice == 1:
            travel()
        elif choice == 2:
            shop()
        else:
            print("Friend, there are no such options here, try again")

run_game()
