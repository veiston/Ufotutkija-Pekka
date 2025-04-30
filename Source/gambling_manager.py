# gambling.py
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
from utilities import print_separator, input_integer, clear_screen
from colorama import Fore, Style
from snake_game import play_snake
#from poker import play_poker  # RIP
from blackjack import play_blackjack
# from player import get_current_player, update_player
from player import Player

available_games = {
    "Blackjack": play_blackjack,
    "Snake": play_snake
}

def gambling_menu():
    clear_screen()

    player = Player()
    player.id = Player.current_id
    player_data = player.get_current()

    while True:
        print_separator()
        print(f"Welcome to the gambling corner!\nHere you can turn your {Fore.MAGENTA}💵 money 💵{Style.RESET_ALL} into.. MORE MONEY!\n")
        
        menu_options = list(available_games.keys()) + ["Exit"]
        for i, game_name in enumerate(menu_options, start=1):
            print(f"{i}. {game_name}")
        print_separator()
        
        choice = input_integer('\nWhat do you want to play?\n')
        if choice < 1 or choice > len(menu_options):
            print(f"{Fore.RED}No such option. Please choose a valid number.{Style.RESET_ALL}")
            continue
        
        # Exit if choise = last in menu
        if choice == len(menu_options):
            print(f"{Fore.YELLOW}Exiting gambling corner...{Style.RESET_ALL}")
            break
        
        # Launch game.
        selected_game = menu_options[choice - 1]
        game_function = available_games[selected_game]

        # Give reward if player wins
        new_money = game_function(player_data)
        if new_money is not None:
            player.update({"money": new_money})
        
if __name__ == "__main__":
    gambling_menu()
