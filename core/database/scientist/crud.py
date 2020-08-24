from sqlalchemy.orm import Session
from . import schema
from .scientist import models


def get_scientist(db: Session, scientist_id: int):
    return db.query(models.Scientist).filter(models.Scientist.id == scientist_id).first()


def get_scientist_by_first_name(db: Session, first_name: str):
    return db.query(models.Scientist).filter(models.Scientist.first_name == first_name).first()


def get_scientist_by_full_name(db: Session, full_name: str):
    return db.query(models.Scientist).filter(models.Scientist.full_name == full_name).first()


def get_scientists(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Scientist).offset(skip).limit(limit).all()


def create_scientist(db: Session, scientist: schema.ScientistCreate):
    db_scientist = models.Scientist(
        first_name=scientist.first_name,
        last_name=scientist.last_name,
        date_of_birth=scientist.date_of_birth,
        nationality=scientist.nationality,
        city_of_birth=scientist.city_of_birth,
        nobel_prize=scientist.nobel_prize,
    )
    db.add(db_scientist)
    db.commit()
    db.refresh(db_scientist)
    return db_scientist
