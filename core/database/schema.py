from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class ScientistBase(BaseModel):
    first_name: str
    last_name: str
    nationality: str
    date_of_birth: datetime
    nobel_prize: bool
    city_of_birth: str


class ScientistCreate(ScientistBase):
    pass


class Scientist(ScientistBase):
    id: int

    class Config:
        orm_mode = True
