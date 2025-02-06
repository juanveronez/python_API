from fastapi import APIRouter, HTTPException, Depends

from .schema import CreateProductSchema, ProductSchema
from .database import get_database, Session
from .model import Product

router = APIRouter(prefix='/products')

@router.get('', response_model=list[ProductSchema])
def list_products(db: Session = Depends(get_database)):
    return db.query(Product).all()

@router.get('/{id}', response_model=ProductSchema)
def get_product_by_id(id: int, db: Session = Depends(get_database)):
    # next is used to get an iterable, get the next value of an iterable or the default if not exists
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return product

@router.post('', status_code = 201)
def create_product(product: CreateProductSchema, db: Session = Depends(get_database)):
    db_product = Product(**product.model_dump())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    
    return { "Message": "Product created successfully" }


@router.delete('/{id}', response_model=ProductSchema)
def delete_product(id: int, db: Session = Depends(get_database)):
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return product

@router.put('/{id}', response_model=ProductSchema)
def update_product(id: int, product_data: CreateProductSchema, db: Session = Depends(get_database)):
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for k, v in product_data.model_dump().items():
        if v:
            setattr(product, k, v)
    db.commit()
    db.refresh(product)
    return product