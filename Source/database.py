# database.py

# we use original flight_game database
# example of using function below: get_data_from_database(f"SELECT name FROM airport WHERE ident = '{player['airport]}'")

# VERY IMPORTANT INFORMATION
# Here lies a ready-to-use function for accessing the database, but it is commented out because it requires your URO project on your computer in current IDE to be connected to the database (as we did in the lesson), otherwise, everything will break.
# I assumed that not all colleagues have set this up yet, so I simply hid the code to avoid complications.
# If you are working on the travel() function and need the airport database, uncomment the "import mysql.connector" and "get_data_from_database()" function.
# Before doing this make sure that the flight_game database is running on your computer and is connected to your UFO project in current IDE (as we did in the lesson)
# If you forget something or run into any issues, please write in the chat


# import mysql.connector
# def get_data_from_database(query): # get_data_from_database function only accepts SELECT queries as a plain string, it cannot process UPDATE, INSERT etc
#     connection = mysql.connector.connect(
#         host='127.0.0.1',
#         port=3306,
#         database='flight_game',
#         user='root',  # attention! do not forget to replace user and password with yours
#         password='1234',
#         autocommit=True,
#         collation="utf8mb4_unicode_ci" # this field may be inappropriate for windows or linux, but we did it in class, use your own configuration instead, if it doesn't work
#     )
#
#     cursor = connection.cursor()
#     cursor.execute(query)
#     result = cursor.fetchall()
#
#     cursor.close()
#     connection.close()
#
#     return result