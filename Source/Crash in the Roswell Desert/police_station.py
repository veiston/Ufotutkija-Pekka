import random
from utilities import print_separator, type_writer
from notifications import SCARY_REMINDERS

# Main function for the police station scenario
def police_station():
    print_separator()
    type_writer("You arrive at the small police station. The air conditioner hums loudly.")
    type_writer("A strict officer at the entrance immediately notices you.")
    
    type_writer("Officer (frowning): 'Hey! Civilians aren’t allowed here! And anyway, the army has already moved out there!'")
    type_writer("(The officer refuses to provide useful information.)")
    
    print("\nWhat will you do?")
    print("1. Try to steal the map from the chief's office.")
    print("2. Eavesdrop on the military radio.")
    print("3. Talk to the tired officer.")
    print("4. Sabotage the radio for everyone to hear.")
    
    choice = input("Choose an option (1/2/3/4): ")
    if choice == "1":
        steal_the_map()
    elif choice == "2":
        eavesdrop_on_radio()
    elif choice == "3":
        talk_to_tired_officer()
    elif choice == "4":
        sabotage_radio()
    else:
        type_writer(random.choice(SCARY_REMINDERS))
        police_station()

# Function to attempt stealing the map from the chief's office
def steal_the_map():
    print_separator()
    type_writer("You need a distraction to enter the chief's office.")
    
    print("How will you do it?")
    print("1. Set off a fire alarm.")
    print("2. Spill coffee.")
    print("3. Fake a delivery.")
    print("4. Use the open window.")
    
    distraction = input("Choose a method (1/2/3/4): ")
    if random.random() < 0.7:  # 70% chance of success
        type_writer("Your distraction works! You slip inside and take a quick photo of the map.")
        type_writer("The map marks an area with military activity and the note: 'Secure perimeter. No access.'")
    else:
        type_writer(random.choice(SCARY_REMINDERS))
        type_writer("Your distraction fails. The officers are suspicious!")
        police_station()

# Function to listen in on military radio transmissions
def eavesdrop_on_radio():
    print_separator()
    type_writer("You carefully listen to the military radio.")
    type_writer("Radio voice: '...unit moving in… The object is unstable. Repeat: unstable!'")
    type_writer("Another voice: 'Radio scanners are picking up interference from the crash site… but there shouldn’t be any transmitters there!'")
    type_writer("Before you hear more, the officer notices you.")
    
    reaction = input("Bluff (b) or try to slip away (s)? ").lower()
    if reaction == "b":
        type_writer("You pretend you got lost. The officer frowns but lets you go.")
    else:
        type_writer(random.choice(SCARY_REMINDERS))
        type_writer("You quietly step away before they get suspicious.")

# Function to talk to a tired officer for potential information
def talk_to_tired_officer():
    print_separator()
    type_writer("You offer coffee to a tired officer in the corner.")
    type_writer("Officer: 'I’m so sick of this! They’ve blocked everything off, won’t tell us a thing. Not even the sheriff knows!'")
    type_writer("With some persuasion, he reveals the military was already searching the desert before the explosion.")

# Function to sabotage the radio and reveal classified information
def sabotage_radio():
    print_separator()
    type_writer("You discreetly turn up the volume on the radio.")
    type_writer("A loud transmission plays: '...the object is still transmitting a signal. What the hell? We were supposed to shut it down!'")
    type_writer("Officers exchange nervous glances, clearly surprised by what they just heard.")

# Entry point of the game
def main():
    police_station()

if __name__ == "__main__":
    main()

# TODO: Add a time-based challenge for stealing the map.
# TODO: Implement a skill check system to increase/decrease chances of success.
# TODO: Introduce a secondary consequence if the player fails a task.
