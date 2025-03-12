import config
from utilities import print_separator, input_press_enter, input_integer, yes_no
from notifications import get_messages
from database import *
from player import get_current_player
from colorama import Fore, Style


def get_inventory():
    if config.tossNokia:
        query = (f'SELECT inventory.item, inventory.amount, items.price, items.item_power, items.item_type, items.description '
                f'FROM inventory '
                f'INNER JOIN items '
                f'ON inventory.item = items.name '
                f'WHERE player_id = {get_current_player()["id"]} '
                f'AND inventory.item NOT IN ("Nokia");')
    else:
        query = (f'SELECT inventory.item, inventory.amount, items.price, items.item_power, items.item_type, items.description '
                f'FROM inventory '
                f'INNER JOIN items '
                f'ON inventory.item = items.name '
                f'WHERE player_id = {get_current_player()["id"]};')
    result = get_data_from_database(query)
    if result:
        columns = ["name", "amount", "price", "power", "type", "description"]
        inventory = []
        for oi in range(len(result)):
            inventory.append({columns[i]: result[oi][i] for i in range(len(columns))})
        return inventory
    else:
        return {}


def list_inventory(): #mainly for combat-purposes, but it might be useful elsewhere too
    inventory = get_inventory()
    inventoryLength = len(inventory)
    openInventory = True

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
                    update_inventory(-1, get_current_player()['id'], item['name'])
                return item

        elif action==inventoryLength+1: #the last option from the list (Go back)
            print_separator()
            return 'exit'

        else:
            print("There's no such option")
            input_press_enter('')


def update_inventory(value, player_id, item):
    amount = 0
    for i in get_inventory(): #search database for the item and how many you have
        if i['name'] == item:
            amount = i['amount']

    if amount == 0:
        update_data_in_database(f'INSERT INTO inventory(player_id, item, amount) VALUES ({player_id}, "{item}", {value});')

    elif amount+value<0:
        print("woah hey you don't have that many items!")
        return 'nope'

    elif amount+value==0:
        update_data_in_database(f'DELETE FROM inventory WHERE player_id = {player_id} AND item = "{item}";')

    else:
        update_data_in_database(f'UPDATE inventory SET amount = {amount+value} WHERE player_id = {player_id} AND item = "{item}"')