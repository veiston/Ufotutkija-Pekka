
# just imports
from colorama import Fore, Style
# import mysql.connector
import time
import sys
import random

##########################################################################################
# constants
PRICE_PER_KM = 0.01

##########################################################################################

# utilities. utility is a helper function that performs a common task.

def type_writer(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def print_separator():
    print("\n" + "=" * 50 + "\n")

##########################################################################################

# db connection. in this version we use only original flight_game database, we do not have our own database
# attention! here's my user and password, do not forget to replace it with yours
# also field "collation" may be inappropriate for windows or linux, idk
# commented because we do not need it yet, I did not white the code for it
# yhteys = mysql.connector.connect(
#     host='127.0.0.1',
#     port=3306,
#     database='flight_game',
#     user='root',
#     password='1234',
#     autocommit=True,
#     collation="utf8mb4_unicode_ci"
# )

##########################################################################################
# our starting setting for the player
player = {
    "name": "Pekka",  # the player's default name is Pekka, but they can change it
    "investigation": '', # the unique key of current investigation
    "airport": "EFHK",  # this is Helsinki-Vantaan lentoasema, the starting point
    "money": 100,  # player needs money for the shop and flights
    "level": 1,  # player's level determines access to new locations
    "inventory": ["nokia"]  # here is the list of bought items from "items", example: ["nokia", "salt"]
}

##########################################################################################

# all items for shop will be here with their name, price and success_chance
# there is no funny pokemon logic here, I hope somebody else could add it, because I do not understand it well yet - Ks
# however I have implementation of the Success-Chance-Idea below
items = {
    "bat": {"name": "Baseball bat", "price": 50, "success_chance": 80},
    "salt": {"name": "Salt", "price": 20, "success_chance": 70},
    "nokia": {"name": "Nokia", "price": 0, "success_chance": 50},
}
# What is success_chance in items? This field defines the price of the item
# Example of using success_chance in the gameplay:
#
# You hear a strange noise in the dark. What do you do?
# 1. Throw salt (need salt, success chance 50%)
# 2. Throw Nokia (need nokia (always awailable), success chance 20%)
#
# You throw the salt...
# It failed! Try again or choose another item.
#
# You hear a strange noise in the dark. What do you do?
# 1. Throw salt (need salt, success chance 50%)
# 2. Throw Nokia (need nokia (always awailable), success chance 20%)
#
# You throw Nokia...
# It worked! The Nokia flies through the air and... (description of next step)
#
#  So player uses their attempt for item using. If item is cheap, the chance of success is low and the player may waste the attempt

# NOKIA IS ALWAYS AVAILABLE, BUT HAS REALLY LOW CHANCE FOR SUCCESS!
# (I understand that this is impossible in real life, and we should give the Nokia a 100% success rate, but we have a not real story)

###############################################################################

# the player has 3 or fewer turns remaining, a random scary reminder is displayed on the screen
# to create a sense of urgency and explain the concept of turns to the player
# the text can be changed, new items can be added
scary_reminders = [
    "*** Just a reminder:  Have you forgotten that paranormal hotspots always have high radiation?\nYou don’t have many choices left. Choose wisely ***",
    "*** Just a reminder: Is someone whispering in the dark, or was it just your imagination?\nAnyway, and you're running out of choices. Choose wisely ***",
]
# ##########################################################################################

investigations = {
    "tutorial": { # story ident, important
        "name": "Tutorial",  # story name, currently unused field
        "description": f"*** {player['name']}, you arrive in the Evergreen to meet Melvin, but your friend doesn't show up\n at the airport by the appointed time. The clock is nearing midnight. Worried, you make\n your way to Melvin's home, using the last known address he mentioned.\n The streets are unusually silent and a strange feeling of unease begins to grow. ***",  # story description
        "airport": "KDEN",  # airport code related to this story
        "reward": 200,  # mission completion reward (money)
        "turns_limit": 8,  # number of attempts allowed for the location
        "level": 1,  # location level, must match the player's level to access
        "win_text":  f"{player['name']}, it looks like you now have to find out what happened to Melvin\n and where the mysterious coordinates from his notebook will lead you.\n For now, you receive $200 for new flights. The Nokia stays in your pocket.",
        "lose_text": f"{player['name']}, we are sorry, but you have run out of turns. You need to restart this investigation from the beginning.",
        "steps": {
            # the game at this location starts from step 1
            1: {  # each story step has an ID for reference
                "text": "Upon arriving you finds Melvin’s car still parked in his yard and the door to his house is ajar.\n You call out for Melvin, but there’s no answer. You head inside.",  # step text displayed to the user
                "choices": {
                    "go_office": {
                        "text": "Go to the office",
                        "next_step": 2, # go to step 2 if you choose this option
                        "required_item": None  # if there is an item identifier, such as “nokia,” the user starts a random game with the success chance described above
                    },
                    "go_kitchen": {
                        "text": "Go to the kitchen",
                        "next_step": 3, # go to step 3 if you choose this option
                        "required_item": None
                    },
                    "examine_living_room": {
                        "text": "Examine the living room",
                        "next_step": 4,
                        "required_item": None
                    }
                }
            },
            2: {
                "text": "You enter the office. You can search the desk drawers or examine the bookshelf.",
                "choices": {
                    "search_desk": {
                        "text": "Search the desk drawers",
                        "next_step": 5,
                        "required_item": None
                    },
                    "examine_bookshelf": {
                        "text": "Examine the bookshelf",
                        "next_step": 6,
                        "required_item": None
                    }
                }
            },
            3: {
                "text": "You enter the kitchen. You find a small gray alien! It is holding Melvin’s notebook!",
                "choices": {
                    "throw_phone": {
                        "text": "Throw your Nokia at the alien (required item Nokia)",
                        "next_step": 7,
                        "required_item": "nokia"
                    },
                    "throw_salt": {
                        "text": "Throw salt at the alien (required item Salt)",
                        "next_step": 7,
                        "required_item": "salt"
                    }
                }
            },
            4: {
                "text": "You see a stack of books and photographs with notes, but nothing unusual.",
                "choices": {
                    "go_office": {
                        "text": "Go to the office",
                        "next_step": 2,
                        "required_item": None
                    },
                    "go_kitchen": {
                        "text": "Go to the kitchen",
                        "next_step": 3,
                        "required_item": None
                    }
                }
            },
            5: {
                "text": "You find Melvin’s laptop. You open it and go to Melvin’s research folder,\n but all the files are encrypted. Such a shame.",
                "choices": {
                    "examine_bookshelf": {
                        "text": "Examine the bookshelf",
                        "next_step": 6,
                        "required_item": None
                    },
                    "go_kitchen": {
                        "text": "Go to the kitchen",
                        "next_step": 3,
                        "required_item": None
                    }
                }
            },
            6: {
                "text": "You find an old book with strange symbols. Nothing interesting...",
                "choices": {
                    "search_desk": {
                        "text": "Search the desk drawers",
                        "next_step": 5,
                        "required_item": None
                    },
                    "go_kitchen": {
                        "text": "Go to the kitchen",
                        "next_step": 3,
                        "required_item": None
                    }
                }
            },
            7: {
                "text": "The alien dodges, kicks you in the shin, and runs away!\nIt’s a fast little bugger and vanishes into the woods.\nYour phone takes no damage because it’s an old Nokia phone.",
                "choices": {
                    "chase_forest": {
                        "text": "Chase after it into the forest",
                        "next_step": 9,
                        "required_item": None
                    },
                    "look_around": {
                        "text": "Run outside but look around before entering the forest",
                        "next_step": 10,
                        "required_item": None
                    }
                }
            },
            8: {
                "text": "The alien dodges, kicks you in the shin, and runs away!\nIt’s a fast little bugger and vanishes into the woods.",
                "choices": {
                    "chase_forest": {
                        "text": "Chase after it into the forest",
                        "next_step": 9,
                        "required_item": None
                    },
                    "look_around": {
                        "text": "Run outside but look around before entering the forest",
                        "next_step": 10,
                        "required_item": None
                    }
                }
            },
            9: {
                "text": "You sprint into the forest. Branches whip against your face, darkness thickens.\nThe alien’s silhouette flickers ahead—then vanishes.\nSuddenly, the ground disappears beneath you and you plunge into a pit.",
                "choices": {
                    "climb_out": {
                        "text": "Climb out and run back",
                        "next_step": 11,
                        "required_item": None
                    }
                }
            },
            10: {
                "text": "You stop at the front door. The alien’s silhouette flickers ahead—then vanishes.\nHowever you notice, than something is lying near the doorstep... It's Melvin's notebook!",
                "choices": {
                    "pick_notebook": {
                        "text": "Pick up the notebook",
                        "next_step": 13,
                        "required_item": None
                    }
                }
            },
            11: {
                "text": "You race back without daring to look behind until you finally stop at the front door.\nThere you notice, that Melvin's notebook lies near the doorstep.",
                "choices": {
                    "pick_notebook": {
                        "text": "Pick up the notebook",
                        "next_step": 13,
                        "required_item": None
                    }
                }
            },
            13: {
                "text": "You open the notebook and see that most of the pages are missing.\nThe remaining notes hint at something important, but it's unclear what exactly.\nInside, the coordinates of three locations are written down.\nLooks like it's time to head back to the airport!",
                "choices": {
                    "end_investigation": {
                        "text": "End the investigation",
                        "next_step": None,
                        "required_item": None
                    }
                }
            }
        }
    }
}

def start():
    print("WeLC0ME TO UФ0tuTKiJa!")
    input("Press ENTER to start")

    user_name = input("Enter your name (otherwise you will be Pekka): ")
    if user_name:
        player["name"] = user_name

    print_separator()

    print(f"Hello, {player['name']}, our best UFO hunter! \nYou've become a legend in paranormal investigations, but now...\nWell... You're stuck in your office, bored and waiting for something exciting...")
    input("Press ENTER to continue")

    print(f"\nOh wait!\n{player['name']}, you hear a notification from your email inbox... Open it?")
    input("Press ENTER to open the email")

    email_text = f"""
    Date: 03 Sept 1999
    Sender: Mel_UFO-Investigator_77

    Yo, {player['name']}, it's your buddy MELVIN from Evergreen!1! Hope you still REMEMBER me, space cowboy
    anyways, i just cant believe what im seeing... its NOT normal! noooo way. This is... PARA-NORMAL, and its HUUUGE. 
    Like, REALLY f*cked up. I NEED your help here, at Evergreen!
    We need 2 meet @ {Fore.GREEN}Denver International Airport{Style.RESET_ALL} tomorrow evening.
    plz dont be late. dont tel anyone about this.

    Cya,
    Melvin
    P.S. I''ve added {Fore.MAGENTA}$100{Style.RESET_ALL} to your bank account for your plane ticket!1! HURRY UP!!
    """

    type_writer(email_text, 0.03)

    input("Press ENTER to continue")

    main_menu()

def main_menu():
    while True:

        print_separator()

        print("Well, what do you want to do next?")
        print(f"1. {Fore.GREEN}Go to the airport{Style.RESET_ALL}")
        print(f"2. {Fore.MAGENTA}Buy equipment {'(For demo purposes go here first)' if player['level'] == 1 else ''}{Style.RESET_ALL}")
        choice = input("Print number of option: ")

        if choice == "1":
            travel()
        elif choice == "2":
            shop()
        else:
            print("There is no options like that")

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

def shop():
    print_separator()

    # TODO replace this stub (these prints) with actual code about shoping and gambling
    print("There will be a store, but for now you get an old Nokia for free")
    print("\nHere is also a list of potentially (in future) reachable items from 'items' list: ")

    for item in items.values():
        print(f"-{item['name']} "
              f"({Fore.MAGENTA}${item['price']}{Style.RESET_ALL}, "
              f"Success chance: {Fore.GREEN}{item['success_chance']}%{Style.RESET_ALL})")

def investigate(ident):
    print_separator()
    # get the investigation data
    investigation = investigations[ident]
    # get how much turns player has
    player["turns"] = investigation["turns_limit"]
    # set current step to first
    step = 1

    # show to user the short story about investigation
    print(f"{investigation['description']}")

    # go through the investigation steps one by one as the player makes choices
    # until there's a reason to stop
    while True:

        # if there's no next step, investigation is done
        if step is None:
            print(f"{investigation['win_text']}")
            player["money"] += investigation["reward"]
            player["level"] += 1
            time.sleep(2)
            break

        # game over, if no turns left
        if player["turns"] <= 0:
            print(f"{investigation['lose_text']}")
            break

        # get the current step data
        step_data = investigation["steps"][step]
        step_description = step_data["text"]
        step_choices_dict = step_data["choices"]
        step_choices_list = list(step_choices_dict.values())

        # print step description
        print(f"{step_description}")

        # print list the available choices from the step
        for number, choice in enumerate(step_choices_list, 1):
            print(f"{number}. {choice['text']}")

        # ask player for their next move
        selected_step_number = int(input("\nSelect your next move by its number: "))

        # get data about selected next move
        if 1 <= selected_step_number <= len(step_choices_list):
            selected_choice = step_choices_list[selected_step_number - 1]

            # ask if the move requires special equipment
            required_item = selected_choice["required_item"]

            # if the next move requires an item
            if required_item:
                # check if player already has the item
                if required_item in player["inventory"]:

                    # take the success chance from the item
                    success_chance = items[required_item]["success_chance"]

                    # check if item use is successful
                    # we "roll the dice" using the random function
                    # to randomly check whether using the item was successful or if the turn was wasted
                    if random.randint(1, 100) <= success_chance:
                        print(f"\nSuccess! The {items[required_item]['name']} worked.")
                        step = selected_choice["next_step"]
                    else:
                        print("\nIt failed! Try again or use another item.")

                else:
                    # if player does not have the item, they can "roll the dice" again without losing a turn
                    print(f"\nYou don't have {items[required_item]['name']}!")
                    continue  # skip turn deduction

            else:
                # move to the next step if there is no required item in the current step
                step = selected_choice["next_step"]

            # in every case we take one turn from the player
            player["turns"] -= 1

        # the function for showing scary reminders, and it is crappy
        # I haven’t found yet  a way to display the scary messages so that they never appear on two consecutive turns
        # but it's still an example
        if step in investigation["steps"]:
            if player["turns"] == investigation["turns_limit"] // 2:
                type_writer(f"\n{random.choice(scary_reminders)}", 0.03)
                time.sleep(0.5)
            elif player["turns"] == 3 and investigation["turns_limit"] > 5:
                type_writer(f"\n{random.choice(scary_reminders)}", 0.03)
                time.sleep(0.5)
            elif player["turns"] == 1 and investigation["turns_limit"] > 6:
                type_writer(f"\n{random.choice(scary_reminders)}", 0.03)
                time.sleep(0.5)

            print_separator()

start()
    






