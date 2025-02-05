from fastapi.responses import Response

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_hello_world():
    """
    Should exists the / request and return the default message when request.
    """

    response: Response = client.get('/')

    assert response.status_code == 200
    assert response.json() == { "message": "hello world!" }

def test_docs():
    """""
    should exists project doc as default, created by Fastapi.
    """
    response: Response = client.get('/docs')
    assert response.status_code == 200

def test_get_products():

    res: Response = client.get('/products')
    assert res.status_code == 200
    assert len(res.json()) == 5