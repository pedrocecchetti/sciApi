from fastapi import FastAPI
from .database.db import SessionLocal
from .routers.scientist import router

app = FastAPI()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def index():
    return {"Message": "Welcome to The SciAPI"}

app.include_router(router, prefix="/scientist")

