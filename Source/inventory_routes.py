from flask import Blueprint, jsonify, request
from inventory import Inventory

inventory_routes = Blueprint('inventory_routes', __name__)

@inventory_routes.route('/inventory/items', methods=['GET'])
def get_inventory_items():
    inventory = Inventory()
    items = inventory.get_inventory()
    return jsonify(items)

@inventory_routes.route('/inventory/add', methods=['POST'])
def add_inventory_item():
    inventory = Inventory()
    data = request.get_json()
    item = data.get('item')
    updated_inventory = inventory.add_item(item)
    return jsonify(updated_inventory)

@inventory_routes.route('/inventory/delete', methods=['POST'])
def delete_inventory_item():
    inventory = Inventory()
    data = request.get_json()
    item = data.get('item')
    updated_inventory = inventory.delete_item(item)
    return jsonify(updated_inventory)

