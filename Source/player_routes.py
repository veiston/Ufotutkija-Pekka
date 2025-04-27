from flask import Blueprint, request, jsonify
from player import add_player, get_current_player
player_routes = Blueprint('player_routes', __name__)

# GET request to fetch player data
@player_routes.route('/player/detail')
def player_detail():
    player = get_current_player()
    return jsonify(player)

# POST request to create new player
@player_routes.route('/player/create', methods=['POST'])
def player_create():
    data = request.get_json()
    player_name = data.get('name', '')
    add_player(player_name)
    player = get_current_player()
    return jsonify(player)

