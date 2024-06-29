import pytest
from app import app, db
from models import User
from werkzeug.security import generate_password_hash

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            user = User(username='testuser', password=generate_password_hash('testpassword'), roles='admin')
            db.session.add(user)
            db.session.commit()
            yield client
            db.drop_all()

def test_login(client):
    response = client.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200
    assert 'access_token' in response.get_json()
