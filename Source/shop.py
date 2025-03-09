# shop.py

from colorama import Fore, Style
<<<<<<< Updated upstream
from utilities import print_separator
from items import items

def shop():
    print_separator()

    # TODO !SONA ALREADY HAS AN IMPLEMENTATION OF STORE! replace this stub with actual code about shoping and gambling
    print("There will be a store, but for now you get an old Nokia for free")
    print("\nHere is also a list of potentially (in future) reachable items from 'items' list: ")
=======
from utilities import print_separator, type_writer
from database import get_data_from_database, update_data_in_database
from player import get_current_player, update_player

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
    player = get_current_player()

    # This is a temporary thing You can add money here to test it out
    """ new_money = player["money"] + 1000
    update_player("money", new_money, player["id"])
    player["money"] = new_money  # update local player's money to reflect the change """

    print(f"Account balance: {Fore.MAGENTA}${str(player.get('money'))}  \n{Style.RESET_ALL}")
    print("Available items:")
    index = 0
    for index, (key, item) in enumerate(items.items(), 1):
        price = item['price'] if item['price'] is not None else 0
        print(f"{index}. {item['name']}: {item['description']} (Price: ${price})")
        
    print(f"{index+1}. Exit shop")
    print_separator()
    print("What would you like to buy?")
    choice = input("Enter the option number: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == index+1:
            return
        elif 1 <= choice <= index:
            selected_key = list(items.keys())[choice-1]
            selected_item = items[selected_key]
            price = selected_item['price'] if selected_item['price'] is not None else 0

            # Retrieve current player's money.
            if not player:
                print("No player found. Please create a player first.")
                return

            if player.get("money", 0) < price:
                print(f"Insufficient funds to purchase {selected_item['name']} mate. Check your balance again. You have ${player.get('money')}.")
            else:
                new_money = player["money"] - price
                update_player("money", new_money, player["id"])
                print(f"Dude, you've got it! You purchased {selected_item['name']} for ${price}. Your new balance is ${new_money}.")
                
                # Update player's inventory and money in the database.
                query = (f"INSERT INTO inventory (player_id, item, amount) VALUES ({player['id']}, '{selected_item['name']}', 1) "
                         f"ON DUPLICATE KEY UPDATE amount = amount + 1")
                update_data_in_database(query)
        else:
            print("Invalid option.")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    shop()
>>>>>>> Stashed changes

    for item in items.values():
        print(f"-{item['name']} "
              f"({Fore.MAGENTA}${item['price']}{Style.RESET_ALL}, "
              f"Success chance: {Fore.GREEN}{item['success_chance']}%{Style.RESET_ALL})")