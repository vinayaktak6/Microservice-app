import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_get_config(client):
    response = client.get('/config')
    assert response.status_code == 200
    data = response.get_json()
    assert 'setting1' in data
    assert 'setting2' in data

def test_update_config(client):
    response = client.put('/config', json={'setting1': 'new_value1'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['setting1'] == 'new_value1'
