# player.py
from database import *
current_player_id = None

# player = {
#     "name": "Pekka",  # the player's default name is Pekka, but they can change it
#     "airport": 'QWE', # the unique key of current investigation
#     "money": 100,  # player needs money for the shop and flights
#     "level": 1,  # player's level determines access to new locations
#     "inventory": ["nokia"]  # here is the list of bought items from "items", example: ["nokia", "salt"]
# }

def reset_player():
    global current_player_id
    current_player_id = None
    update_data_in_database("DELETE FROM inventory")
    update_data_in_database("ALTER TABLE inventory AUTO_INCREMENT = 1")
    update_data_in_database("DELETE FROM player")
    update_data_in_database("ALTER TABLE player AUTO_INCREMENT = 1")

def update_player(field, new_value, player_id):
    update_data_in_database(f"UPDATE player SET {field} = '{new_value}' WHERE id = {player_id}")

def add_player(new_player_name):
    reset_player()
    global current_player_id

    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='ufo_peli',
        user='root',  # Attention! do not forget to replace user and password with yours
        password='1234',
        autocommit=True,
        collation="utf8mb4_unicode_ci"
    )

    if new_player_name:
        query = f"INSERT INTO player (name) VALUES ('{new_player_name}')"
    else:
        query = "INSERT INTO player (name, location_ident, money, player_level) VALUES ('Pekka', 'KBNA', 100, 1)"

    cursor = connection.cursor()
    cursor.execute(query)
    cursor.execute("SELECT LAST_INSERT_ID()")
    result = cursor.fetchall()

    if result and result[0]:
        current_player_id = result[0][0]

    cursor.close()
    connection.close()

def get_current_player():
    global current_player_id
    if current_player_id:
        query = f"SELECT * FROM player WHERE id = {current_player_id}"
        result = get_data_from_database(query)
        if result:
            columns = ["id", "name", "location_ident", "hp", "attack", "money", "player_level"]
            player_data = result[0]
            player = {columns[i]: player_data[i] for i in range(len(columns))}
            return player
    else:
        return {}

add_player('')

# Test block
if __name__ == "__main__":
    test_player = get_current_player()
    if test_player:
        print("Current player data:")
        for key, value in test_player.items():
            print(f"{key}: {value}")
    else:
        print("ERROR: No player.")
