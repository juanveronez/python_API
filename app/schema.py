from pydantic import BaseModel, PositiveFloat
from typing import Optional

class ProductSchema(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: PositiveFloat
    available: bool