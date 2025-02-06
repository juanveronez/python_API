from fastapi import FastAPI, Response, HTTPException

from .data import products
from .schema import ProductSchema

app = FastAPI()

@app.get('/')
def hello_world():
    return { "message": "hello world!" }

@app.get('/products', response_model=list[ProductSchema])
def list_products():
    return products

@app.get('/products/{id}', response_model=ProductSchema)
def get_product_by_id(id: int):
    # next is used to get an iterable, get the next value of an iterable or the default if not exists
    product = next((product for product in products if product["id"] == id), None)
    if product:
        return product
    
    raise HTTPException(status_code=404, detail="Product not found")

@app.post('/products')
def create_product(product: ProductSchema, response: Response):
    products.append(product)

    response.status_code = 201
    return { "Message": "Product created successfully" }
