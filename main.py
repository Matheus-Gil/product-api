from fastapi import FastAPI
from database import engine, Base
from routers import product

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(product.router)