# items.py

# plain items for shop
# TODO add new items, but it depends on whether we will have a fight. If we do, then additions should be made depending on the fighting logic. See TODO in investigations.py
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

# TODO I suggest giving the player a Nokia at the beginning and keeping it forever so they always have a backup item for fighting. Somebody needs to decide when exactly the player receives the Nokia at the start and say this information to the player with prints
# NOKIA IS ALWAYS AVAILABLE, BUT HAS REALLY LOW CHANCE FOR SUCCESS!
