from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import crud, schema
from .database.db import SessionLocal

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


@app.get("/scientist/{first_name}", response_model=schema.Scientist)
async def read_scientist_by_first_name(first_name: str, db: Session = Depends(get_db)):
    treated_first_name = first_name.lower().capitalize()
    scientist = crud.get_scientist_by_first_name(db, first_name=treated_first_name  )
    if scientist is None:
        raise HTTPException(status_code=404, detail="Scientist Not Found!")
    return scientist


@app.post("/scientist/", response_model=schema.Scientist)
async def create_scientist(scientist: schema.ScientistCreate, db: Session = Depends(get_db)):
    full_name = scientist.first_name + " " + scientist.last_name
    scientist_db = crud.get_scientist_by_full_name(db, full_name=full_name)
    if scientist_db:
        raise HTTPException(status_code=400, detail="This Scientist already exists!")
    return crud.create_scientist(db=db, scientist=scientist)