from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from shared.sql_engine import db
import enum

class Gender(enum.Enum):
    M = "M"
    F = "F"

    def __repr__(self) -> str:
        return "{}".format(self.value)

class Person(db.Model):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    birth_date = Column(Date)
    gender = Column(Enum(Gender))
    department_id = Column(Integer, ForeignKey("department.id"))

    def __repr__(self) -> str:
        return f"Person(id={self.id!r}, name={self.name!r})"
