from flask import Blueprint

investigations_routes = Blueprint('investigations_routes', __name__)

@investigations_routes.route('/investigations/example-route-name')
def investigations_example_route_name():
    return {'example_field': 'example response'}
