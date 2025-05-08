# shop.py
from database import get_data_from_database, update_data_in_database
from player import Player

def get_shop_items():
    query = "SELECT * FROM items"
    result = get_data_from_database(query)
    items = []
    for row in result:
        item = {
            "name": row[0],
            "price": row[1],
            "item_type": row[2],
            "description": row[3],
            "is_finite": row[4]
        }
        if item["name"] != "Nokia":
            items.append(item)
    return items

def buy_item(item_name):
    player = Player()
    player.id = Player.current_id
    player_data = player.get_current()

    if not player_data:
        return {"error": "Player not found", "status": 404}

    items = get_shop_items()
    selected_item = next((item for item in items if item['name'] == item_name), None)

    if not selected_item:
        return {"error": "Item not found", "status": 404}

    price = selected_item['price'] if selected_item['price'] is not None else 0

    if player_data.get("money", 0) < price:
        return {"error": "Insufficient funds", "status": 400}

    new_money = player_data.get("money") - price
    player.update({"money": new_money})

    query = (
        f"INSERT INTO inventory (player_id, item, amount) VALUES ({player.id}, '{item_name}', 1) "
        f"ON DUPLICATE KEY UPDATE amount = amount + 1"
    )
    update_data_in_database(query)

    return {
        "new_balance": new_money
    }
