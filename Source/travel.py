# travel.py
import time

from colorama import Fore, Style
from utilities import type_writer, print_separator
from player import player
from investigations import investigate

# TODO, a fucking ton of TODOs... This is logic for traveling. It is not hard, just takes time. Comments about requirements are below

PRICE_PER_KM = 0.01

def travel():
    print_separator()

    print(f"Your level: {player['level']}")
    print(f"Your balance: ${player['money']}")
    print(f"\nAttention, {player['name']}! By agreeing to the flight, you start investigating a new case.\n\nOptions, where you could go now:")

    if player['level'] == 1:
        # TODO replace this stub (these prints) with actual code about traveling. Comments about the possible implementation are below
        print("\n(Here the airport selection mechanics should be implemented.\nI have described them in the comments in the code.\nYou can a look at it after.\nFor now let's pretend the player receives a list of airports not by hardcode. On level 1 it's just one airport)")
        print(f"\n1. {Fore.GREEN}Denver International Airport (KDEN){Style.RESET_ALL}")
        input("\nSelect the airport you want to fly to by its number in the list: ")
        print("\nGreat choice!")
        type_writer("Taking off...", 0.1)
        time.sleep(0.5)
        type_writer("Flying...", 0.1)
        time.sleep(0.5)
        type_writer("Landing complete!", 0.1)
        time.sleep(0.5)
        player['airport'] = 'KDEN'
        player['investigation'] = 'tutorial'
        player['money'] -= 100

        investigate(player['investigation'])
    else:
        print("There's no option for level 2 yet")

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