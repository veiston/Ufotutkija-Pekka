# travel.py
import time
from database import get_data_from_database, update_data_in_database
from colorama import Fore, Style
from utilities import type_writer
from player import get_current_player, update_player, add_player
from investigations import investigate

PRICE_PER_KM = 0.01

# Travel text function
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

def travel():
    current_player = get_current_player()
    if not current_player:
        print("ERROR: No player found. Please create a player first.")
        return

    # Consolidated airport selection logic for all levels
    airport_symbol = "KDEN"
    airport_text = f"Denver International Airport ({airport_symbol})"
    print(f"\n1. {Fore.GREEN}{airport_text}{Style.RESET_ALL}")
    input("\nSelect the airport you want to fly to by its number in the list: ")
    print("\nGreat choice!")
    flight_text()
    
    # Update player's airport and deduct money.
    update_player('location_ident', airport_symbol, current_player['id'])
    new_money = current_player['money'] - 100
    update_player('money', new_money, current_player['id'])
    
    # Start investigation
    investigate('tutorial')
    
    # Fetch and display airport data using the new function
    airport_data = get_airport_data(airport_symbol)

# Test block to check if the functions work. (This is only run if running this file directly)
if __name__ == '__main__':
    add_player('Test dude')
    current_player = get_current_player()
    # For testing, manually set player level if needed.
    current_player['player_level'] = 2  
    travel()

    # For this logic you need database. See file database.py for more information about what is already done

    # How does the player choose the airport they want to fly to?
    # We take the list of all investigations. Each investigation has a level and an airport.
    # We filter the list of investigations, keeping only those where the level matches the player's level.
    # From the filtered investigations we extract the airport field and create a list of airport codes.
    # We search for each found airport in the database using its code and retrieve its name.
    # We display the list of available airports, numbering them so the player can choose.
    # When the player enters the number of an airport, we find it in the list and determine whether the player can fly there.

    # How do we determine if the player can fly to the selected airport?
    # The player has a field player["airport"], which stores the code of the airport where they are currently located.
    # (If the player hasn't flown yet, they are in the default airport (EFHK – Helsinki))
    # We take the code of the current airport and the identifier of the selected airport.
    # We calculate the distance between these two airports (we did a similar Python homework, if I remember right).
    # Based on the distance we calculate the flight cost. For example, we can take 1km as 0.01$. We use the PRICE_PER_KM variable (it's defined above and can be changed).
    # We check if the player has enough money.
    # If player doesn’t have enough money, we show them a message and tell them they need to go Gambling in the store.
    # If player does have enough money, we "move" the player to the new airport and start new investigation.

    # How do we determine which investigation the player starts with chosen airport? IMPORTANT: for now, one airport = one investigation
    # Each investigation has a unique key (ex: "tutorial") and is linked to a specific airport.
    # After the player selects an airport, we search for an investigation where the "airport" field matches the selected airport.
    # We take the key of that investigation and assign it to player["investigation"].
    # We need this key later, that is why I decided to save it