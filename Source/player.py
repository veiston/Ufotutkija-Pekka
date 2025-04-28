# player.py
from database import *
current_player_id = None

def reset_player():
    global current_player_id
    current_player_id = None
    update_data_in_database("DELETE FROM inventory")
    update_data_in_database("ALTER TABLE inventory AUTO_INCREMENT = 1")
    update_data_in_database("DELETE FROM player")
    update_data_in_database("ALTER TABLE player AUTO_INCREMENT = 1")

def update_player(updates, player_id):
    if not updates:
        return
    set_clause = ', '.join([f"{field} = '{value}'" for field, value in updates.items()])
    query = f"UPDATE player SET {set_clause} WHERE id = {player_id}"
    update_data_in_database(query)

def add_player(new_player_name):
    reset_player()
    global current_player_id

    connection = connect_to_database()

    if new_player_name:
        query = f"INSERT INTO player (name) VALUES ('{new_player_name}')"
    else:
        query = "INSERT INTO player (name, location_ident, money, player_level) VALUES ('Pekka', 'EFHK', 500, 1)"

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

# Test block
if __name__ == "__main__":
    test_player = get_current_player()
    if test_player:
        print("Current player data:")
        for key, value in test_player.items():
            print(f"{key}: {value}")
    else:
        print("ERROR: No player.")
