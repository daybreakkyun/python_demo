from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_enum import EnumField
from marshmallow import fields
from modules.department.department_model import Department, DepartmentCode
from modules.person.person_schema import PersonSchema

class DepartmentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        load_instance = True
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    code = EnumField(DepartmentCode, by_value=True, required=True)
    persons = fields.List(
        fields.Nested(
            PersonSchema(exclude=["birth_date", "gender", "department_id"])
        )
    )

schema = DepartmentSchema()
schema_list = DepartmentSchema(many=True)