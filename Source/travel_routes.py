from flask import Blueprint

travel_routes = Blueprint('travel_routes', __name__)

@travel_routes.route('/travel/example-route-name')
def travel_example_route_name():
    return {'example_field': 'example response'}