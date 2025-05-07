from flask import Blueprint, jsonify, request
from investigations import investigation_start, investigation_update_step, get_investigations
investigations_routes = Blueprint('investigations_routes', __name__)

@investigations_routes.route('/investigations/start')
def investigations_start():
    result = investigation_start()
    return jsonify(result)

@investigations_routes.route('/investigations/update-step', methods=["POST"])
def investigations_update_step():
    data = request.get_json()
    step = data.get("step")
    result = investigation_update_step(step)
    return jsonify(result)

@investigations_routes.route('/investigations/list')
def investigations_list():
    type_param = request.args.get("type")
    result = get_investigations(type_param)
    return jsonify(result)
