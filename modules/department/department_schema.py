from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_enum import EnumField
from marshmallow import fields
from modules.person.person_model import Person, Gender
from modules.department.department_model import Department, DepartmentCode

class PersonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
    name = fields.Str(required=True)
    birth_date = fields.Date(format="%Y-%m-%d", required=True)
    gender = EnumField(Gender, by_value=True, required=True)

class DepartmentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        load_instance = True
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    code = EnumField(DepartmentCode, by_value=True, required=True)
    persons = fields.List(
        fields.Nested(
            PersonSchema(exclude=["gender", "birth_date"])
        )
    )

schema = DepartmentSchema()
schema_list = DepartmentSchema(many=True)