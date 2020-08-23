from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import crud, schema
from .database.db import SessionLocal

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Welcome to SciAPI!"}