from bson import ObjectId
from fastapi import APIRouter

from models.user import User
from config.db import connection
from schemas.user import userEntity, usersEntity
from bson import ObjectId

user = APIRouter()


@user.get("/")
async def find_all_address():
    return usersEntity(connection.local.user.find())


@user.get("/{id}")
async def get_one_address(id):
    return userEntity(connection.local.user.find_one({"_id": ObjectId(id)}))


@user.post("/")
async def create_address(user: User):
    connection.local.user.insert_one(dict(user))
    return usersEntity(connection.local.user.find())


@user.put("/{id}")
async def update_address(id, user: User):
    (connection.local.user.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)}))
    return userEntity(connection.local.user.find_one({"_id": ObjectId(id)}))


@user.delete("/{id}")
async def delete_address(id):
    return userEntity(connection.local.user.find_one_and_delete({"_id": ObjectId(id)}))
