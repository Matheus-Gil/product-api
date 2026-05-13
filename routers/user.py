from fastapi import APIRouter
from schemas.user import User as userSchema
from models.user import User as userModel
from schemas.user import UserRole as userRole
from database import SessionLocal

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

###########
# GET ALL #
###########
@router.get("/", 
            summary="Gets all users", 
            description="Returns all users registered in the database")
def get_users():
    db = SessionLocal()

    users = db.query(userModel).all()

    db.close()

    return users

#############
# GET BY ID #
#############
@router.get("/{user_id}", 
            summary="Gets an user by ID", 
            description="Returns a user by the given ID")
def get_by_id(user_id: int):
    db = SessionLocal()

    user = db.query(userModel).filter(
        userModel.id == user_id
    ).first()

    db.close()

    if user:
        return user

    return {"error": "User not found"}

###############
# GET BY NAME #
###############
@router.get("/{username}", 
            summary="Gets Users by Name", 
            description="Returns all users matching the given name")
def get_by_name(username: str):
    db = SessionLocal()

    user = db.query(userModel).filter(
        userModel.username == username
    ).all()

    db.close()

    if user:
        return user

    return {"error": "User not found"}

###############
# GET BY ROLE #
###############

@router.get("/role/{role}")
def get_by_role(role: userRole):
    db = SessionLocal()

    user = db.query(userModel).filter(
        userModel.role == role
    ).all()

    db.close()

    if user:
        return user
    
    return {"error": "Users not found"}
