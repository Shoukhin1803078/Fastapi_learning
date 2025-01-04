# Fastapi_learning


# Instructions:
For MySQL, you'll need to install these dependencies:
bashCopypip install fastapi uvicorn sqlalchemy mysql-connector-python pydantic
Before running the application:

Create a MySQL database:

sqlCopyCREATE DATABASE dbname;

Update the database URL in config/database.py with your MySQL credentials:

pythonCopySQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/dbname"

Create an empty __init__.py file in each directory to make them Python packages:

bashCopy    touch controllers/__init__.py models/__init__.py schemas/__init__.py config/__init__.py

Run the application:

bashCopypython main.py
The API will be available at:

Swagger documentation: http://localhost:8000/docs
API endpoints:

POST http://localhost:8000/users/ - Create user
GET http://localhost:8000/users/ - Get all users



Would you like me to add any additional features or explain any part in more detail?






# SQL Code


CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create an index on the name column for faster searches
CREATE INDEX idx_users_name ON users(name);



# models/model.py
from sqlalchemy import Column, Integer, String
from config.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

# schemas/schema.py
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    
    class Config:
        orm_mode = True

# controllers/controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.database import get_db
from models.model import User
from schemas.schema import UserCreate, UserResponse

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# config/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL connection URL
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/dbname"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=5,
    max_overflow=10
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# main.py
from fastapi import FastAPI
from controllers.controller import router
from config.database import engine, Base

app = FastAPI(title="User Info System")

# Create tables
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(router, tags=["users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)