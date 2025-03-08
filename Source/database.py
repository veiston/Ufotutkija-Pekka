# database.py

# example of using functions below:
# get_data_from_database(f"SELECT name FROM airport WHERE ident = 'AA00'")
# update_data_in_database("UPDATE player SET money = 1000 WHERE id = 1")

import mysql.connector
def get_data_from_database(query):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='ufo_peli',
        user='root',  # attention! do not forget to replace user and password with yours
        password='1234',
        autocommit=True,
        collation="utf8mb4_unicode_ci" # this field may be inappropriate for windows or linux, but we did it in class, use your own configuration instead, if it doesn't work
    )

    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

def update_data_in_database(query, params=None):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='ufo_peli',
        user='root',
        password='1234',  # attention! do not forget to replace user and password with yours
        autocommit=True,
        collation="utf8mb4_unicode_ci" # this field may be inappropriate for windows or linux, but we did it in class, use your own configuration instead, if it doesn't work
    )

    cursor = connection.cursor()

    cursor.execute(query)

    cursor.close()
    connection.close()
