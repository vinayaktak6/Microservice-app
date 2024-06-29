from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import Config
from routes import auth_bp, items_bp, config_bp, status_bp

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(items_bp)
app.register_blueprint(config_bp)
app.register_blueprint(status_bp)

if __name__ == '__main__':
    app.run(debug=True)
