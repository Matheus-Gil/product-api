from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# A simple solution to use the pytest command without clogging the actual database with test products
# Another database URL can be provided instead of the default (mainly a test.db)
# On terminal: python run_tests.py 
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./store.db"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency Injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()