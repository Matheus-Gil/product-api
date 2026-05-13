from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    EMPLOYEE = "EMPLOYEE"
    CLIENT = "CLIENT"

class User(BaseModel):
    username: str
    role: UserRole
    