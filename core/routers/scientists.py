from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database.db import SessionLocal
from ..database import crud, schema

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[schema.Scientist])
async def read_scientists(db: Session = Depends(get_db)):
    return crud.get_scientists(db)


@router.get("/{first_name}", response_model=schema.Scientist)
async def read_scientist_by_first_name(first_name: str, db: Session = Depends(get_db)):
    treated_first_name = first_name.lower().capitalize()
    scientist = crud.get_scientist_by_first_name(db, first_name=treated_first_name  )
    if scientist is None:
        raise HTTPException(status_code=404, detail="Scientist Not Found!")
    return scientist


@router.post("/", response_model=schema.Scientist)
async def create_scientist(scientist: schema.ScientistCreate, db: Session = Depends(get_db)):
    full_name = scientist.first_name + " " + scientist.last_name
    scientist_db = crud.get_scientist_by_full_name(db, full_name=full_name)
    if scientist_db:
        raise HTTPException(status_code=400, detail="This Scientist already exists!")
    return crud.create_scientist(db=db, scientist=scientist)