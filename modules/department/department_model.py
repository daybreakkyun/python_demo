from sqlalchemy import Column, Integer, String, Enum
from shared.engine import db
import enum

class DepartmentCode(enum.Enum):
    HR = "HR"
    FI = "FI"
    OP = "OP"
    IT = "IT"

    def __repr__(self) -> str:
        return "{}".format(self.value)

class Department(db.Model):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    code = Column(Enum(DepartmentCode))
    persons = db.relationship("Person", backref="department")

