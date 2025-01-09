from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import mysql.connector


app=FastAPI()

# def get_db_connecion():
#     return mysql.connector.connect(host="localhost",user="root",password="",database="fastapi_learning")

class UserInfoCreate(BaseModel):
    username:str
    roll:int



@app.get("/")
def root():
    return {"message":"This is alamins website"}




@app.post("/user/")
def create_user(user:UserInfoCreate):
    db= mysql.connector.connect(host="localhost",user="root",password="",database="fastapi_learning")
    
    cursor=db.cursor()

    query="INSERT INTO user_info(username,roll) VALUES(%s,%s)"

    print(f"User name: {user.username}")
    values=(user.username,user.roll)

    cursor.execute(query,values)
    db.commit()
    cursor.close()
    db.close()
    return {
        "message":"User created successfully",
        "username":user.username,
        "roll":user.roll
        }


@app.get("/user/display/")
def display_user():
    db= mysql.connector.connect(host="localhost",user="root",password="",database="fastapi_learning")
    cursor=db.cursor(dictionary=True)
    # query="SELECT * FROM user_info"
    query="SELECT username,roll FROM user_info "
    cursor.execute(query)
    result=cursor.fetchall()
    print(f"result= {result}")
    cursor.close()
    db.close()
    return {
        "message":"User displayed successfully",
        "data":result
    }



# @app.get("/users/")
# def get_users():
#     try:
#         db = mysql.connector.connect(host="localhost",user="root",password="",database="fastapi_learning")
#         cursor = db.cursor(dictionary=True)
#         query = "SELECT username, roll FROM user_info"
#         cursor.execute(query)
#         users = cursor.fetchall()
#         cursor.close()
#         db.close()
#         if not users:
#             raise HTTPException(status_code=404, detail="No users found")
#         return {"users": users}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))