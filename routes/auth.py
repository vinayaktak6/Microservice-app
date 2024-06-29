from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    if user and check_password_hash(user.password, data.get('password')):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # JWT tokens are stateless, so to "logout" you would need a token blacklist implementation
    return jsonify({"msg": "Logout successful"}), 200

@auth_bp.route('/user/<int:id>/roles', methods=['GET'])
@jwt_required()
def get_user_roles(id):
    user = User.query.get_or_404(id)
    return jsonify(roles=user.roles.split(',')), 200
