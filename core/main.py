from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from .database import crud, schema
from .database.db import SessionLocal
from .routers.scientists import router

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

