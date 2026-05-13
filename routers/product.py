from fastapi import APIRouter
from schemas.product import Product as productSchema
from database import engine, Base
from models.product import Product as productModel
from database import SessionLocal

router = APIRouter()

@router.get("/")
def home():
    return {"message": "hello world"}

###########
# GET ALL #
###########
@router.get("/products")
def get_products():
    db = SessionLocal()

    products = db.query(productModel).all()

    db.close()

    return products 

#############
# GET BY ID #
#############
@router.get("/products/{product_id}")
def get_by_id(product_id: int):
    db = SessionLocal()

    product = db.query(productModel).filter(
        productModel.id == product_id
    ).first()

    db.close()

    if product:
        return product

    return {"error": "Product not found"}

##################
# CREATE PRODUCT #
##################
@router.post("/products")
def create_product(product: productSchema):
    db = SessionLocal()

    new_product = productModel(
        name=product.name,
        price=product.price,
        manufacturer=product.manufacturer,
        stock=product.stock,
        category=product.category
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    db.close()

    return new_product

##################
# DELETE PRODUCT #
##################
@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    db = SessionLocal()

    product = db.query(productModel).filter(
        productModel.id == product_id
    ).first()

    if not product:
        db.close()
        return {"error": "Product not found"}

    db.delete(product)
    db.commit()
    db.close()

    return {"message": "Product deleted",
            "deleted item": product.name,
            "id": product.id}

##################
# UPDATE PRODUCT #
##################
@router.put("/products/{product_id}")
def update_product(product_id: int, updated_product: productSchema):
    db = SessionLocal()

    product = db.query(productModel).filter(
        productModel.id == product_id
    ).first()

    if not product:
        db.close()
        return {"error": "Product not found"}

    product.name = updated_product.name
    product.price = updated_product.price

    db.commit()
    db.refresh(product)
    db.close()

    return product