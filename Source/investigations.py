# investigations.py

import time
import random

from utilities import type_writer, print_separator
from player import player
from items import items
from notifications import SCARY_REMINDERS

# TODO new stories should be added here
# TODO logic of fighting can be added here. For example you create a dictionary of monsters, where each monster has hp and damage. Then you add an hp key for the player. Then you include monsters in the story steps, just like items are currently added. And you also add damage to items
# TODO logic of interview can be added here. For example you create a dictionary of conversation partners, where each partner has some kind of power scale and a list of questions. Then you add a key with the same power scale for the player. Then you include interrogations in the story steps, just like items are currently added. Finally you develop the logic where your scale influences the game without adding many new entities
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

# TODO it is really big and ugly function, it should be divided on smaller functions. Also maybe the logic of throwing the Nokia should be removed from here and added as part of the fighting mechanic. If we do not have fighting mechanic, then part with items should be just additional function
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
                type_writer(f"\n{random.choice(SCARY_REMINDERS)}", 0.03)
                time.sleep(0.5)
            elif player["turns"] == 3 and investigation["turns_limit"] > 5:
                type_writer(f"\n{random.choice(SCARY_REMINDERS)}", 0.03)
                time.sleep(0.5)
            elif player["turns"] == 1 and investigation["turns_limit"] > 6:
                type_writer(f"\n{random.choice(SCARY_REMINDERS)}", 0.03)
                time.sleep(0.5)

            print_separator()
