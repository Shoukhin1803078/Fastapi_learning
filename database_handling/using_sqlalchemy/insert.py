from database_creation.using_sqlalchemy.create_table import Student, Session

def insert_student():
    session=Session()
    n=input("enter name=")
    r=int(input("enter roll="))
    a=int(input("enter age="))
    st=Student(name=n,roll=r,age=a)
    session.add(st)
    session.commit()
    session.close()

def show_all_students():
    session = Session()
    st = session.query(Student).all()
    print(st)
    print("\nAll Students:")
    for i in st:
        print(i)
        # print(f"students name={i.name} roll={i.roll} age={i.age}")
    session.close()


if __name__=="__main__":
    # insert_student()
    show_all_students()