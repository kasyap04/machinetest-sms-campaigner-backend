from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'status': True, 'msg': "Welcome to SMS Campaigner"}


def test_auth():
    response = client.post("/auth")
    assert response.status_code == 200
    assert response.json() == {'status': False}

    

def test_create_campaign():
    response = client.post(
        "/create-campaign", 
        json={
            "campaignName": "Test Campaign",
            "originator": "Test-Originator",
            "recipients": ["testnum1", "testnum2"],
            "content": "Test content"
        }
    )

    assert response.status_code == 200
    assert response.json() == {'status' : False, 'msg' : 'Error occured'}



def test_login():
    response = client.post(
        "/login", 
        json={
            "username": "admin",
            "password": "admin123"
        }
    )

    assert response.status_code == 200
    assert response.json() == {'status' : True, 'msg' : 'loged in'}