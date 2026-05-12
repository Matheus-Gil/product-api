from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    manufacturer: str
    stock: int