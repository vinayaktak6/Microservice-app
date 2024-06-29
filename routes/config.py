from flask import Blueprint, request, jsonify

config_bp = Blueprint('config', __name__)

# Mock configuration settings
config_settings = {
    "setting1": "value1",
    "setting2": "value2"
}

@config_bp.route('/config', methods=['GET'])
def get_config():
    return jsonify(config_settings), 200

@config_bp.route('/config', methods=['PUT'])
def update_config():
    data = request.get_json()
    config_settings.update(data)
    return jsonify(config_settings), 200
