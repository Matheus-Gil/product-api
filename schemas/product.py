from pydantic import BaseModel
from enum import Enum

class ProductCategory(str, Enum):
    COMPONENTS = "COMPONENTS"
    PERIPHERALS = "PERIPHERALS"
    NETWORK = "NETWORK"
    MOBILE = "MOBILE"
    OFFICE = "OFFICE"

class Product(BaseModel):
    name: str
    price: float
    category: ProductCategory
    subcategory: str
    manufacturer: str
    stock: int