# player.py

player = {
    "name": "Pekka",  # the player's default name is Pekka, but they can change it
    "airport": 'QWE', # the unique key of current investigation
    "money": 100,  # player needs money for the shop and flights
    "level": 1,  # player's level determines access to new locations
    "inventory": ["nokia"]  # here is the list of bought items from "items", example: ["nokia", "salt"]
}

def update_player(key, value):
    player[key] = value
