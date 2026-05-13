from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    category: str
    manufacturer: str
    stock: int