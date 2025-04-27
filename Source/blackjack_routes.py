from flask import Blueprint

blackjack_routes = Blueprint('blackjack_routes', __name__)

@blackjack_routes.route('/blackjack/example-route-name')
def blackjack_example_route_name():
    return {'example_field': 'example response'}
