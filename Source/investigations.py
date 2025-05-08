# investigations.py
import time
import random
from utilities import type_writer, print_separator,input_integer
from player import Player
from notifications import SCARY_REMINDERS
from combat import battle
from database import update_data_in_database, get_data_from_database

player_instance: Player | None = None
player: dict | None = None

investigations = {
    "tutorial": { # story ident, important
        "ident": "tutorial",
        "description": "{player_name}, you arrive in the Evergreen to meet Melvin, but your friend doesn't show up at the airport by the appointed time. The clock is nearing midnight. Worried, you make your way to Melvin's home, using the last known address he mentioned. The streets are unusually silent and a strange feeling of unease begins to grow.",  # story description
        "airport": "KBNA",  # airport code related to this story
        "city": "Evergreen",
        "reward": 300,  # mission completion reward (money)
        "turns_limit": 100,  # number of attempts allowed for the location
        "max_turns": 100,
        "level": 1,  # location level, must match the player's level to access
        "win_text":  "{player_name}, it looks like you now have to find out what happened to Melvin and where the mysterious coordinates from his notebook will lead you. You receive $300 for new flights and equipment.",
        "lose_text": "{player_name}, your resources have run out, and now you lose.",
        "creature": "Alien",
        "is_completed": False,
        "step": 1,
        "steps": {
            1: {
                "text": "Upon arriving you find Melvin’s car still parked in his yard and the door to his house is ajar. In the air, you can smell the smoke. Suddenly, you get a headache. You call out for Melvin, but there’s no answer.“Something about this reminds me... I’m sure someone unusual has visited Melvin. It’s best to investigate the house and find out who,” you decide and head inside.",
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
                "text": "You enter the office. The floor is covered with strange marks, unlike anything human, but they definitely have a shape. It's hard to tell what (or who) caused them without a closer look. Maybe you should use your equipment.",
                "can_examine": True,
                "is_examined": False,
                "choices": {
"                   search_desk": {
                        "text": "Search the desk" ,
                        "next_step": 5,
                    },
                    "go_kitchen": {
                        "text": "Go to the kitchen",
                        "next_step": 3,
                    },
                    "examine": {
                        "text": "Examine the room",
                        "next_step": 6,
                    }
                }
            },
            3: {
                "text": "You enter the kitchen. In the air, there’s a strange chemical smell, but without equipment, it’s hard to tell what (or who) caused it.",
                "can_examine": True,
                "is_examined": False,
                "choices": {
                    "investigate_shelf": {
                        "text": "Investigate the shelf" ,
                        "next_step": 4,
                    },
                    "go_office": {
                        "text": "Go to the office",
                        "next_step": 2,
                    },
                    "examine": {
                        "text": "Examine the room",
                        "next_step": 6,
                    }
                }
            },
            4: {
                "text": "You are looking at the shelf with groceries. Cans of tuna, beans, and an old chocolate bar. Nothing unusual.",
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
                "text": "You are searching Melvin’s desk and find his laptop. You open it and go to Melvin’s research folder, but all the files are encrypted. Such a shame.",
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
                "text": "Now think twice! After investigating all rooms, you begin to see a pattern. The strange marks and smells in each room are clearly not of human origin. The equipment you used has confirmed it — this is clearly the work of...",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "choose_nakki": {
                        "title": "Näkki",
                        "image": "nakki.png",
                        "text": "A ghostly water entity that lures its victims to the depths.",
                        "is_creature": True,
                        "next_step": 6,
                    },
                    "choose_braxie": {
                        "title": "Braxie",
                        "image": "flatwoodsmonster.png",
                        "is_creature": True,
                        "text": "A towering, faceless alien entity with glowing red eyes and a metallic hood. It reeks of burning metal and fear.",
                        "next_step": 10,
                    },
                    "choose_alien": {
                        "title": "Unknown Alien",
                        "image": "alien.png",
                        "text": "A little gray troublemaker who can’t be knocked out even with a Nokia throw.",
                        "is_creature": True,
                        "next_step": 7,
                    },
                },
            },
            7: {
                "is_last": True,
                "can_examine": False,
                "is_examined": False,
                "text": "You don’t believe it yourself, but there is no mistake… Aliens! Melvin, where are you? Suddenly, in the corner of the room, you notice Melvin’s notebook. Most of the pages have been torn out with inhuman strength, and on the remaining ones — strange symbols and the coordinates of three locations. Well, now it’s clear where to search for your friend (and who you’ll have to face along the way).",
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
        "ident": "metal_goblin",
        "description": "{player_name}, the coordinates from the infamous notebook have led you to Kentucky, to the village of Kelly — a place where strange occurrences have long been the norm. For half a century, Hopkinsville County has intrigued people: at night, household appliances disappear, and witnesses speak of tiny creatures with shimmering skin hiding in the woods. If stolen toasters and radio transmitters hold the key to Melvin’s disappearance, it's worth figuring out who is behind this.",
        "airport": "KDEN",
        "city": "Hopkinsville",
        "reward": 250,
        "turns_limit": 15,
        "max_turns": 15,
        "level": 2,
        "win_text": f"You leave Kelly, but before that, you pick up a floppy disk from the sticky floor of the barn. On it — Melvin's name. What could it mean...",
        "lose_text": "{player_name}, you have exhausted all your resources and failed to uncover the mystery.",
        "creature": "Alien",
        "is_completed": False,
        "step": 1,
        "steps": {
            1: {
                "text": "Where should the investigation begin?",
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
                "text": "The forest is dark and damp. Among the trees, you notice strange tracks — small, as if made by a child or a large dog, but with long claws and webbing between the toes. They look fresh. It seems that someone has recently passed through here.",
                "can_examine": True,
                "is_examined": False,
                "choices": {
                    "go_neighborhood": {
                        "text": "Question the local residents",
                        "next_step": 3,
                    },
                    "examine": {
                        "text": "Examine the tracks",
                        "next_step": 6,
                    },
                }
            },
            3: {
                "text": "The locals tell different stories: some have seen shimmering creatures, others have heard strange sounds. Some recall an old incident on a farm where someone shot at the creatures, but they didn’t fall. However, all that remains of that farm now is an old barn...",
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
                "text": "Ahead lies the edge of the forest, an open field, and a dilapidated barn — peeling paint, a rusted antenna on the roof, and... strangely, the sound of a radio coming from inside. Though the shack appears abandoned, a cold light flickers behind its dirty windows.",
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
                "text": "Inside the barn, chaos reigns: satellite dishes, broken TVs, radios with exposed wires. Among the three-toed tracks, a transmitter blinks, crackling with fragmented signals. A dim lamp flickers behind a shelf. Someone was clearly here recently, but now — it's empty.",
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
                "text": "Now think twice! After investigating the forest and the old barn, you begin to see a pattern. The strange marks, three-toed footprints, hacked-apart radio equipment, and ripped-down satellite antennas are clearly not of human origin. The equipment you used has confirmed it — this is clearly the work of...",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "choose_mg": {
                        "title": "Metal Goblin",
                        "image": "metalgoblin.png",
                        "is_creature": True,
                        "text": "Small, metallic alien creature that steals electronics and hides in the dark.",
                        "next_step": 7,
                    },
                    "choose_nakki": {
                        "title": "Näkki",
                        "image": "nakki.png",
                        "is_creature": True,
                        "text": "A damp, elusive ghost figure seen near water, watching silently.",
                        "next_step": 6,
                    },
                    "choose_braxie": {
                        "title": "Braxie",
                        "image": "flatwoodsmonster.png",
                        "is_creature": True,
                        "text": "A towering, faceless alien entity with glowing red eyes and a metallic hood. It reeks of burning metal and fear.",
                        "next_step": 6,
                    },
                }
            },
            7: {
                "text": "Your instincts were right. Aliens again! You’re starting to understand what’s going on, but there’s still not enough information. Have we checked all the locations from Melvin’s notebook?",
                "can_examine": False,
                "is_examined": False,
                "is_last": True,
                "choices": {
                    "end_investigation": {
                        "text": "Finish the investigation",
                        "next_step": None,
                    }
                }
            }
        }
    },
    "nakki": {
        "ident": "nakki",
        "description": "{player_name}, the coordinates in Melvin's notebook lead you to Aberdeen, Washington. Here, by the banks of the Chihalis River, something strange is happening - late at night, fishermen saw a dark figure in the water, then began to find drowned people. People say that at night someone splashes in the water, and in the morning they find ashy gray slime on the pier. Who is it and what does it have to do with Melvin?",
        "airport": "KSEA",
        "city": "Aberdeen",
        "reward": 300,
        "turns_limit": 20,
        "max_turns": 20,
        "level": 2,
        "win_text": "{player_name}, lost in thought, you slowly wander along the pier toward your next destination when you notice a little floppy disk underfoot. Strange symbols cover it, and… Melvin’s name. What could this mean?",
        "lose_text": "{player_name}, you have exhausted all resources and never discovered what lurks in the water.",
        "creature": "Ghost",
        "is_completed": False,
        "step": 1,
        "steps": {
            1: {
                "text": "Where should the investigation begin?",
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
                "text": "The fishermen are scared. One of them saw something near the pier. They claim that in the morning, dark patches of an unknown substance were found there.",
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
                "text": "The pier is old, its planks covered in moss, but distinct tracks of long, thin… fingers are imprinted on them. Near the tracks, there is a strange, slimy residue.",
                "can_examine": True,
                "is_examined": False,
                "choices": {
                    "wait_pier": {
                        "text": "Wait by the pier",
                        "next_step": 4,
                    },
                    "examine": {
                        "text": "Examine the substance",
                        "next_step": 5,
                    },
                }
            },
            4: {
                "text": "Midnight. The silence is suffocating, yet ripples appear on the water—despite the windless night. Something is moving in the shallows... A shadow beneath the water slowly approaches the pier.",
                "can_examine": True,
                "is_examined": False,
                "choices": {
                    "search_pier": {
                        "text": "Inspect the pier",
                        "next_step": 3,
                    },
                    "examine": {
                        "text": "Examine the water",
                        "next_step": 5,
                    },
                }
            },
            5: {
                "text": "You remain still, watching as the underwater shadow takes shape and silently climbs onto the pier - too silently. It is tall, almost inhumanly elongated. Its skin is pale as river sludge, with a wet, glossy sheen, as if it were made of water itself.",
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
                "text": "Suddenly, an unbearable chill washes over you. Somewhere in the distance, a dog starts barking. The creature reaches toward you with its translucent, vine-like fingers. Ah! It burns!",
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
                "text": "You scream as loud as you can, but the silence remains impenetrable. How is that possible?",
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
                "text": "You try to step back, but the creature's grip tightens like a vise. It’s dragging you toward the water!",
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
                "text": "You prepare to fight, but at that moment, an old, nearly empty salt shaker slips out of your backpack. The creature sees the salt and instantly recoils, releasing you without a sound, before slipping silently back into the water.",
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
                "text": "A water-dwelling creature that drowns people, leaves ectoplasm behind, and fears salt... I’ve heard of this before. Of course! It was something from my childhood. My older brother used to tell me about...",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "choose_nakki": {
                        "title": "Näkki",
                        "image": "nakki.png",
                        "is_creature": True,
                        "text": "A ghostly water entity that lures its victims to the depths.",
                        "next_step": 11,
                    },
                    "choose_mg": {
                        "title": "Metal Goblin",
                        "image": "metalgoblin.png",
                        "is_creature": True,
                        "text": "Small, metallic alien creature that steals electronics and hides in the dark.",
                        "next_step": 10,
                    },
                    "choose_braxie": {
                        "title": "Braxie",
                        "image": "flatwoodsmonster.png",
                        "is_creature": True,
                        "text": "A towering, faceless alien entity with glowing red eyes and a metallic hood. It reeks of burning metal and fear.",
                        "next_step": 10,
                    },
                }
            },
            11: {
                "text": "Ghosts! How unusual. What have you gotten yourself into, Melvin?",
                "can_examine": False,
                "is_examined": False,
                "is_last": True,
                "choices": {
                    "end_investigation": {
                        "text": "Finish the investigation",
                        "next_step": None,
                    }
                }
            },
        }
    },
    "flatwoods_monster": {
        "ident": "flatwoods_monster",
        "description": "{player_name}, the coordinates from Melvin's notebook have led you to Flatwoods, Braxton County, West Virginia. This place is a living legend. Half a century ago, something was seen here: a red sphere descending from the sky, a metallic stench in the air, scorched patches of earth where nothing grows to this day. The locals whisper: it has returned. Do you feel it?",
        "airport": "KHTS",
        "city": "Flatwoods",
        "reward": 300,
        "turns_limit": 15,
        "max_turns": 15,
        "level": 2,
        "win_text": "You run out of the forest at full speed and stop only near the bar. On the ground, you see a floppy disk with Melvin's name on it. What the f...",
        "lose_text": "{player_name}, your resources have run out, and the mystery remains unsolved.",
        "creature": "Alien",
        "is_completed": False,
        "step": 1,
        "steps": {
            1: {
                "text": "What should we do in this small, half-empty town?",
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
                "text": "The bar is nearly empty. The bartender silently wipes a glass. In the corner sits an old man, his eyes inflamed, his hands trembling. He says he has seen the red sphere in the forest again.",
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
                "text": "The old man speaks of a creature. It is tall—about three meters. A red face, a green body. It stands in the shadows of the trees, watching.",
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
                "text": "Nice try, but you don't drink on the job!",
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
                "text": "The forest is quiet, but the air is thick with a disgusting, burnt, metallic smell. Underfoot are old scorched patches of earth. Your eyes start to burn.",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "inspect_ground": {
                        "text": "Examine the patches",
                        "next_step": 5,
                    },
                    "inspect_trees": {
                        "text": "Examine the trees",
                        "next_step": 10,
                    },
                }
            },
            10: {
                "text": "Trees look like trees, nothing interesting, but what are these scorched patches beneath you?",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "inspect_ground": {
                        "text": "Examine the patches",
                        "next_step": 5,
                    },
                }
            },
            5: {
                "text": "The scorched patches are sticky to the touch—some kind of black liquid. The substance reacts to light.",
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
                "text": "Hissing. Red light. The creature stands—or rather, levitates—in front of you. A towering three-meter figure with burning eyes, a triangular head, and a dark body resembling armor or a cloak. A sharp metallic stench fills the air, and the ground beneath is scorched.",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "choose_mg": {
                        "title": "Metal Goblin",
                        "is_creature": True,
                        "image": "metalgoblin.png",
                        "text": "Metal Goblin. Small, metallic alien creature that steals electronics and hides in the dark.",
                        "next_step": 7,
                    },
                    "choose_braxie": {
                        "title": "Braxie",
                        "is_creature": True,
                        "image": "flatwoodsmonster.png",
                        "text": "A towering, faceless entity with glowing red eyes and a metallic hood. It reeks of burning metal and fear.",
                        "next_step": 8,
                    },
                    "choose_nakki": {
                        "title": "Näkki",
                        "image": "nakki.png",
                        "is_creature": True,
                        "text": "A ghostly water entity that lures its victims to the depths.",
                        "next_step": 7,
                    },
                }
            },
            8: {
                "text": "Run!",
                "can_examine": False,
                "is_examined": False,
                "is_last": True,
                "choices": {
                    "run": {
                        "text": "Finish the investigation with a heroic escape!",
                        "next_step": None,
                    },
                }
            }
        }
    },
    "endgame": {
        "ident": "endgame",
        "description": "{player_name}, strange creatures, floppy disks, notebook pages — every investigation site had traces linked to Melvin. It's time to uncover the truth.",
        "airport": "KBNA",
        "city": "Evergreen",
        "reward": 500,
        "turns_limit": 4,
        "max_turns": 4,
        "level": 3,
        "win_text": "{player_name}, it's time to accept congratulations! You managed to stop Melvin and escape this nightmare, but what will you do with this knowledge now?..",
        "lose_text": "{player_name}, you failed to resist Melvin. Now you are part of his insane plan.",
        "creature": "Melvin",
        "is_completed": False,
        "step": 1,
        "steps": {
            1: {
                "text": f"You return to Melvin’s house. Everything looks the same as the first time, but now you notice the details: strange devices, flickering screens, wires stretching from room to room. The air is filled with the scent of burning and something... chemical.",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "warn": {
                        "text": "Insert the assembled floppies into Melvin's laptop",
                        "next_step": 2,
                    },
                }
            },
            2: {
                "text": f"You insert the floppy disks into Melvin's old computer. This time, strange symbols appear on the screen, followed by fragments of text:\n\n'Project Assimilation.\n\nStage 1: Contact.\nStage 2: Transformation.\nStage 3: Colonization.'\n\nThe last disk contains a video: Melvin—but not quite Melvin. His eyes glow, and his voice sounds mechanical:\n\n'PRepare THe f00th0ld. EarTH wiLL be 0urs.'\n\nWhat does all this mean?",
                "can_examine": False,
                "is_examined": False,
                "choices": {
                    "warn": {
                        "text": "Call someone",
                        "next_step": 3,
                    },
                }
            },
            3: {
                "text": "You pull out your phone to warn your colleagues — someone must be able to stop this madness, but at that moment, you hear footsteps.\n\nMelvin steps out from the shadows of the office, but he is no longer the Melvin you once knew. His eyes glow with an unnatural light, his skin appears to be partially covered in metallic scales. He speaks, but his voice sounds strange, as if two people are talking at once:\n\n'Y0u're t00 laTE, space c0wb0y. It's alREady begUN.'",
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
                "text": "Melvin freezes for a moment. His eyes flicker:\n'I... I can't stop this. They're inside me. They're everywhere.'\n\nSuddenly, his face contorts, and he laughs—a sound more like grinding metal:\n'THey f0und mE. THey ch0se mE. I am m0re THan huMAn n0w. I am THe veSSel. Soon, EVeryTHing wiLL change. EarTH will bec0me a new... c0l0ny. AnD y0u... We neED experts lIKe y0u. Y0u muST bec0me part 0f this. WiLLingly... 0r n0t.'\n\nMelvin steps forward, and you see he is holding a syringe filled with a thick, shimmering liquid.",
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
    global player_instance, player
    player_instance = Player()
    player_instance.id = Player.current_id
    player = player_instance.get_current()

    player_name = player.get("name", "Player")
    story_template = investigations[ident]
    investigation = eval(str(story_template).replace("{player_name}", player_name))
    investigations[ident] = investigation

    print_separator()

    turns = investigation["turns_limit"]
    step = 1

    print(f"{investigation['description']}")

    while True:
        if step is None:
            print(f"{investigation['win_text']}")
            investigation["is_completed"] = True

            current = player
            current_money = current.get("money", 0)
            current_level = current.get("player_level", 1)

            new_money = current_money + investigation["reward"]
            new_level = current_level

            player_instance.update({"money": new_money})
            player_instance.update({"player_level": new_level})

            if not has_unfinished_investigations(current_level):
                player["player_level"] += 1
                player_instance.update({"player_level": player["player_level"]})
                print(f"You've reached level {player['player_level']}!")

            break

        if turns <= 0:
            battle_result = battle()
            if battle_result:
                print(f"{investigation['win_text']}")
            else:
                print(f"{investigation['lose_text']}")
            break

        if len(investigation["steps"]) > 4 and ((turns == 3 and investigation["turns_limit"] > 3) or (turns == 1 and investigation["turns_limit"] <= 3)):
            type_writer(f"{random.choice(SCARY_REMINDERS)}\nYou have {turns} turns left", 0.03)
            time.sleep(2)
            print_separator()

        step_data = investigation["steps"][step]
        step_choices_dict = step_data["choices"]
        step_choices_list = list(step_choices_dict.values())
        step_description = step_data["text"] if not step_data["is_examined"] else f"{step_data['text']}\nYou’ve already examined this area... What's next?"

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
            examine(ident)
            investigation["steps"][step]["is_examined"] = True

            is_all_explored = all(
                step_data["is_examined"] if step_data["can_examine"] else True
                for step_data in investigation["steps"].values()
            )

            if is_all_explored:
                step = selected_choice["next_step"]
            else:
                continue
        else:
            step = selected_choice["next_step"]

        turns -= 1
        print_separator()



def get_inventory():
    query = f"""
        SELECT inventory.item, items.description, inventory.amount, items.item_type
        FROM inventory
        LEFT JOIN items ON inventory.item = items.name
        WHERE inventory.player_id = {player["id"]};
    """
    return get_data_from_database(query)

def get_creature_types():
    query = "SELECT name, weakness FROM creature_types;"
    creature_results = get_data_from_database(query)
    return {row[0]: row[1] for row in creature_results}

def update_inventory(selected_item):
    query = f"UPDATE inventory SET amount = amount - 1 WHERE player_id = {player['id']} AND item = '{selected_item}';"
    update_data_in_database(query)

    query = f"DELETE FROM inventory WHERE player_id = {player['id']} AND item = '{selected_item}' AND amount = 0;"
    update_data_in_database(query)

def use_equipment(selected_item, item_type, current_creature, creature_types):
    is_effective = selected_item == "Nokia" or item_type == creature_types.get(current_creature)

    if is_effective:
        confidence = random.randint(40, 95)
        print(f"Your analysis suggests: with {confidence}% confidence, the creature is {current_creature}.")
        return True

    if random.randint(1, 100) <= 5:
        wrong_creatures = list(creature_types.keys())
        guess = random.choice(wrong_creatures)
        confidence = random.randint(10, 30)
        print(f"Your equipment gives an uncertain reading... With {confidence}% confidence, it says, that the creature might be {guess}. Too vague. You should try again.")
    else:
        print("You try using the item, but nothing happens.")

    return False

def examine(investigation_ident):
    inventory_results = get_inventory()

    if not inventory_results:
        print("No items in inventory.")
        return

    creature_types = get_creature_types()
    current_creature = investigations[investigation_ident]["creature"]

    print_separator()

    print("\nYou're going to use the equipment to determine what kind of creature you're dealing with.")
    print("You think it might be: " + ", ".join(creature_types.keys()) + ".")

    while True:
        print("Choose equipment from your inventory to perform a more accurate analysis.")

        inventory = {}
        for index, (item, description, amount, item_type) in enumerate(inventory_results, 1):
            print(f"{index}. {item} | {description} | {'Unlimited' if amount is None else f'{amount} pcs'}")
            inventory[index] = (item, item_type, amount)

        choice = input_integer("\nSelect an item by its number: ")

        print_separator()

        if choice not in inventory:
            print("Dude, there are no such options here. Try again!")
            continue

        selected_item, item_type, amount = inventory[choice]

        if selected_item != "Nokia" and item_type not in creature_types.values():
            print("Sorry, but you should try again, this item cannot be used here.")
            continue

        if selected_item != "Nokia" and amount is not None:
            update_inventory(selected_item)
            inventory_results = get_inventory()

        if use_equipment(selected_item, item_type, current_creature, creature_types):
            break

def investigation_start():
    player_instance = Player()
    player_instance.id = Player.current_id
    player = player_instance.get_current()
    player_location = player.get("location_ident")

    for ident, story in investigations.items():
        if story["airport"] == player_location and not story["is_completed"]:
            player_name = player.get("name", "Player")

            story["description"] = story["description"].replace("{player_name}", player_name)
            story["win_text"] = story["win_text"].replace("{player_name}", player_name)
            story["lose_text"] = story["lose_text"].replace("{player_name}", player_name)

            return story

    return {"error": "No available investigation."}

def has_unfinished_investigations(current_level):
    for investigation in investigations.values():
        if investigation["level"] == current_level and not investigation["is_completed"]:
            return True
    return False

def investigation_update_step(step):
    player_instance = Player()
    player_instance.id = Player.current_id
    player = player_instance.get_current()
    player_location = player.get("location_ident")

    for ident, story in investigations.items():
        if story["airport"] == player_location and not story["is_completed"]:
            if story["turns_limit"] > 0:
                story["turns_limit"] -= 1

            is_win = step not in story["steps"] and story["turns_limit"] > 0 and story["steps"][story["step"]].get("is_last", False)

            if not is_win:
                story["step"] = step
            else:
                story["is_completed"] = True
                story["turns_limit"] = story["max_turns"]
                story["step"] = 1

                player["money"] += story["reward"]
                player_instance.update({"money": player["money"]})

                if not has_unfinished_investigations(player["player_level"]):
                    player["player_level"] += 1
                    player_instance.update({"player_level": player["player_level"]})

            return {
                "turns_limit": story["turns_limit"],
                "is_win": is_win,
            }

    return {"error": "No available investigation."}

def get_investigations(type):
    investigations_list = []
    for ident, story in investigations.items():
        story_copy = {key: value for key, value in story.items() if key != "steps"}
        if type == 'uncompleted':
            if not story.get("is_completed", False):
                investigations_list.append(story_copy)
        else:
            investigations_list.append(story_copy)
    return investigations_list


if __name__ == "__main__":
    while True:
        print_separator()
        print("Investigations Menu:")
        keys = list(investigations.keys())
        for i, inv in enumerate(keys, 1):
            print(f"{i}. {inv}")
        print(f"{len(keys) + 1}. Exit")
        print_separator()
        choice = input_integer("Select an investigation by its number: ")
        if choice == len(keys) + 1:
            print("Exiting investigation menu...")
            break
        elif 1 <= choice <= len(keys):
            selected_ident = keys[choice - 1]

            # Set location to investigation's airport
            player_instance = Player('Pekka')
            player_instance.add()
            player_instance.id = Player.current_id
            airport_code = investigations[selected_ident]["airport"]
            player_instance.update({"location_ident": airport_code})
            investigate(selected_ident)

            # Reset location back to EFHK after investigation
            player_instance.update({"location_ident": "EFHK"})
        else:
            print("No such option. Please try again.")
