from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role, UserUpdateRequest
from uuid import UUID, uuid4

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("07703279-c5c0-4450-86b6-f7f51c9d29e2"),
        first_name="Ryan",
        last_name="dee",
        middle_name=None,
        gender= Gender.male,
        roles=[Role.student]
        ),
     User(
        id=UUID("b12b2502-dcab-4b16-9358-da282e49eae7"),
        first_name="Sandy",
        last_name="bee",
        middle_name=None,
        gender= Gender.female,
        roles=[Role.admin]
        ),
     User(
        id=UUID("5a623892-4c63-4a4c-b32c-cf511919167f"),
        first_name="charlie",
        last_name="sheen",
        middle_name=None,
        gender= Gender.male,
        roles=[Role.user]
        )
]

@app.get("/")
async def root():
    return {"Hello":"world"}

@app.get("/users")
async def fetch_users():
    return db

@app.post("/users")
async def register_user(user: User):
    db.append(user)
    return {"id" : user.id}

@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail=f"Error user with id: {user_id} does not excist"
    )

@app.put("/users/{user_id}")
async def update_user(user_id: UUID,update_user:UserUpdateRequest):
    for user in db:
        if user.id == user_id:
            if update_user.first_name is not None:
                user.first_name = update_user.first_name
                return
            if update_user.last_name is not None:
                user.last_name = update_user.first_name
                return
            if update_user.middle_name is not None:
                user.middle_name = update_user.middle_name
                return
            if update_user.roles is not None:
                user.roles = update_user.roles
                return
        
    raise HTTPException(
        status_code=404,
        detail= f"User {user_id} not found"
    )