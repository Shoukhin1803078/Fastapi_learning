from fastapi import FastAPI


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from pydantic import BaseModel






app = FastAPI()

# Database setup
engine = create_engine("postgresql://postgres:1803078Boss%40%23%24%25%26@localhost:5432/testing")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Database model
class StudentDB(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    roll = Column(Integer, unique=True)
    age = Column(Integer)


# Pydantic model
class Student(BaseModel):
    name: str
    roll: int
    age: int

# Create tables
Base.metadata.create_all(bind=engine)

# API endpoints
@app.get("/")
def homepage():
    return {"message":"Hello world this is alamins world"}


# @app.post("/students")
# def create_student(student: Student):
#     db = SessionLocal()
#     db_student = StudentDB(**student.dict())
#     db.add(db_student)
#     db.commit()
#     db.close()
#     return {
#         "Here is the whole object":student,
#         "You write name":student.name,
#         "Your roll":student.roll,
#         "Your age":student.age,
#         "Success message":"Your full data stored in the table successfully"
#         }

@app.post("/students")
def create_student(student: Student):
    db = SessionLocal()
    db_student = StudentDB(**student.dict())
    print(db_student)

    db.add(db_student)
    db.commit()
    db.close()
    return student
    # return {
    #     "Here is the whole object": student,
    #     "You write name": "{student.name}",
    #     "Your roll": student.roll,
    #     "Your age": student.age,
    #     "Success message": "Your full data stored in the table successfully"
    # }

@app.get("/students")
def get_students():
    db = SessionLocal()
    students = db.query(StudentDB).all()
    db.close()
    return students

@app.get("/students/{roll}")
def get_student(roll: int):
    db = SessionLocal()
    student = db.query(StudentDB).filter(StudentDB.roll == roll).first()
    db.close()
    return student

@app.put("/students/{roll}")
def update_student(roll: int, student: Student):
    db = SessionLocal()
    db_student = db.query(StudentDB).filter(StudentDB.roll == roll).first()
    db_student.name = student.name
    db_student.age = student.age
    db.commit()
    db.close()
    return student

@app.delete("/students/{roll}")
def delete_student(roll: int):
    db = SessionLocal()
    student = db.query(StudentDB).filter(StudentDB.roll == roll).first()
    db.delete(student)
    db.commit()
    db.close()
    return {"message": "Student deleted"}