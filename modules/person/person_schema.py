from marshmallow import fields
from modules.person.person_model import Person, Gender
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_enum import EnumField
from modules.department.department_model import Department, DepartmentCode

class DepartmentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        load_instance = True
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    code = EnumField(DepartmentCode, by_value=True, required=True)

class PersonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
    name = fields.Str(required=True)
    birth_date = fields.Date(format="%Y-%m-%d", required=True)
    gender = EnumField(Gender, by_value=True, required=True)
    department_id = fields.Int()
    department = fields.Nested(DepartmentSchema(exclude=["id", "description", "code"]))

schema = PersonSchema()
schema_list = PersonSchema(many=True)
