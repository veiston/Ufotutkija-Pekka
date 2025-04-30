# travel.py
import time
from database import get_data_from_database, update_data_in_database
from colorama import Fore, Style
from utilities import type_writer, clear_screen
# from player import get_current_player, update_player, add_player
from player import Player
from investigations import investigate, investigations

PRICE_PER_KM = 0.01
FLIGHT_COST = 100

def flight_text():
    type_writer("Taking off...", 0.04)
    time.sleep(0.5)
    type_writer("Flying...", 0.04)
    time.sleep(0.5)
    type_writer("Landing complete!", 0.04)
    time.sleep(0.5)

def get_airport_data(symbol):
    query = f"SELECT * FROM airport WHERE ident = '{symbol}'"
    result = get_data_from_database(query)
    return result[0] if result else None

def get_available_airports(player_level):
    """
    Here it returns a list of airport symbols unlocked based on the player's level.
    Level 5 or higher: All configured airports become available.
    """
    if player_level == 1:
        return ["KBNA"]
    elif player_level == 2:
        return ["KDEN", "KSEA", "KHTS"]
    elif player_level == 3:
        return ["KBNA"]
    else:
        return ["KDEN", "KSEA", "KBNA", "KHTS"]

def travel():
    # current_player = get_current_player()
    player = Player()
    player.id = Player.current_id
    if not player.id:
        print("ERROR: No player found. Please create a player first.")
        return
    player_data = player.get_current()
    # Change lever for testing purposes here:
    # Retrieve available airports based on player's level

    available_airports = get_available_airports(player_data['player_level'])
    
    print("\nAvailable Airports:")
    airport_options = []
    index = 1
    for symbol in available_airports:
        airport_data = get_airport_data(symbol)
        if airport_data:
            # Expected structure: (ident, name, municipality, player_location)
            airport_name = airport_data[1]
            option_text = f"{airport_name} ({symbol})"
            print(f"{index}. {Fore.GREEN}{option_text}{Style.RESET_ALL}")
            airport_options.append(symbol)
            index += 1
    
    # Option to exit travel
    print(f"{index}. Exit travel")
    
    choice = input("\nSelect the airport you want to fly to by its number: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == index:
            print("Exiting travel...")
            return
        elif 1 <= choice < index:
            selected_symbol = airport_options[choice - 1]
            selected_airport = get_airport_data(selected_symbol)
            print(f"\nGreat choice! You selected {selected_airport[1]} ({selected_symbol})")
            flight_text()
            
            # Check if the player has enough money for the flight
            if player_data["money"] < FLIGHT_COST:
                print(f"Insufficient funds for the flight. You have ${player_data['money']}, but the flight costs ${FLIGHT_COST}. Have you tried to earn more money by gambling?")
                return
            
            # Update player's airport and deduct flight cost.
            player.update({'location_ident': selected_symbol})
            new_money = player_data['money'] - FLIGHT_COST
            player.update({'money': new_money})
            print(f"Flight cost ${FLIGHT_COST} deducted. New balance: ${new_money}")

            current_investigation = None

            for key, value in investigations.items():
                if value["airport"] == selected_symbol and not value["is_completed"]:
                    current_investigation = key
                    break

            if current_investigation:
                # Start investigation
                clear_screen()
                investigate(current_investigation)
        else:
            print("Invalid option selected.")
    else:
        print("Invalid input.")

# Test block to check if the functions work. (This is only run if running this file directly)
if __name__ == '__main__':
    player = Player('Test dude')
    player.add()
    travel()