from flask import Blueprint

creature_routes = Blueprint('creature_routes', __name__)

@creature_routes.route('/creature/example-route-name')
def creature_example_route_name():
    return {'example_field': 'example response'}
