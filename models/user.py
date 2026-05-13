from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class User(Base):
    __tablename__: "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    role = Column(String(10), nullable=False)
    birth = Column(Date, nullable=False)