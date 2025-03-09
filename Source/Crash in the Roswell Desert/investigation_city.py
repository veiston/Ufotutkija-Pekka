import random
from utilities import print_separator, type_writer
from notifications import SCARY_REMINDERS

# Main function that starts the game
def main():
    print_separator()
    type_writer("Welcome to Roswell Investigation!")
    type_writer("You enter the hotel bar-restaurant. The place is small but cozy.")
    type_writer("You see an old pilot talking on the phone. You decide to listen in...")
    pilot_scene()

# Function to show the pilot's conversation only once
def pilot_scene():
    print_separator()
    type_writer("Pilot (on the phone): 'Kusto, I’m telling you, it was huge! And shiny! Like the mayor’s new Cadillac, but in the sky!'")
    type_writer("(The pilot glances around, notices you staring, and ends the call.)")
    print_separator()
    player_choices()

# Function to handle player's choices
def player_choices():
    while True:
        print_separator()
        type_writer("What will you do?")
        print("1. Try to steal the note with the coordinates.")
        print("2. Talk to the pilot and try to convince him.")
        print("3. Challenge the pilot in a mini-game.")
        
        choice = input("Choose an option (1/2/3): ")
        if choice == "1":
            steal_the_note()
            break
        elif choice == "2":
            if convince_the_pilot():
                break
        elif choice == "3":
            win_a_bet()
            break
        else:
            type_writer(random.choice(SCARY_REMINDERS))

# Function for attempting to steal the pilot's note
def steal_the_note():
    print_separator()
    type_writer("You carefully reach for the note as the pilot eats his burger...")
    if random.random() < 0.5:
        type_writer("A waiter drops a tray! The pilot notices you reaching for the note!")
        type_writer("Pilot: 'Whoa! I haven’t seen reflexes that fast since my cat saw a cucumber!'")
        type_writer(random.choice(SCARY_REMINDERS))
        player_choices()
    else:
        type_writer("You successfully steal the note! You now have the coordinates!")
        type_writer("Pilot: 'Be careful. If you see anything there besides sand – that means I was right.'")

# Function to convince the pilot by solving riddles
def convince_the_pilot():
    print_separator()
    type_writer("You sit across from the pilot.")
    type_writer("Player: 'I heard you saw something interesting.'")
    type_writer("Pilot: 'I did. But no one believes me! You think you’re worthy of the truth? Solve these riddles first!'")
    
    riddles = [
        {"question": "You're in the desert with no water. Do you go to the river or the bar?", "answer": "bar"},
        {"question": "You're on a crashing plane. What's the first thing you do?", "answer": "wake up"}
    ]
    
    for riddle in riddles:
        answer = input(f"{riddle['question']} (Type your answer): ").lower()
        if answer != riddle['answer']:
            type_writer("Pilot: 'Ha! You must be joking! Try again later.'")
            type_writer(random.choice(SCARY_REMINDERS))
            return False  # Return to choices without repeating the scene
    
    type_writer("Pilot: 'Alright, you’re not like all the skeptics. Here are the coordinates.'")
    type_writer("Pilot: 'Be careful. If you see anything there besides sand – that means I was right.'")
    return True  # Success, break loop

# Function to win the bet by playing the arcade game
def win_a_bet():
    print_separator()
    type_writer("You notice the pilot glaring at an old arcade machine.")
    type_writer("Pilot: 'This damn machine is rigged!'")
    type_writer("Player: 'Maybe I can give it a shot?'")
    
    if random.random() < 0.6:
        type_writer("You beat the high score! The pilot laughs and hands over the coordinates.")
        type_writer("Pilot: 'Be careful. If you see anything there besides sand – that means I was right.'")
    else:
        type_writer("You lose. The pilot chuckles. 'Try again?' (y/n)")
        type_writer(random.choice(SCARY_REMINDERS))
        retry = input().lower()
        if retry == "y":
            win_a_bet()
        else:
            player_choices()

# Entry point of the game
if __name__ == "__main__":
    main()

# TODO: Implement a scoring system for riddles.
# TODO: Add more possible ways to interact with the pilot.
# TODO: Introduce a time-based challenge for the arcade mini-game.