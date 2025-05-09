import os # The 'os' module provides functions to interact with the operating system, used for convenience, you can ignore this information
from flask import Flask, send_from_directory

# Importing routes
from blackjack_routes import blackjack_routes
from combat_routes import combat_routes
from creature_routes import creature_routes
from gambling_manager_routes import gambling_manager_routes
from investigations_routes import investigations_routes
from inventory_routes import inventory_routes
from player_routes import player_routes
from shop_routes import shop_routes
from snake_game_routes import snake_game_routes
from travel_routes import travel_routes

# Create an instance of the Flask class to initialize the web application
app = Flask(__name__)

# Register the game routes
app.register_blueprint(blackjack_routes)
app.register_blueprint(combat_routes)
app.register_blueprint(creature_routes)
app.register_blueprint(gambling_manager_routes)
app.register_blueprint(investigations_routes)
app.register_blueprint(inventory_routes)
app.register_blueprint(player_routes)
app.register_blueprint(shop_routes)
app.register_blueprint(snake_game_routes)
app.register_blueprint(travel_routes)



# Function to register all the pages (HTML files) from the templates folder
def register_template_routes():
    for filename in os.listdir('templates'):
        if filename.endswith('.html'):
            route = '/' if filename == 'index.html' else f'/{filename.replace(".html", "")}'
            app.add_url_rule(route, endpoint=filename, view_func=lambda file=filename: send_from_directory('templates', file))

# Call the function that registers all the pages
register_template_routes()

# Start the server so users can begin playing when they open the site
if __name__ == '__main__':
    app.run(debug=True)