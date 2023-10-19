from marshmallow import fields
from modules.person.person_model import Person, Gender
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_enum import EnumField

class PersonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
    name = fields.Str(required=True)
    birth_date = fields.Date(format="%Y-%m-%d", required=True)
    gender = EnumField(Gender, by_value=True, required=True)
    department_id = fields.Int()

schema = PersonSchema()
schema_list = PersonSchema(many=True)
