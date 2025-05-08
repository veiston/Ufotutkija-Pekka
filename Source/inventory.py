import config
from utilities import print_separator, input_press_enter, input_integer, yes_no
from notifications import get_messages
from database import *
from player import Player
from colorama import Fore, Style

# This is the new class Inventory that is now used for working with the inventory
# Below it are the old functions, which might still be used in combat.py. Ideally they should later be added to the class as well

class Inventory:
    def __init__(self):
        self.player = Player()
        self.player.id = Player.current_id

    def get_inventory(self):
        query = (f'SELECT inventory.item, inventory.amount, items.price, items.item_power, items.item_type, items.description '
                 f'FROM inventory '
                 f'INNER JOIN items '
                 f'ON inventory.item = items.name '
                 f'WHERE player_id = {self.player.id};')
        result = get_data_from_database(query)
        if result:
            columns = ["name", "amount", "price", "power", "type", "description"]
            inventory = []
            for oi in range(len(result)):
                inventory.append({columns[i]: result[oi][i] for i in range(len(columns))})
            return inventory
        else:
            return {}

    def add_item(self, item_name):
        inventory = self.get_inventory()
        for entry in inventory:
            if entry['name'] == item_name:
                new_amount = entry['amount'] + 1
                update_data_in_database(
                    f'UPDATE inventory SET amount = {new_amount} WHERE player_id = {self.player.id} AND item = "{item_name}"'
                )
                return self.get_inventory()

        if item_name == "Nokia":
            update_data_in_database(
                f'INSERT INTO inventory(player_id, item, amount) VALUES ({self.player.id}, "{item_name}", NULL);'
            )
        else:
            update_data_in_database(
                f'INSERT INTO inventory(player_id, item, amount) VALUES ({self.player.id}, "{item_name}", 1);'
            )
        return self.get_inventory()

    def delete_item(self, item_name):
        if item_name == "Nokia":
            return self.get_inventory()
        inventory = self.get_inventory()
        for entry in inventory:
            if entry['name'] == item_name:
                if entry['amount'] > 1:
                    new_amount = entry['amount'] - 1
                    update_data_in_database(
                        f'UPDATE inventory SET amount = {new_amount} WHERE player_id = {self.player.id} AND item = "{item_name}";'
                    )
                elif entry['amount'] == 1:
                    update_data_in_database(
                        f'DELETE FROM inventory WHERE player_id = {self.player.id} AND item = "{item_name}";'
                    )
                return self.get_inventory()


# def get_inventory():
#     player = Player()
#     player.id = Player.current_id
#
#     if config.tossNokia:
#         query = (f'SELECT inventory.item, inventory.amount, items.price, items.item_power, items.item_type, items.description '
#                 f'FROM inventory '
#                 f'INNER JOIN items '
#                 f'ON inventory.item = items.name '
#                 f'WHERE player_id = {player.id} '
#                 f'AND inventory.item NOT IN ("Nokia");')
#     else:
#         query = (f'SELECT inventory.item, inventory.amount, items.price, items.item_power, items.item_type, items.description '
#                 f'FROM inventory '
#                 f'INNER JOIN items '
#                 f'ON inventory.item = items.name '
#                 f'WHERE player_id = {player.id};')
#     result = get_data_from_database(query)
#     if result:
#         columns = ["name", "amount", "price", "power", "type", "description"]
#         inventory = []
#         for oi in range(len(result)):
#             inventory.append({columns[i]: result[oi][i] for i in range(len(columns))})
#         return inventory
#     else:
#         return {}


def list_inventory(): #mainly for combat-purposes, but it might be useful elsewhere too
    inventory = get_inventory()
    inventoryLength = len(inventory)
    openInventory = True

    player = Player()
    player.id = Player.current_id

    while openInventory:
        print_separator()
        print('Inventory\n')

        for i in range(inventoryLength): #numbered list of items you have
            print(f'{i + 1}) {inventory[i]["name"]}')

        print(f'{inventoryLength+1}) Go back\n')
        action = input_integer(get_messages("COMMON_PRINT_OPTION_NUMBER"))

        if action>0 and action<=inventoryLength: #checking if user entered a valid number
            item = inventory[action-1]
            print_separator()
            print(item['description'])

            if item['type'] != 'Healing':
                print(f'Attack power {Fore.RED}{item["power"]}{Style.RESET_ALL}\n')
            else:
                print(f'Healing power {Fore.GREEN}{item["power"]}{Style.RESET_ALL}\n')

            if item['name'] != 'Nokia':
                print(f'You have {item["amount"]} left\n')

            choose = yes_no('Do you want to use this item? y/n\n')

            if choose == 'y':
                if item['name'] == 'Nokia':
                    config.tossNokia = True
                else:
                    update_inventory(-1, player.id, item['name'])
                return item

        elif action==inventoryLength+1: #the last option from the list (Go back)
            print_separator()
            return 'exit'

        else:
            print("There's no such option")
            input_press_enter('')

#
# def update_inventory(value, player_id, item):
#     amount = 0
#     for i in get_inventory(): #search database for the item and how many you have
#         if i['name'] == item:
#             amount = i['amount']
#
#     if amount == 0:
#         update_data_in_database(f'INSERT INTO inventory(player_id, item, amount) VALUES ({player_id}, "{item}", {value});')
#
#     elif amount+value<0:
#         print("woah hey you don't have that many items!")
#         return 'nope'
#
#     elif amount+value==0:
#         update_data_in_database(f'DELETE FROM inventory WHERE player_id = {player_id} AND item = "{item}";')
#
#     else:
#         update_data_in_database(f'UPDATE inventory SET amount = {amount+value} WHERE player_id = {player_id} AND item = "{item}"')
#
#
