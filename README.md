steps
create engine->session->table->migrate

steps like 
create engine 
create session
create table 
migrate




# create_table.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:your_password@localhost:5432/testing")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    roll = Column(Integer, unique=True)
    age = Column(Integer)
    
    def __repr__(self):
        return f"Name: {self.name}, Roll: {self.roll}, Age: {self.age}"

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Table created successfully!")

# ----------------------------------------

# insert.py
from create_table import Student, Session

def insert_student():
    session = Session()
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    age = int(input("Enter age: "))
    
    student = Student(name=name, roll=roll, age=age)
    session.add(student)
    session.commit()
    print(f"Added student: {student}")
    session.close()

if __name__ == "__main__":
    insert_student()

# ----------------------------------------

# update.py
from create_table import Student, Session

def show_all_students():
    session = Session()
    students = session.query(Student).all()
    print("\nAll Students:")
    for student in students:
        print(student)
    session.close()

def update_student():
    session = Session()
    roll = int(input("Enter roll number to update: "))
    student = session.query(Student).filter_by(roll=roll).first()
    
    if student:
        new_age = int(input("Enter new age: "))
        student.age = new_age
        session.commit()
        print(f"Updated student: {student}")
    else:
        print(f"No student found with roll number {roll}")
    session.close()

if __name__ == "__main__":
    show_all_students()
    update_student()
    show_all_students()

# ----------------------------------------

# delete.py
from create_table import Student, Session

def delete_student():
    session = Session()
    roll = int(input("Enter roll number to delete: "))
    student = session.query(Student).filter_by(roll=roll).first()
    
    if student:
        session.delete(student)
        session.commit()
        print(f"Deleted student with roll number {roll}")
    else:
        print(f"No student found with roll number {roll}")
    session.close()

if __name__ == "__main__":
    show_all_students()
    delete_student()
    show_all_students()













































create_table.py (Database Setup):

pythonCopy# Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create database engine
engine = create_engine("postgresql://postgres:your_password@localhost:5432/testing")
# Create session factory
Session = sessionmaker(bind=engine)
# Create base class for models
Base = declarative_base()

# Define Student model
class Student(Base):
    __tablename__ = 'student'  # Table name in database
    
    # Define columns
    id = Column(Integer, primary_key=True)  # Auto-incrementing ID
    name = Column(String(50))               # Name with max length 50
    roll = Column(Integer, unique=True)     # Unique roll number
    age = Column(Integer)                   # Age
    
    # String representation of Student object
    def __repr__(self):
        return f"Name: {self.name}, Roll: {self.roll}, Age: {self.age}"

# Create tables in database
if __name__ == "__main__":
    Base.metadata.create_all(engine)

insert.py (Create Operation):

pythonCopy# Import model and session
from create_table import Student, Session

def insert_student():
    # Start new session
    session = Session()
    
    # Get user input
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    age = int(input("Enter age: "))
    
    # Create new student object
    student = Student(name=name, roll=roll, age=age)
    session.add(student)      # Add to session
    session.commit()          # Save to database
    print(f"Added student: {student}")
    session.close()           # Close session

update.py (Read and Update Operations):

pythonCopyfrom create_table import Student, Session

# Read operation
def show_all_students():
    session = Session()
    students = session.query(Student).all()  # Get all students
    print("\nAll Students:")
    for student in students:
        print(student)
    session.close()

# Update operation
def update_student():
    session = Session()
    roll = int(input("Enter roll number to update: "))
    # Find student by roll number
    student = session.query(Student).filter_by(roll=roll).first()
    
    if student:
        new_age = int(input("Enter new age: "))
        student.age = new_age    # Update age
        session.commit()         # Save changes
        print(f"Updated student: {student}")
    else:
        print(f"No student found with roll number {roll}")
    session.close()

delete.py (Delete Operation):

pythonCopyfrom create_table import Student, Session

def delete_student():
    session = Session()
    roll = int(input("Enter roll number to delete: "))
    # Find student by roll number
    student = session.query(Student).filter_by(roll=roll).first()
    
    if student:
        session.delete(student)   # Mark for deletion
        session.commit()          # Perform deletion
        print(f"Deleted student with roll number {roll}")
    else:
        print(f"No student found with roll number {roll}")
    session.close()
Key Concepts:

Engine: Connection to the database
Session: Manages database transactions
Base: Parent class for all models
Model: Defines table structure
CRUD Operations:

Create: session.add()
Read: session.query()
Update: Direct attribute modification
Delete: session.delete()



The workflow follows a consistent pattern:

Start a session
Perform database operation
Commit changes (if any)
Close the session

Each file builds on create_table.py, which sets up the database structure and provides the model and session factory for other operations.