from flask import Blueprint

snake_game_routes = Blueprint('snake_game_routes', __name__)

@snake_game_routes.route('/snake_game/example-route-name')
def snake_game_example_route_name():
    return {'example_field': 'example response'}
