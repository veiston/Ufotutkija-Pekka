# player.py

player = {
    "name": "Pekka",  # the player's default name is Pekka, but they can change it
    "investigation": '', # the unique key of current investigation
    "airport": "EFHK",  # this is Helsinki-Vantaan lentoasema, the starting point
    "money": 100,  # player needs money for the shop and flights
    "level": 1,  # player's level determines access to new locations
    "inventory": ["nokia"]  # here is the list of bought items from "items", example: ["nokia", "salt"]
}

def update_player(key, value):
    player[key] = value
