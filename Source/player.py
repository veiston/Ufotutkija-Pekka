# player.py
from database import *

class Player:
    current_id = None

    def __init__(self, name=None):
        self.id = None
        self.name = name or "Pekka"
        self.location_ident = "EFHK"
        self.hp = None
        self.attack = None
        self.money = 300
        self.player_level = 1

        if name is None:
            self.load_current_player()

    @staticmethod
    def reset():
        update_data_in_database("DELETE FROM inventory")
        update_data_in_database("ALTER TABLE inventory AUTO_INCREMENT = 1")
        update_data_in_database("DELETE FROM player")
        update_data_in_database("ALTER TABLE player AUTO_INCREMENT = 1")

    def load_current_player(self):
        result = get_data_from_database(
            "SELECT id, name, location_ident, hp, attack, money, player_level FROM player LIMIT 1")

        if result:
            row = result[0]
            self.id = row[0]
            self.name = row[1]
            self.location_ident = row[2]
            self.hp = row[3]
            self.attack = row[4]
            self.money = row[5]
            self.player_level = row[6]
            Player.current_id = self.id

    def add(self):
        Player.reset()
        connection = connect_to_database()

        if self.name:
            query = f"INSERT INTO player (name) VALUES ('{self.name}')"
        else:
            query = "INSERT INTO player (name, location_ident, money, player_level) VALUES ('Pekka', 'EFHK', 300, 1)"

        cursor = connection.cursor()
        cursor.execute(query)
        cursor.execute("SELECT LAST_INSERT_ID()")
        result = cursor.fetchall()

        if result and result[0]:
            self.id = result[0][0]
            Player.current_id = self.id

        cursor.close()
        connection.close()

    def update(self, updates):
        if not updates:
            return
        set_clause = ', '.join([f"{field} = '{value}'" for field, value in updates.items()])
        query = f"UPDATE player SET {set_clause} WHERE id = {self.id}"
        update_data_in_database(query)

    def get_current(self):
        if self.id:
            query = f"SELECT * FROM player WHERE id = {self.id}"
            result = get_data_from_database(query)
            if result:
                columns = ["id", "name", "location_ident", "hp", "attack", "money", "player_level"]
                player_data = result[0]
                return {columns[i]: player_data[i] for i in range(len(columns))}
        else:
            return {}

# Test block
if __name__ == "__main__":
    player = Player("Pekka")
    player.add()
    test_player = player.get_current()

    if test_player:
        for key, value in test_player.items():
            print(f"{key}: {value}")
    else:
        print("ERROR: No player")
