# notifications.py

from colorama import Fore, Style
# from player import player

# the player has 3 or fewer turns remaining, a random scary reminder is displayed on the screen
# to create a sense of urgency and explain the concept of turns to the player
# the text can be changed, new items can be added
SCARY_REMINDERS = [
    "*** Just a reminder:  Have you forgotten that paranormal hotspots always have high radiation?\nYou don’t have many choices left. Choose wisely ***",
    "*** Just a reminder: Is someone whispering in the dark, or was it just your imagination?\nAnyway, and you're running out of choices. Choose wisely ***",
]

# TODO add other texts from prints here as variable (not investigations, only direct text from the print()). Skip it if you do not agree that variables are more beautiful
def get_messages(key):
    messages = {

        "COMMON_PRINT_OPTION_NUMBER": "Print number of option: ",
        "COMMON_WRONG_INPUT": "Wrong input. Please, try again",

        "START_PRESS_ENTER_EMAIL": "Press ENTER to open the email",

        "START_ENTER_YOUR_NAME": "Enter your name (otherwise you will be Pekka): ",
        "START_HELLO_USER_NAME": f"Hello, {player['name']}, our best UFO hunter! \nYou've become a legend in paranormal investigations, but now...\nWell... You're stuck in your office, bored and waiting for something exciting...",


        "MAIN_TRAVEL": "Go to the airport",
        "MAIN_SHOP": "Buy equipment",
    }
    if not key:
        return messages
    else:
        return messages[key]
