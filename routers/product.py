from fastapi import APIRouter
from schemas.product import Product as productSchema
from models.product import Product as productModel
from database import SessionLocal

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

###########
# GET ALL #
###########
@router.get("/", 
            summary="Gets all Products", 
            description="Returns every Product registered in the Database")
def get_products():
    db = SessionLocal()

    products = db.query(productModel).all()

    db.close()

    return products 

#############
# GET BY ID #
#############
@router.get("/{product_id}", 
            summary="Gets a Product by ID", 
            description="Returns a product through the given ID.")
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
@router.post("/", 
             summary="Adds a new Product", 
             description="Creates and adds a new product in the database, requiring a name, price, manufacturer, stock and category.")
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
@router.delete("/{product_id}", 
               summary="Deletes a Product", 
               description="Removes a Product from the database through the given ID")
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
@router.put("/{product_id}", 
            summary="Updates a Product", 
            description="Updates the selected Product's name, price and stock through the given ID")
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
    product.stock = updated_product.stock

    db.commit()
    db.refresh(product)
    db.close()

    return product