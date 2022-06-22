from fastapi import FastAPI
from routes.user import user
app = FastAPI(
    title="Address Manager with MongoDB",
    description="Perform CRUD operations on a MongoDB database using the fastapi services"
)
app.include_router(user)
