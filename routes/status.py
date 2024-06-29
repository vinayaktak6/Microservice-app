from flask import Blueprint, jsonify

status_bp = Blueprint('status', __name__)

@status_bp.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "running"}), 200

@status_bp.route('/health', methods=['GET'])
def health():
    return jsonify({"health": "healthy"}), 200
