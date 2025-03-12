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
      
 ## Start the Game
 Start the game by executing the following command:
  ```sh
  python game.py
  ```
 
 ## Contributors
 - Veikka Liukkonen
 - Unna Postila
 - Kseniia Shlenskaia
 - Sona Tuuvi
 
 ##
