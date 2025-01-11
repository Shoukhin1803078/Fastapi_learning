#Database setup
# Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create database engine
# engine = create_engine("postgresql://postgres:your_password@localhost:5432/testing")
engine = create_engine("postgresql://postgres:1803078Boss%40%23%24%25%26@localhost:5432/testing")


# Create session factory
Session = sessionmaker(bind=engine)


# Create base class for models
Base = declarative_base()

# Define Student model
class Student(Base):
    __tablename__ = 'student'  # Table name in database
    
    # Define columns
    id = Column(Integer, primary_key=True)  
    name = Column(String(50))               
    roll = Column(Integer, unique=True)     
    age = Column(Integer)                   
    
    # String representation of Student object
    def __repr__(self):
        return f"{self.name} {self.roll} {self.age}"
        # return f"Name: {self.name}, Roll: {self.roll}, Age: {self.age}"

# Create tables in database
if __name__ == "__main__":
    Base.metadata.create_all(engine)

















# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # engine = create_engine("postgresql://postgres:1803078Boss@#$%&@localhost:5432/testing")
# engine = create_engine("postgresql://postgres:1803078Boss%40%23%24%25%26@localhost:5432/testing")
# Session = sessionmaker(bind=engine)
# Base = declarative_base()

# class Student(Base):
#     __tablename__ = 'student'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     roll = Column(Integer, unique=True)
#     age = Column(Integer)
    
#     def __repr__(self):
#         return f"Name: {self.name}, Roll: {self.roll}, Age: {self.age}"

# if __name__ == "__main__":
#     Base.metadata.create_all(engine)
#     print("Table created successfully!")