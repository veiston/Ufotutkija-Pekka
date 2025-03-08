# shop.py

from colorama import Fore, Style
from utilities import print_separator
from database import get_data_from_database

def get_items_from_database():
    query = "SELECT * FROM items"
    result = get_data_from_database(query)
    items = {}
    for row in result:
        item = {
            "name": row[0],
            "price": row[1],
            "item_type": row[2],
            "description": row[3],
            "is_finite": row[4]
        }
        items[row[0]] = item
    return items

def shop():
    print_separator()
    items = get_items_from_database()

    # TODO
    print("Available items:")
    for index, (key, item) in enumerate(items.items(), 1):
        price = item['price'] if item['price'] is not None else 0
        print(f"{index}. {item['name']}: {item['description']} "
              f"(Price: ${price})")

    print_separator()

