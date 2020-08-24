from sqlalchemy import Column, String, DateTime, Integer, Boolean
from sqlalchemy.ext.hybrid import hybrid_property
from .db import Base


class Scientist(Base):

    __tablename__ = "scientists"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    nationality = Column(String(50))
    date_of_birth = Column(DateTime)
    nobel_prize = Column(Boolean, default=False)
    city_of_birth = Column(String(50))

    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __repr__(self):
        return f"<Scientist: {self.full_name()}>"

