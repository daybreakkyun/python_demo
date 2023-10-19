from modules.person import person_schema
from modules.person.person_model import Person
from shared.sql_engine import db
from shared.custom_exception import EntityNotFound

def find_all():
    person_list = Person.query.all()
    return person_schema.schema_list.dump(person_list)

def find_by_id(id):
    person = get_person(id)
    return person_schema.schema.dump(person)

def save(data):
    new_person: Person = person_schema.schema.load(data=data, session=db.session)
    db.session.add(new_person)
    db.session.commit()

def delete(id):
    person = Person.query.get(id)

    if (person is None):
        raise EntityNotFound("id {} not found".format(id))

    db.session.delete(person)
    db.session.commit()

def get_person(id):
    person = Person.query.get(id)

    if (person is None):
        raise EntityNotFound("id {} not found".format(id))    

    return person    