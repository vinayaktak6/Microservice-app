from flask import Blueprint

auth_bp = Blueprint('auth', __name__)
items_bp = Blueprint('items', __name__)
config_bp = Blueprint('config', __name__)
status_bp = Blueprint('status', __name__)

from . import auth, items, config, status
