from fastapi import FastAPI
from pydantic import BaseModel, Field

app=FastAPI()

users =[]

class User(BaseModel):
    name : str
    email : str
    age : int = Field(gt=18)

# create Users
@app.post("/users/post")
async def create_user(user:User): 
    users.append(user.model_dump())
    return {"message":"User ceated!", "user":user.model_dump()}

# Read All Users
@app.get("/users")
async def get_user():
    return {"users":users}

# Read single user
@app.get("/users/{user_id}")
async def get_user(user_id:int):
    if user_id < len(users):
        return users[user_id]
    return {"error": "user not found"}

# Update User
@app.put("/users/{user_id}")
async def update_user(user_id:int, update_user:User):
    if user_id < len(users):
        users[user_id] = update_user.model_dump()
        return {"MEssage": "user upated", "user":users[user_id]}
    return {"error":"user not found"}

@app.delete("users/{user_id}")
async def delete_user(user_id:int):
    if user_id < len(users):
        deleted_user = users.pop(user_id)
        return {"message": "user deleted", "user":deleted_user}
    return {"error": "User not found"}