from flask import Blueprint, request, jsonify
from player import add_player, get_current_player, update_player
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

@player_routes.route('/player/update', methods=['POST'])
def player_update():
    data = request.get_json()

    from player import current_player_id

    if current_player_id is None:
        return jsonify({"error": "The field current_player_id is required"}), 404

    update_player(data, current_player_id)
    player = get_current_player()
    return jsonify(player)

# Example of usage in JS
#
# const newPlayerData = {
#     name: 'Lucky bastard',
#     money: 1000000
#     // You can add here and thereby update any field of a player entity from the database
# };
#
# const updatePlayer = async (newData = {}) => {
#     try {
#         const response = await fetch('/player/update', {
#             method: 'POST',
#             headers: {
#                 'Content-Type': 'application/json',
#             },
#             body: JSON.stringify(newData),
#         });
#
#         if (!response.ok) {
#             throw new Error(`HTTP error`); // Fetch does not throw an error on HTTP 400 or 500 responses, so you should manually check the response to force the interpreter into the catch block
#         }
#
#         const updatedPlayer = await response.json(); // Returns the updated current user in full
#         return updatedPlayer;
#     } catch (error) {
#         console.error(error);
#         return null;
#     }
# };