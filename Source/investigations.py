# investigations.py

import time
import random

from utilities import type_writer, print_separator,input_integer
from player import player
from items import items
from notifications import SCARY_REMINDERS

# TODO new stories should be added here
# TODO logic of fighting can be added here. For example you create a dictionary of monsters, where each monster has hp and damage. Then you add an hp key for the player. Then you include monsters in the story steps, just like items are currently added. And you also add damage to items
# TODO logic of interview can be added here. For example you create a dictionary of conversation partners, where each partner has some kind of power scale and a list of questions. Then you add a key with the same power scale for the player. Then you include interrogations in the story steps, just like items are currently added. Finally you develop the logic where your scale influences the game without adding many new entities
investigations = {
    "tutorial": { # story ident, important
        "description": f"{player['name']}, you arrive in the Evergreen to meet Melvin, but your friend doesn't show up\nat the airport by the appointed time. The clock is nearing midnight. Worried, you make\nyour way to Melvin's home, using the last known address he mentioned.\nThe streets are unusually silent and a strange feeling of unease begins to grow.",  # story description
        "airport": "KDEN",  # airport code related to this story
        "reward": 200,  # mission completion reward (money)
        "turns_limit": 10,  # number of attempts allowed for the location
        "level": 1,  # location level, must match the player's level to access
        "win_text":  f"{player['name']}, it looks like you now have to find out what happened to Melvin\nand where the mysterious coordinates from his notebook will lead you.\nYou receive $200 for new flights.",
        "lose_text": f"{player['name']}, your resources have run out, and now you lose.",
        "steps": {
            1: {
                "text": "\nUpon arriving you find Melvin’s car still parked in his yard and the door to his house is ajar.\nIn the air, you can smell the smoke. Suddenly, you get a headache.\nYou call out for Melvin, but there’s no answer.“Something about this reminds me...\nI’m sure someone unusual has visited Melvin. It’s best to investigate the house and find out who,”\nyou decide and head inside.\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "go_office": {
                        "text": "Go to the office",
                        "next_step": 2,
                    },
                    "go_kitchen": {
                        "text": "Go to the kitchen",
                        "next_step": 3,
                    },
                }
            },
            2: {
                "text": "You enter the office. The floor is covered with strange marks, unlike anything human,\nbut they definitely have a shape. It's hard to tell what (or who) caused them without a closer look.\nMaybe you should use your equipment.\n",
                "can_examine": True,
                "is_examined": False,
                "choices": {
"                   search_desk": {
                        "text": "Search the desk drawers" ,
                        "next_step": 5,
                    },
                    "go_kitchen": {
                        "text": "Go to the kitchen",
                        "next_step": 3,
                    },
                    "examine": {
                        "text": "Examine the room with equipment",
                        "next_step": 6,
                    }
                }
            },
            3: {
                "text": "You enter the kitchen. In the air, there’s a strange chemical smell,\nbut without equipment, it’s hard to tell what (or who) caused it.\n",
                "can_examine": True,
                "is_examined": False,
                "choices": {
                    "investigate_shelf": {
                        "text": "Investigate the shelf with with groceries" ,
                        "next_step": 4,
                    },
                    "go_office": {
                        "text": "Go to the office",
                        "next_step": 2,
                    },
                    "examine": {
                        "text": "Examine the room with equipment",
                        "next_step": 6,
                    }
                }
            },
            4: {
                "text": "You are looking at the shelf with groceries. Cans of tuna, beans, and an old chocolate bar.\nNothing unusual.\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "go_kitchen": {
                        "text": "Return to the kitchen",
                        "next_step": 3,
                    },

                }
            },
            5: {
                "text": "You are searching Melvin’s desk and find his laptop.\nYou open it and go to Melvin’s research folder, but all the files are encrypted.\nSuch a shame.\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "go_office": {
                        "text": "Return to the office",
                        "next_step": 2,
                    },

                }
            },
            6: {
                "text": "Now think twice! After investigating all rooms, you begin to see a pattern.\nThe strange marks and smells in each room are clearly not of human origin.\nThe equipment you used has confirmed it — this is clearly the work of...\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "choose_alien": {
                        "text": "Unknown Alien",
                        "next_step": 7,
                    },
                    "choose_ghost": {
                        "text": "The Lady in White",
                        "next_step": 6,
                    },
                    "choose_cryptid": {
                        "text": "Bigfoot",
                        "next_step": 6,
                    },
                },
            },
            7: {
                "can_examine": False,
                "is_examined": False,
                "text": "You don’t believe it yourself, but there is no mistake… Aliens! Melvin, where are you?\nSuddenly, in the corner of the room, you notice Melvin’s notebook.\nMost of the pages have been torn out with inhuman strength,\nand on the remaining ones — strange symbols and the coordinates of three locations.\nWell, now it’s clear where to search for your friend\n(and who you’ll have to face along the way).",
                "choices": {
                    "end_investigation": {
                        "text": "End the investigation",
                        "next_step": None,
                    }
                },
            }
        }
    }
}

def investigate(ident):
    print_separator()

    investigation = investigations[ident]
    turns = investigation["turns_limit"]
    step = 1

    print(f"{investigation['description']}")

    while True:
        if step is None:
            print(f"{investigation['win_text']}")
            player["money"] += investigation["reward"]
            player["level"] += 1
            break

        if turns <= 0:
            print(f"{investigation['lose_text']}")
            # TODO FIGHTING INSTEAD OF lose_text HERE
            # Example
            # fighting_result = fight() # fight() return True if you won and False if you lose
            # if fighting_result == True:
            #     print(f"{investigation['win_text']}")
            # else:
            #     print(f"{investigation['lose_text']}")
            # break
            break

        if (turns == 3 and investigation["turns_limit"] > 3) or (turns == 1 and investigation["turns_limit"] <= 3):
            type_writer(f"{random.choice(SCARY_REMINDERS)}\nYou have {turns} turns left", 0.03)
            time.sleep(2)
            print_separator()

        step_data = investigation["steps"][step]
        step_choices_dict = step_data["choices"]
        step_choices_list = list(step_choices_dict.values())
        step_description = step_data["text"] if not step_data["is_examined"] else "FYI, you’ve already examined this area... What's next?\n"

        print(step_description)

        for number, choice in enumerate(step_choices_list, 1):
            if step_data["is_examined"] and list(step_choices_dict.keys())[number - 1] == "examine":
                continue
            print(f"{number}. {choice['text']}")

        while True:
                selected_step_number = input_integer("\nSelect your next move by its number: ")
                if 1 <= selected_step_number <= len(step_choices_list):
                    break
                else:
                    print("Dude, there are no such options here, try again")

        selected_choice = step_choices_list[selected_step_number - 1]
        selected_key = list(step_choices_dict.keys())[selected_step_number - 1]

        if selected_key == "examine" and not step_data["is_examined"]:
            examine()
            investigation["steps"][step]["is_examined"] = True

            is_all_explored = True
            for step_data in investigation["steps"].values():
                if step_data["can_examine"] and not step_data["is_examined"]:
                    is_all_explored = False
                    break

            if is_all_explored:
                step = selected_choice["next_step"]
            else:
                continue
        else:
            step = selected_choice["next_step"]

        turns -= 1

        print_separator()

def examine():
    print_separator()
    # TODO
    print('TODO The user uses items and actions. The user returns to the room.')
    print_separator()
    return True
