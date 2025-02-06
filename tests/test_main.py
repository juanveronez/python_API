from fastapi.responses import Response

from fastapi.testclient import TestClient

from app.main import app
from app.schema import ProductSchema

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

# def test_list_products():

#     res: Response = client.get('/products')
#     assert res.status_code == 200
#     assert len(res.json()) == 5

# def test_get_product_by_id():
#     res: Response = client.get('/products/1')
#     assert res.status_code == 200

#     product = {
#         "id": 1,
#         "name": "Laptop",
#         "description": "A high performance laptop",
#         "price": 999.99,
#         "available": True
#     }

#     assert res.json() == product

# def test_not_get_product_by_inexistent_id():
#     res: Response = client.get('/products/6')
#     assert res.status_code == 404
#     assert res.json() == {'detail': 'Product not found'}

# def test_create_product():
#     product = ProductSchema(id=6,name="test", description="description", available=True, price=2000.56)
    
#     res = client.post('/products', json=product.model_dump(mode='json'))
#     assert res.status_code == 201
#     assert res.json() == { "Message": "Product created successfully" }
