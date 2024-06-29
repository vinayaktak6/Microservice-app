from flask import Blueprint, request, jsonify
from models import Item
from app import db

items_bp = Blueprint('items', __name__)

@items_bp.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data.get('name'), description=data.get('description'))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"id": new_item.id}), 201

@items_bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{"id": item.id, "name": item.name, "description": item.description} for item in items]), 200

@items_bp.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify({"id": item.id, "name": item.name, "description": item.description}), 200

@items_bp.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    db.session.commit()
    return jsonify({"id": item.id, "name": item.name, "description": item.description}), 200

@items_bp.route('/items/<int:id>', methods=['PATCH'])
def partially_update_item(id):
    item = Item.query.get_or_404(id)
    data = request.get_json()
    if 'name' in data:
        item.name = data.get('name')
    if 'description' in data:
        item.description = data.get('description')
    db.session.commit()
    return jsonify({"id": item.id, "name": item.name, "description": item.description}), 200

@items_bp.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204
