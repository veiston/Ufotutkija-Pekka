from flask import Blueprint, jsonify
from investigations import investigation_start

investigations_routes = Blueprint('investigations_routes', __name__)

@investigations_routes.route('/investigations/start')
def investigations_start():
    result = investigation_start()
    return jsonify(result)
