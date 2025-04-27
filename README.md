# Ufotutkija
 
 Ufotutkija is a text-based adventure game in the paranormal investigation genre. The player takes on the role of
 a renowned UFO hunter. The game starts in the player’s office, where they receive a mysterious letter from an old friend
 asking for help.
 
 ## Tech features
 - Python 3.x 
 - `ufo_peli` database 
 
 ## Requirements
 - Python 3.x 
 - Required dependencies (see requirements.txt)
 - Access to the `ufo_peli` database
 
 ## Installation
 1. Clone this repository:
    ```sh
    git clone https://github.com/veiston/Ufotutkija-Pekka.git
    ```
     ```sh
    cd Ufotutkija-Pekka
    ```
 2. Install dependencies:
     ```sh
    pip install -r requirements.txt
    ```
 3. Set up the `ufo_peli` database:
    - Ensure MariaDB is installed and running.  
    - Log in to MariaDB:
      ```sh
      mariadb -u your_user_name -p
      ```
    - Navigate to the project root directory:  
      ```sh
      cd path/to/Ufotutkija-Pekka
      ```
    - Execute the SQL script to create and populate the database:
      ```sh
      mariadb -u root -p < ufo_peli.sql
      ```
    - The database is accessed using the `root` user with the password `1234`

## Start the Server and Interface

1. Navigate to the `Source` directory:
   ```sh
   cd Source
   ```

2. Launch the server:
   ```sh
   python server.py
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Troubleshooting

### Error: Unknown collation: 'utf8mb4_0900_ai_ci'

If you encounter the following error when running the application:

```
mysql.connector.errors.DatabaseError: 1273 (HY000): Unknown collation: 'utf8mb4_0900_ai_ci'
```

This error occurs because MySQL does not support the specified collation.

### Solution

In the `database.py` file, inside the `connect_to_database` function, uncomment the following line:

```python
collation = 'utf8mb3_unicode_ci'  # I think this breaks the database on Windows
```

This change ensures compatibility with your MySQL version.

 ## Contributors
 - Veikka Liukkonen
 - Unna Postila
 - Kseniia Shlenskaia
 - Sona Tuuvi
 
 ##
