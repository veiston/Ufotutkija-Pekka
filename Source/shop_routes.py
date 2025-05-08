from flask import Blueprint, request, jsonify
from shop import get_shop_items, buy_item

shop_routes = Blueprint('shop_routes', __name__)

@shop_routes.route('/shop/items', methods=['GET'])

def shop_items():
    items = get_shop_items()
    return jsonify(items)

@shop_routes.route('/shop/buy', methods=['POST'])
def shop_buy():
    data = request.get_json()
    item_name = data.get('item_name')

    if not item_name:
        return jsonify({'error': 'The field item_name are required'}), 400

    result = buy_item(item_name)
    if "status" in result:
        return jsonify(result), result["status"]
    return jsonify(result)