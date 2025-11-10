import pytest
from app import create_app
from app import services

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as c:
        # ensure clean store each test
        services.clear_store()
        yield c

def test_health(client):
    rv = client.get('/api/health')
    assert rv.status_code == 200
    assert rv.get_json()['status'] == 'ok'

def test_add_and_get_entry(client):
    data = {'user':'alice','activity':'running','duration_minutes':30,'category':'cardio'}
    rv = client.post('/api/entries', json=data)
    assert rv.status_code == 201
    j = rv.get_json()
    assert j['user'] == 'alice'
    eid = j['id']

    rv2 = client.get(f'/api/entries/{eid}')
    assert rv2.status_code == 200
    assert rv2.get_json()['activity'] == 'running'

def test_missing_field(client):
    rv = client.post('/api/entries', json={'user':'bob'})
    assert rv.status_code == 400

def test_delete_entry(client):
    data = {'user':'c','activity':'yoga','duration_minutes':20}
    rv = client.post('/api/entries', json=data)
    eid = rv.get_json()['id']
    rv2 = client.delete(f'/api/entries/{eid}')
    assert rv2.status_code == 204
    rv3 = client.get(f'/api/entries/{eid}')
    assert rv3.status_code == 404
