from flask import Blueprint

combat_routes = Blueprint('combat_routes', __name__)

@combat_routes.route('/combat/example-route-name')
def combat_example_route_name():
    return {'example_field': 'example response'}