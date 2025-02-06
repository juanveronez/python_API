from pydantic import BaseModel, PositiveFloat
from typing import Optional

class CreateProductSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: PositiveFloat
    available: bool

class ProductSchema(CreateProductSchema):
    id: int