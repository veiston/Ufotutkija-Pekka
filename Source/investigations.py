# investigations.py

import time
import random

from utilities import type_writer, print_separator,input_integer
from player import *
from items import items
from notifications import SCARY_REMINDERS
player = get_current_player()

player = get_current_player()

investigations = {
    "tutorial": { # story ident, important
        "description": f"{player['name']}, you arrive in the Evergreen to meet Melvin, but your friend doesn't show up\nat the airport by the appointed time. The clock is nearing midnight. Worried, you make\nyour way to Melvin's home, using the last known address he mentioned.\nThe streets are unusually silent and a strange feeling of unease begins to grow.",  # story description
        "airport": "KBNA",  # airport code related to this story
        "reward": 200,  # mission completion reward (money)
        "turns_limit": 100,  # number of attempts allowed for the location
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
                        "text": "Finish the investigation",
                        "next_step": None,
                    }
                },
            }
        }
    },
    "metal_goblin": {
        "description": f"{player['name']}, the coordinates from the infamous notebook have led you to Kentucky, to the village of Kelly\n— a place where strange occurrences have long been the norm. For half a century, Hopkinsville County\nhas intrigued people: at night, household appliances disappear, and witnesses speak of tiny creatures\nwith shimmering skin hiding in the woods. If stolen toasters and radio transmitters hold the key\nto Melvin’s disappearance, it's worth figuring out who is behind this.\n",
        "airport": "KDEN",
        "reward": 250,
        "turns_limit": 12,
        "level": 2,
        "win_text": f"You leave Kelly, but before that, you pick up a floppy disk from the sticky floor of the barn. On it — Melvin's name. What could it mean...",
        "lose_text": f"{player['name']}, you have exhausted all your resources and failed to uncover the mystery.",
        "steps": {
            1: {
                "text": "Where should the investigation begin?\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "go_forest": {
                        "text": "Go into the forest",
                        "next_step": 2,
                    },
                    "go_neighborhood": {
                        "text": "Question the local residents",
                        "next_step": 3,
                    },
                }
            },
            2: {
                "text": "The forest is dark and damp. Among the trees, you notice strange tracks — small, as if made by a child or\na large dog, but with long claws and webbing between the toes. They look fresh. It seems that someone has\nrecently passed through here.\n",
                "can_examine": True,
                "is_examined": False,
                "choices": {
                    "go_neighborhood": {
                        "text": "Question the local residents",
                        "next_step": 3,
                    },
                    "examine": {
                        "text": "Examine the tracks using equipment",
                        "next_step": 6,
                    },
                }
            },
            3: {
                "text": "The locals tell different stories: some have seen shimmering creatures, others have heard strange sounds.\nSome recall an old incident on a farm where someone shot at the creatures, but they didn’t fall. However,\nall that remains of that farm now is an old barn...\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "check_barn": {
                        "text": "Check the old barn",
                        "next_step": 4,
                    },
                    "go_forest": {
                        "text": "Go into the forest",
                        "next_step": 2,
                    },
                }
            },
            4: {
                "text": "Ahead lies the edge of the forest, an open field, and a dilapidated barn — peeling paint, a rusted antenna\non the roof, and... strangely, the sound of a radio coming from inside. Though the shack appears abandoned,\na cold light flickers behind its dirty windows.",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "visit_barn": {
                        "text": "Enter the barn",
                        "next_step": 5,
                    },
                    "go_forest": {
                        "text": "Go into the forest",
                        "next_step": 2,
                    },
                }
            },
            5: {
                "text": "Inside the barn, chaos reigns: satellite dishes, broken TVs, radios with exposed wires. Among the three-toed\ntracks, a transmitter blinks, crackling with fragmented signals. A dim lamp flickers behind a shelf. Someone\nwas clearly here recently, but now — it's empty.",
                "can_examine": True,
                "is_examined": False,
                "choices": {
                    "go_forest": {
                        "text": "Go into the forest",
                        "next_step": 2,
                    },
                    "examine": {
                        "text": "Investigate the barn using equipment",
                        "next_step": 6,
                    }
                }
            },
            6: {
                "text": "Now think twice! After investigating the forest and the old barn, you begin to see a pattern. The strange\nmarks, three-toed footprints, hacked-apart radio equipment, and ripped-down satellite antennas are clearly\nnot of human origin. The equipment you used has confirmed it — this is clearly the work of...\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "choose_mg": {
                        "text": "Metal Goblin. Small, metallic alien creature that steals electronics and hides in the dark.",
                        "next_step": 7,
                    },
                    "choose_nakki": {
                        "text": "Näkki. A damp, elusive ghost figure seen near water, watching silently.",
                        "next_step": 6,
                    },
                    "choose_ghost": {
                        "text": "Wounded Grey. A disoriented, lanky being with hollow eyes. Very aggressive. Looks extraterrestrial.",
                        "next_step": 6,
                    },
                }
            },
            7: {
                "text": "Your instincts were right. Aliens again! You’re starting to understand what’s going on, but there’s still\nnot enough information. Have we checked all the locations from Melvin’s notebook?",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "end_investigation": {
                        "text": "Finish the investigation",
                        "next_step": None,
                    }
                }
            }
        }
    },
    "flatwoods_monster": {
        "description": f"{player['name']}, the coordinates from Melvin's notebook have led you to Flatwoods, Braxton County, West Virginia.\nThis place is a living legend. Half a century ago, something was seen here: a red sphere descending from\nthe sky, a metallic stench in the air, scorched patches of earth where nothing grows to this day.\nThe locals whisper: it has returned. Do you feel it?\n",
        "airport": "KHTS",
        "reward": 300,
        "turns_limit": 15,
        "level": 1,
        "win_text": f"You run out of the forest at full speed and stop only near the bar. On the ground, you see a floppy disk with Melvin's name on it. What the f...",
        "lose_text": f"{player['name']}, your resources have run out, and the mystery remains unsolved.",
        "steps": {
            1: {
                "text": "What should we do in this small, half-empty town?\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "check_bar": {
                        "text": "Enter the bar",
                        "next_step": 2,
                    },
                }
            },
            2: {
                "text": "The bar is nearly empty. The bartender silently wipes a glass. In the corner sits an old man, his eyes\ninflamed, his hands trembling. He says he has seen the red sphere in the forest again.\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "press_old_man": {
                        "text": "Demand more information",
                        "next_step": 3,
                    },
                }
            },
            3: {
                "text": "The old man speaks of a creature. It is tall—about three meters. A red face, a green body. It stands\nin the shadows of the trees, watching.\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "go_forest": {
                        "text": "Go into the forest",
                        "next_step": 4,
                    },
                    "stay_bar": {
                        "text": "Order a beer",
                        "next_step": 11,
                    },
                }
            },
            11: {
                "text": "Nice try, but you don't drink on the job!\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "go_forest": {
                        "text": "Go into the forest",
                        "next_step": 4,
                    },
                }
            },
            9: {
                "text": "We need to check what the strange old man was talking about.",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "go_forest": {
                        "text": "Go into the forest",
                        "next_step": 4,
                    },
                }
            },
            4: {
                "text": "The forest is quiet, but the air is thick with a disgusting, burnt, metallic smell. Underfoot are old\nscorched patches of earth. Your eyes start to burn.\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "inspect_ground": {
                        "text": "Examine the patches",
                        "next_step": 5,
                    },
                    "inspect_trees": {
                        "text": "Examine the trees around",
                        "next_step": 10,
                    },
                }
            },
            10: {
                "text": "Trees look like trees, nothing interesting, but what are these scorched patches beneath you?\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "inspect_ground": {
                        "text": "Examine the patches on the ground",
                        "next_step": 5,
                    },
                }
            },
            5: {
                "text": "The scorched patches are sticky to the touch—some kind of black liquid. The substance reacts to light.\n",
                "can_examine": True,
                "is_examined": False,
                "choices": {
                    "examine": {
                        "text": "Analyze the substance using equipment",
                        "next_step": 6,
                    },
                }
            },
            6: {
                "text": "Did you hear that? A branch snapped above your head. Is something watching you?",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "look_up": {
                        "text": "Look up",
                        "next_step": 7,
                    },
                    "step_back": {
                        "text": "Step back",
                        "next_step": 7,
                    },
                }
            },
            7: {
                "text": "Hissing. Red light. The creature stands—or rather, levitates—in front of you. A towering three-meter\nfigure with burning eyes, a triangular head, and a dark body resembling armor or a cloak. A sharp\nmetallic stench fills the air, and the ground beneath is scorched.\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "choose_mg": {
                        "text": "Metal Goblin. Small, metallic alien creature that steals electronics and hides in the dark.",
                        "next_step": 7,
                    },
                    "choose_braxie": {
                        "text": "Braxie. A towering, faceless entity with glowing red eyes and a metallic hood. It reeks of burning metal and fear.",
                        "next_step": 8,
                    },
                    "choose_ghost": {
                        "text": "Wounded Grey. A disoriented, lanky being with hollow eyes. Very aggressive. Looks extraterrestrial.",
                        "next_step": 7,
                    },
                }
            },
            8: {
                "text": "Run!\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "run": {
                        "text": "Finish the investigation with a heroic escape!",
                        "next_step": None,
                    },
                }
            }
        }
    },
    "nakki": {
        "description": f"{player['name']}, the coordinates in Melvin's notebook lead you to Aberdeen, Washington. Here, by the banks\nof the Chihalis River, something strange is happening - late at night, fishermen saw a dark\nfigure in the water, then began to find drowned people. People say that at night someone splashes\nin the water, and in the morning they find ashy gray slime on the pier. Who is it and what does it\nhave to do with Melvin?\n",
        "airport": "KSEA",
        "reward": 300,
        "turns_limit": 20,
        "level": 2,
        "win_text": f"{player['name']}, lost in thought, you slowly wander along the pier toward your next destination\nwhen you notice a little floppy disk underfoot. Strange symbols cover it, and… Melvin’s name.\nWhat could this mean?",
        "lose_text": f"{player['name']}, you have exhausted all resources and never discovered what lurks in the water.",
        "steps": {
            1: {
                "text": "Where should the investigation begin?\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "go_port": {
                        "text": "Question the fishermen",
                        "next_step": 2,
                    },
                    "go_river": {
                        "text": "Investigate the riverbanks",
                        "next_step": 3,
                    },
                }
            },
            2: {
                "text": "The fishermen are scared. One of them saw something near the pier. They claim that in the morning,\ndark patches of an unknown substance were found there.\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "go_river": {
                        "text": "Head to the pier",
                        "next_step": 3,
                    },
                }
            },
            3: {
                "text": "The pier is old, its planks covered in moss, but distinct tracks of long, thin… fingers\nare imprinted on them. Near the tracks, there is a strange, slimy residue.\n",
                "can_examine": True,
                "is_examined": False,
                "choices": {
                    "wait_pier": {
                        "text": "Wait by the pier",
                        "next_step": 4,
                    },
                    "examine": {
                        "text": "Examine the substance using equipment",
                        "next_step": 5,
                    },
                }
            },
            4: {
                "text": "Midnight. The silence is suffocating, yet ripples appear on the water—despite the windless night.\nSomething is moving in the shallows... A shadow beneath the water slowly approaches the pier.\n",
                "can_examine": True,
                "is_examined": False,
                "choices": {
                    "search_pier": {
                        "text": "Inspect the pier",
                        "next_step": 3,
                    },
                    "examine": {
                        "text": "Examine the water using equipment",
                        "next_step": 5,
                    },
                }
            },
            5: {
                "text": "You remain still, watching as the underwater shadow takes shape and silently climbs onto the pier -\ntoo silently. It is tall, almost inhumanly elongated. Its skin is pale as river sludge, with a wet, glossy\nsheen, as if it were made of water itself.\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "what_the": {
                        "text": "Mutter: `What the...?`",
                        "next_step": 6,
                    }
                }
            },
            6: {
                "text": "Suddenly, an unbearable chill washes over you. Somewhere in the distance, a dog starts barking.\nThe creature reaches toward you with its translucent, vine-like fingers. Ah! It burns!\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "step_back": {
                        "text": "Take a step back",
                        "next_step": 8,
                    },
                    "scream": {
                        "text": "Scream",
                        "next_step": 7,
                    },
                    "attack": {
                        "text": "Attack",
                        "next_step": 9,
                    },
                }
            },
            7: {
                "text": "You scream as loud as you can, but the silence remains impenetrable. How is that possible?\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "attack": {
                        "text": "Attack",
                        "next_step": 9,
                    },
                }
            },
            8: {
                "text": "You try to step back, but the creature's grip tightens like a vise. It’s dragging you toward the water!\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "attack": {
                        "text": "Attack",
                        "next_step": 9,
                    },
                }
            },
            9: {
                "text": "You prepare to fight, but at that moment, an old, nearly empty salt shaker slips out of your backpack.\nThe creature sees the salt and instantly recoils, releasing you without a sound, before slipping\nsilently back into the water.\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "stare_water": {
                        "text": "Stare dumbfounded at the water",
                        "next_step": 10,
                    },
                }
            },
            10: {
                "text": "A water-dwelling creature that drowns people, leaves ectoplasm behind, and fears salt... I’ve heard\nof this before. Of course! It was something from my childhood. My older brother used to tell me about...\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "choose_nakki": {
                        "text": "Näkki. A ghostly water entity that lures its victims to the depths.",
                        "next_step": 11,
                    },
                    "choose_mg": {
                        "text": "Metal Goblin. Small, metallic alien creature that steals electronics and hides in the dark.",
                        "next_step": 10,
                    },
                    "choose_braxie": {
                        "text": "Braxie. A towering, faceless alien entity with glowing red eyes and a metallic hood. It reeks of burning metal and fear.",
                        "next_step": 10,
                    },
                }
            },
            11: {
                "text": "Ghosts! How unusual. What have you gotten yourself into, Melvin?\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "end_investigation": {
                        "text": "Finish the investigation",
                        "next_step": None,
                    }
                }
            },
        }
    },
    "endgame": {
        "description": f"{player['name']}, strange creatures, floppy disks, notebook pages—every investigation\nsite had traces linked to Melvin. It's time to uncover the truth.\n",
        "airport": "KBNA",
        "reward": 500,
        "turns_limit": 4,
        "level": 3,
        "win_text": f"{player['name']}, it's time to accept congratulations! You managed to stop Melvin and escape this nightmare, but what will you do with this knowledge now?..",
        "lose_text": f"{player['name']}, you failed to resist Melvin. Now you are part of his insane plan.",
        "steps": {
            1: {
                "text": f"You return to Melvin’s house. Everything looks the same as the first time,\nbut now you notice the details: strange devices, flickering screens, wires\nstretching from room to room. The air is filled with the scent of burning\nand something... chemical.\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "warn": {
                        "text": "Insert the assembled floppies into Melvin's laptop.",
                        "next_step": 2,
                    },
                }
            },
            2: {
                "text": f"You insert the floppy disks into Melvin's old computer. This time, strange\nsymbols appear on the screen, followed by fragments of text:\n'Project Assimilation.\nStage 1: Contact.\nStage 2: Transformation.\nStage 3: Colonization.'\n\nThe last disk contains a video: Melvin—but not quite Melvin. His eyes glow,\nand his voice sounds mechanical: 'PRepare THe f00th0ld. EarTH wiLL be 0urs.'\n\nWhat does all this mean?\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "warn": {
                        "text": "Call someone.",
                        "next_step": 3,
                    },
                }
            },
            3: {
                "text": "You pull out your phone to warn your colleagues — someone must be able\nto stop this madness, but at that moment, you hear footsteps.\n\nMelvin steps out from the shadows of the office, but he is no longer\nthe Melvin you once knew. His eyes glow with an unnatural light, his skin\nappears to be partially covered in metallic scales. He speaks, but his voice\nsounds strange, as if two people are talking at once:\n'Y0u're t00 laTE, space c0wb0y. It's alREady begUN.'\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "try_reason": {
                        "text": "'Melvin, stop! This isn't you!'",
                        "next_step": 4,
                    },
                }
            },
            4: {
                "text": f"Melvin freezes for a moment. His eyes flicker:\n'I... I can't stop this. They're inside me. They're everywhere.'\n\nSuddenly, his face contorts, and he laughs—a sound more like grinding metal:\n'THey f0und mE. THey ch0se mE. I am m0re THan huMAn n0w. I am THe veSSel.\nSoon, EVeryTHing wiLL change. EarTH will bec0me a new... c0l0ny. AnD y0u, {player['name']}...\nWe neED experts lIKe y0u. Y0u muST bec0me part 0f this. WiLLingly... 0r n0t.'\n\nMelvin steps forward, and you see he is holding a syringe filled with a thick, shimmering liquid.\n",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "fight": {
                        "text": "Fight!",
                        "next_step": 4,
                    },
                }
            },
        }
    },
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
            # Retrieve the full, updated player data. This returns a dictionary with an 'id' key.
            current = get_current_player()
            # Ensure current money and player_level are valid numbers.
            current_money = current.get("money")
            if current_money is None:
                current_money = 0
            current_level = current.get("player_level")
            if current_level is None:
                current_level = 0

            new_money = current_money + investigation["reward"]
            new_level = current_level + 1
            # Update player's data with the new money and level.
            update_player("money", new_money, current["id"])
            update_player("player_level", new_level, current["id"])
            break

        if turns <= 0:
            print(f"{investigation['lose_text']}")
            # TODO: Fighting logic could be placed here.
            break

        if len(investigation["steps"]) > 4 and ((turns == 3 and investigation["turns_limit"] > 3) or (turns == 1 and investigation["turns_limit"] <= 3)):
            type_writer(f"{random.choice(SCARY_REMINDERS)}\nYou have {turns} turns left", 0.03)
            time.sleep(2)
            print_separator()

        step_data = investigation["steps"][step]
        step_choices_dict = step_data["choices"]
        step_choices_list = list(step_choices_dict.values())
        step_description = step_data["text"] if not step_data["is_examined"] else f"{step_data["text"]}\n\nYou’ve already examined this area... What's next?\n"

        print(step_description)

        for number, choice in enumerate(step_choices_list, 1):
            # Skip re-displaying the "examine" option if already examined.
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

if __name__ == "__main__":
    while True:
        print_separator()
        print("Investigations Menu:")
        keys = list(investigations.keys())
        for i, inv in enumerate(keys, 1):
            print(f"{i}. {inv}")
        print(f"{len(keys)+1}. Exit")
        print_separator()
        choice = input_integer("Select an investigation by its number: ")
        if choice == len(keys)+1:
            print("Exiting investigation menu...")
            break
        elif 1 <= choice <= len(keys):
            investigate(keys[choice-1])
        else:
            print("No such option. Please try again.")