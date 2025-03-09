import random
from utilities import print_separator, type_writer
from notifications import SCARY_REMINDERS

# Main function for the desert journey scenario
def desert_journey():
    print_separator()
    type_writer("The player sets off into the desert, but the military is already on the move.")
    type_writer("How will you get there?")
    
    print("1. Main road (Fast but risky)")
    print("2. Abandoned mines (Safer but full of traps)")
    
    choice = input("Choose a route (1/2): ")
    if choice == "1":
        military_checkpoint()
    elif choice == "2":
        navigate_mines()
    else:
        type_writer(random.choice(SCARY_REMINDERS))
        desert_journey()

# Function for encountering a military checkpoint
def military_checkpoint():
    print_separator()
    type_writer("Night falls as you drive along the dusty desert road.")
    type_writer("Ahead, headlights flicker—military jeeps. A checkpoint blocks your path.")
    type_writer("Soldier: 'Stop the car! Papers!'")
    
    type_writer("How will you respond?")
    print("1. Pretend to be a lost tourist.")
    print("2. Pretend to be a food delivery courier.")
    print("3. Try to talk your way through with a joke.")
    
    choice = input("Choose an option (1/2/3): ")
    if choice == "1":
        lost_tourist()
    elif choice == "2":
        food_delivery()
    elif choice == "3":
        joke_escape()
    else:
        type_writer(random.choice(SCARY_REMINDERS))
        military_checkpoint()

# Function to pretend being a lost tourist
def lost_tourist():
    print_separator()
    type_writer("Player: 'Oh, thank God! I’m totally lost! Can you tell me how to get to the motel?'")
    type_writer("Soldier: 'What motel? This is just desert.'")
    type_writer("Player: 'Really? The guy at the gas station said I’d find the most famous motel here!'")
    if random.random() > 0.5:
        type_writer("The soldiers exchange glances and let you go, but you must turn back.")
    else:
        type_writer(random.choice(SCARY_REMINDERS))
        type_writer("The soldier isn't buying it. You are forced to retreat.")

# Function to bluff as a food delivery courier
def food_delivery():
    print_separator()
    type_writer("Player: 'Finally, soldiers! I’ve been looking for you! Got a delivery here!'")
    type_writer("Soldier: 'What kind of order?'")
    type_writer("Player: 'Five hot dogs, two burgers, three sodas... for Sergeant Thompson!'")
    if random.random() > 0.7:
        type_writer("The soldiers hesitate, then take the food and let you go.")
    else:
        type_writer(random.choice(SCARY_REMINDERS))
        type_writer("They see through your bluff and force you to leave.")

# Function to try talking through the checkpoint with a joke
def joke_escape():
    print_separator()
    type_writer("Player: 'Good to see you! I thought I was the only one seeing weird lights in the sky!'")
    type_writer("Soldier: 'Not your concern. Turn around.'")
    type_writer("Player: 'What, no secret movie being filmed here? War of the Worlds?'")
    if random.random() > 0.5:
        type_writer("The soldier chuckles and lets you go, but you must turn back.")
    else:
        type_writer(random.choice(SCARY_REMINDERS))
        type_writer("They glare at you and make you leave.")

# Function for navigating through the abandoned mines
def navigate_mines():
    print_separator()
    type_writer("You choose the abandoned mines, avoiding the road.")
    type_writer("Inside, narrow passages and unstable tunnels make progress slow and dangerous.")
    type_writer("You must navigate safely! (Mini-game could be implemented here.)")
    type_writer("After a tense journey, you emerge near the crash site, unseen by the military.")
    crash_site()

# Function for the crash site encounter
def crash_site():
    print_separator()
    type_writer("You reach the crash site. A strange object glows in the moonlight.")
    type_writer("What will you do?")
    print("1. Examine the wreckage.")
    print("2. Search for artifacts.")
    print("3. Touch the ship’s panels.")
    
    choice = input("Choose an action (1/2/3): ")
    if choice == "1":
        type_writer("The wreckage is unlike any metal you've ever seen, covered in strange patterns.")
    elif choice == "2":
        type_writer("You find an unidentified device, possibly still active.")
    elif choice == "3":
        type_writer("A vision flashes before your eyes! A garbled message transmits: '…do not touch… we… mistake…'")
    type_writer("In the distance, you hear approaching military vehicles…")
    end_mission()

# Function to conclude the mission based on player choices
def end_mission():
    print_separator()
    type_writer("Your choices impact the next steps:")
    type_writer("✔ Stealth: Escape with wreckage and analyze it later.")
    type_writer("✔ Contact: Receive a vision or message.")
    type_writer("✔ Conflict: Military forces arrive, forcing a fight or capture.")
    type_writer("The mystery deepens...")

# Entry point of the game
def main():
    desert_journey()

if __name__ == "__main__":
    main()

# TODO: Add a chase sequence if the player fails at the checkpoint.
# TODO: Implement a puzzle for navigating the mines.
# TODO: Introduce branching paths depending on player success or failure.
