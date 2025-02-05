from typing import Dict, List, Any

from fastapi import FastAPI, Response

app = FastAPI()

products: List[Dict[str, Any]] = [
    {
        "id": 1,
        "name": "Laptop",
        "description": "A high performance laptop",
        "price": 999.99,
        "available": True
    },
    {
        "id": 2,
        "name": "Smartphone",
        "description": "A latest model smartphone",
        "price": 699.99,
        "available": True
    },
    {
        "id": 3,
        "name": "Headphones",
        "description": "Noise-cancelling headphones",
        "price": 199.99,
        "available": False
    },
    {
        "id": 4,
        "name": "Monitor",
        "description": "4K Ultra HD monitor",
        "price": 299.99,
        "available": True
    },
    {
        "id": 5,
        "name": "Keyboard",
        "description": "Mechanical keyboard",
        "price": 89.99,
        "available": True
    }
]

@app.get('/')
def hello_world():
    return { "message": "hello world!" }

@app.get('/products')
def list_products():
    return products

@app.get('/products/{id}')
def get_product_by_id(id: int, response: Response):
    # next is used to get an iterable, get the next value of an iterable or the default if not exists
    product = next((product for product in products if product["id"] == id), None)
    if product:
        return product
    
    response.status_code = 404
    return {"Message": "Product not Found."}
    