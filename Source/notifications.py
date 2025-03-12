# notifications.py

from colorama import Fore, Style
from player import *

SCARY_REMINDERS = [
    "*** Just a reminder:  Have you forgotten that paranormal hotspots always have high radiation?\nYou don’t have many choices left. Choose wisely ***",
    "*** Just a reminder: Is someone whispering in the dark, or was it just your imagination?\nAnyway, and you're running out of choices. Choose wisely ***",
]

# TODO add other texts from prints here as variable (not investigations, only direct text from the print()). Skip it if you do not agree that variables are more beautiful
def get_messages(message_key):
    current_player = get_current_player()
    messages = {
        "COMMON_PRESS_ENTER_CONTINUE": "Press ENTER to continue",
        "COMMON_PRINT_OPTION_NUMBER": "Print number of option: ",
        "COMMON_WRONG_INPUT": "Wrong input. Please, try again",
        "START_PRESS_ENTER_START": "Press ENTER to start",
        "START_PRESS_ENTER_EMAIL": "Press ENTER to open the email",
        "START_WELCOME": "WeLC0ME TO UF0tutkiJA!",
        "START_ENTER_YOUR_NAME": "Enter your name (otherwise you will be Pekka): ",
        "START_HELLO_USER_NAME": f"Hello, {current_player['name']}, our best UFO hunter! \nYou've become a legend in paranormal investigations, but now...\nWell... You're stuck in your office, bored and waiting for something exciting...",
        "START_EMAIL_NOTIFICATION": f"\nOh wait!\n{current_player['name']}, you hear a notification from your email inbox... Open it?",
        "START_EMAIL_TEXT": f"""
            Date: 03 Sept 1999
            Sender: Mel_UFO-Investigator_77

            Yo, {current_player['name']}, it's your buddy MELVIN from Evergreen!1! Hope you still REMEMBER me, space cowboy
            anyways, i just cant believe what im seeing... its NOT normal! noooo way. This is... PARA-NORMAL, and its HUUUGE. 
            Like, REALLY f*cked up. I NEED your help here, at Evergreen!
            We need 2 meet @ {Fore.GREEN}Denver International Airport{Style.RESET_ALL} tomorrow evening.
            plz dont be late. dont tell anyone about this.

            Cya,
            Melvin
            P.S. I''ve added {Fore.MAGENTA}$500{Style.RESET_ALL} to your bank account for your plane ticket!1! HURRY UP!!
        """,
        "START_NOKIA": "Hooray! A business trip! Before leaving the office, don’t forget to take your Nokia from the desk. You’ll definitely need it.",
        "MAIN_WHAT_TO_DO": "\nWell, what do you want to do next?",
        "MAIN_TRAVEL": "Go to the airport",
        "MAIN_SHOP": "Buy equipment",
    }
    if not message_key:
        return messages
    else:
        return messages[message_key]
