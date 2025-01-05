# FastAPI User Information System
Prepared by alamin
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

A robust RESTful API built with FastAPI and MySQL for managing user information. This project follows the MVC (Model-View-Controller) pattern and provides a clean, organized structure for handling user data through HTTP endpoints.

## 📑 Table of Contents
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [🔧 Configuration](#-configuration)
- [📝 Usage](#-usage)
- [📚 API Documentation](#-api-documentation)
- [💻 Code Structure](#-code-structure)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## ✨ Features
* 🚀 RESTful API endpoints for user management
* 🗄️ MySQL database integration with SQLAlchemy ORM
* 🏗️ MVC architecture for clean code organization
* 📖 Automatic Swagger/OpenAPI documentation
* ✅ Input validation using Pydantic models
* 🔄 Connection pooling for optimal database performance
* ⚡ Asynchronous request handling

## 🛠️ Tech Stack
* [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
* [MySQL](https://www.mysql.com/) - Database
* [SQLAlchemy](https://www.sqlalchemy.org/) - ORM
* [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
* [Uvicorn](https://www.uvicorn.org/) - ASGI server

## 📁 Project Structure
```
project_root/
│
├── controllers/
│   ├── __init__.py
│   └── controller.py
│
├── models/
│   ├── __init__.py
│   └── model.py
│
├── schemas/
│   ├── __init__.py
│   └── schema.py
│
├── config/
│   ├── __init__.py
│   └── database.py
│
├── main.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-user-system.git
   cd fastapi-user-system
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up MySQL database:
   ```sql
   CREATE DATABASE dbname;
   ```

## 🔧 Configuration

1. Create `config/database.py`:
   ```python
   from sqlalchemy import create_engine
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker

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
   ```

2. Create database tables:
   ```sql
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

   CREATE INDEX idx_users_name ON users(name);
   ```

## 📝 Usage

1. Start the server:
   ```bash
   python main.py
   ```

2. Access the API:
   * API endpoints: `http://localhost:8000`
   * Swagger UI: `http://localhost:8000/docs`
   * ReDoc: `http://localhost:8000/redoc`

3. Example API calls:
   ```bash
   # Create user
   curl -X POST "http://localhost:8000/users/" \
        -H "Content-Type: application/json" \
        -d '{"name": "John Doe"}'

   # Get all users
   curl "http://localhost:8000/users/"
   ```

## 📚 API Documentation

### Endpoints

#### POST /users/
Create a new user
* Request Body:
  ```json
  {
      "name": "string"
  }
  ```
* Response:
  ```json
  {
      "id": "integer",
      "name": "string"
  }
  ```

#### GET /users/
Get all users
* Response:
  ```json
  [
      {
          "id": "integer",
          "name": "string"
      }
  ]
  ```

## 💻 Code Structure

### Models (`models/model.py`)
```python
from sqlalchemy import Column, Integer, String
from config.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
```

### Controllers (`controllers/controller.py`)
```python
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
```

### Schemas (`schemas/schema.py`)
```python
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    
    class Config:
        orm_mode = True
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Show your support

Give a ⭐️ if this project helped you!

<a href="https://www.buymeacoffee.com/yourusername" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>