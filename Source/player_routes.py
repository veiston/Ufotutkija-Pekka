from flask import Blueprint, request, jsonify
from player import Player
from investigations import reset_investigations
player_routes = Blueprint('player_routes', __name__)

# POST request to create new player
@player_routes.route('/player/create', methods=['POST'])
def player_create():
    data = request.get_json()
    player_name = data.get('name', '')
    player = Player(player_name)
    player.add()
    reset_investigations()
    current = player.get_current()
    return jsonify(current)

# POST request to update current player
@player_routes.route('/player/update', methods=['POST'])
def player_update():
    if not Player.current_id:
        return jsonify({"error": "The field current_id is required"}), 404
    data = request.get_json()
    player = Player()
    player.id = Player.current_id
    player.update(data)
    updated = player.get_current()
    return jsonify(updated)

# GET request to fetch player data
@player_routes.route('/player/detail')
def player_detail():
    if not Player.current_id:
        return jsonify({"error": "The field current_id is required"}), 404
    player = Player()
    player.id = Player.current_id
    current = player.get_current()
    return jsonify(current)




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