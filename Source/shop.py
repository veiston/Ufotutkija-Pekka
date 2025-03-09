# shop.py

from colorama import Fore, Style
from utilities import print_separator
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

    # This is a temporary thing You can add more money here to test it out by uncommenting this folllowing block
    """ new_money = player["money"] + 1000
    update_player("money", new_money, player["id"])
    player["money"] = new_money  # update local player's money to reflect the change """

    print(f"Account balance: {Fore.MAGENTA}${str(player.get('money'))}  \n{Style.RESET_ALL}")
    print("Available items:")
    display_index = 1
    filtered_items = []
    for key, item in items.items():
        if item['name'] == "Nokia":
            continue
        filtered_items.append((key, item))
        price = item['price'] if item['price'] is not None else 0
        print(f"{display_index}. {item['name']}: {item['description']} (Price: ${price})")
        display_index += 1
        
    print(f"{display_index}. Exit shop")
    print_separator()
    print("What would you like to buy?")
    choice = input("Enter the option number: ")
    if choice.isdigit():
        choice = int(choice)  # remove the +1 adjustment
        if choice == display_index:
            return
        elif 1 <= choice < display_index:
            # Use the filtered_items list for selection
            selected_key, selected_item = filtered_items[choice - 1]
            price = selected_item['price'] if selected_item['price'] is not None else 0

            # Retrieve current player's money.
            if not player:
                print("ERROR: No player found. Please create a player first.")
                return

            # Check if the player has enough money
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
        print("Invalid airport_data = get_airport_data(airport_symbol)input.")

if __name__ == "__main__":
    while True:
     shop()