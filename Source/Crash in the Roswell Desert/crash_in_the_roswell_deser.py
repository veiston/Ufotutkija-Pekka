import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import investigation_city
import police_station
import desert_mission
from utilities import print_separator, type_writer
from notifications import SCARY_REMINDERS


# Main function to start the game and navigate between modules
def start_game():
    print_separator()
    type_writer("Welcome to Roswell Investigation!")
    type_writer("Choose your starting location:")
    
    print(f"1. Hotel Bar (Investigate the pilot)")
    print(f"2. Police Station (Find classified information)")
    print(f"3. Desert (Reach the crash site)")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        print_separator()
        investigation_city.main()
    elif choice == "2":
        print_separator()
        police_station.main()
    elif choice == "3":
        print_separator()
        desert_mission.main()
    else:
        type_writer("Invalid choice. Try again.")
        start_game()

# Run the game if executed as the main script
if __name__ == "__main__":
    start_game()
