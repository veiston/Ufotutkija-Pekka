from flask import Blueprint

gambling_manager_routes = Blueprint('gambling_manager_routes', __name__)

@gambling_manager_routes.route('/gambling/example-route-name')
def gambling_example_route_name():
    return {'example_field': 'example response'}
