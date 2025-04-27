from flask import Blueprint

shop_routes = Blueprint('shop_routes', __name__)

@shop_routes.route('/shop/example-route-name')
def shop_example_route_name():
    return {'example_field': 'example response'}
