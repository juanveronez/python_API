from pydantic import BaseModel, PositiveFloat
from typing import Optional

class ProductSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: PositiveFloat
    available: bool