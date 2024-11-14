from fastapi import FastAPI

from database import engine, Base
from routers import user_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_router.router, prefix="/user")
