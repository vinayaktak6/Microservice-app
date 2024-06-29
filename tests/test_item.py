import pytest
from app import app, db
from models import Item

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_create_item(client):
    response = client.post('/items', json={'name': 'item1', 'description': 'description1'})
    assert response.status_code == 201
    assert 'id' in response.get_json()

def test_get_items(client):
    client.post('/items', json={'name': 'item1', 'description': 'description1'})
    response = client.get('/items')
    assert response.status_code == 200
    assert len(response.get_json()) == 1
