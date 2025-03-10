import config
from Source.config import tossNokia
from Source.utilities import yes_no
from utilities import type_writer, print_separator, input_press_enter, input_integer
from notifications import get_messages
from database import *
from player import update_player, get_current_player


def get_inventory():
    if config.tossNokia:
        query = (f'SELECT inventory.item, inventory.amount, items.price, items.item_type, items.description '
                f'FROM inventory '
                f'INNER JOIN items '
                f'ON inventory.item = items.name '
                f'WHERE player_id = {get_current_player()["id"]} '
                f'AND inventory.item NOT IN ("Nokia");')
    else:
        query = (f'SELECT inventory.item, inventory.amount, items.price, items.item_type, items.description '
                f'FROM inventory '
                f'INNER JOIN items '
                f'ON inventory.item = items.name '
                f'WHERE player_id = {get_current_player()["id"]};')
    result = get_data_from_database(query)
    print(len(result))
    if result:
        columns = ["name", "amount", "price", "type", "description"]
        inventory = []
        for oi in range(len(result)):
            inventory.append({columns[i]: result[oi][i] for i in range(len(columns))})
        return inventory
    else:
        return {}


def list_inventory():
    inventory = get_inventory()
    inventoryLength = len(inventory)

    for i in range(inventoryLength):
        if inventory[i]["amount"] is None:
            print(f'{i+1}) {inventory[i]["name"]}')
        else:
            print(f'{i + 1}) {inventory[i]["name"]} {inventory[i]["amount"]}')

    print(f'{inventoryLength+1}) Go back\n')
    action = input_integer(get_messages("COMMON_PRINT_OPTION_NUMBER"))

    if action>0 and action<=inventoryLength:
        item = inventory[action-1]
        print(item)
        print(item['description'])

        if item['name'] != 'Nokia':
            print(f'You have {item["amount"]} left\n')

        choose = yes_no('Do you want to use this item? y/n\n')
        print(choose)

        if choose == 'y':
            if item['name'] == 'Nokia':
                config.tossNokia = True
            else:
                update_inventory(1, get_current_player()['id'], item['name'])
            return item
        if choose == 'n':
            list_inventory()
    elif action==inventoryLength+1:
        print('bye')
        return 'exit'
    else:
        print("There's no such option")
        input_press_enter('')
        list_inventory()


def get_item(pick):
    for i in get_inventory():
        if i['name'] == pick:
            print(i['amount'])
            break

def update_inventory(value, player_id, item):
    amount = 0
    for i in get_inventory():
        if i['name'] == item:
            amount = i['amount']
    if amount-value<0:
        print("woah hey you don't have that many items!")
        return 'nope'
    elif amount-value==0:
        update_data_in_database(f'DELETE FROM inventory WHERE player_id = {player_id} AND item = "{item}";')
    else:
        update_data_in_database(f'UPDATE inventory SET amount = {amount-value} WHERE player_id = {player_id} AND item = "{item}"')

#print(get_inventory()[0])

#print(get_item('Salt'))
#list_inventory()
#list_inventory()