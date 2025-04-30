# shop.py

from colorama import Fore, Style
from utilities import print_separator, clear_screen
from database import get_data_from_database, update_data_in_database
from player import Player
from gambling_manager import gambling_menu

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
    clear_screen()
    print_separator()
    items = get_items_from_database()
    player = Player()
    player.id = Player.current_id
    player_data = player.get_current()

    # This is a temporary thing You can add more money here to test it out by uncommenting this folllowing block
    """ new_money = player_data["money"] + 1000
    player.update({"money": new_money})
    player_data["money"] = new_money  # update local player's money to reflect the change """

    print(f"Account balance: {Fore.MAGENTA}${str(player_data.get('money'))}  \n{Style.RESET_ALL}")
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
        
    print(f"{display_index}. Gamble and earn more money")
    print(f"{display_index + 1}. Exit shop")
    print_separator()
    print("What would you like to buy?")
    choice = input("Enter the option number: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == display_index:  # Gambling option selected
            gambling_menu()
            return
        elif choice == display_index + 1:  # Exit shop
            return
        elif 1 <= choice < display_index:
            selected_key, selected_item = filtered_items[choice - 1]
            price = selected_item['price'] if selected_item['price'] is not None else 0

            # Retrieve current player's money.
            if not player_data:
                print("ERROR: No player found. Please create a player first.")
                return
            
            # Check if the player has enough money
            if player_data.get("money", 0) < price:
                print(f"Insufficient funds to purchase {selected_item['name']} mate. Check your balance again. You have ${player.get('money')}.")
            else:
                new_money = player_data.get("money") - price
                player.update({"money": new_money})
                print(f"Dude, you've got it! You purchased {selected_item['name']} for ${price}. Your new balance is ${new_money}.")
                
                # Update player's inventory in the database.
                query = (f"INSERT INTO inventory (player_id, item, amount) VALUES ({player.id}, '{selected_item['name']}', 1) "
                         f"ON DUPLICATE KEY UPDATE amount = amount + 1")
                update_data_in_database(query)
        else:
            print("Invalid option.")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    player = Player('Test dude')
    player.add()
    while True:
        shop()