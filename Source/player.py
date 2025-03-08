# player.py
import mysql.connector
from database import update_data_in_database, get_data_from_database

current_player_id = None

def reset_player():
    global current_player_id
    current_player_id = None
    update_data_in_database("DELETE FROM player")
    update_data_in_database("ALTER TABLE player AUTO_INCREMENT = 1")
    update_data_in_database("DELETE FROM inventory")
    update_data_in_database("ALTER TABLE inventory AUTO_INCREMENT = 1")

def update_player(field, value, player_id):
    update_data_in_database(f"UPDATE player SET {field} = '{value}' WHERE id = {player_id}")

def add_player(new_player_name):
    reset_player()
    global current_player_id

    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='ufo_peli',
        user='root',  # attention! do not forget to replace user and password with yours
        password='1234',
        autocommit=True,
        collation="utf8mb4_unicode_ci" # this field may be inappropriate for windows or linux, but we did it in class, use your own configuration instead, if it doesn't work
    )

    if new_player_name:
        query = f"INSERT INTO player (name) VALUES ('{new_player_name}')"
    else:
        query = "INSERT INTO player () VALUES ()"

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
            columns = ["id", "name", "location_ident", "money", "player_level"]
            player_data = result[0]
            player = {columns[i]: player_data[i] for i in range(len(columns))}
            return player
    else:
        return {}

add_player('')