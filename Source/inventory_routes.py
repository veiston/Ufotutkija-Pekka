from flask import Blueprint

inventory_routes = Blueprint('inventory_routes', __name__)

@inventory_routes.route('/inventory/example-route-name')
def inventory_example_route_name():
    return {'example_field': 'example response'}
