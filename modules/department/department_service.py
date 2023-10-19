from modules.department.department_model import Department
from modules.department import department_schema
from shared.custom_exception import EntityNotFound
from sqlalchemy.exc import NoResultFound

def find_all_departments():
    list = Department.query.all()
    return department_schema.schema_list.dump(list)

def find_department_by_code(code):
    try:
        department = Department.query.filter(Department.code == code).one()
        return department_schema.schema.dump(department)
    except NoResultFound:
        raise EntityNotFound("Department code ({}) not found".format(code))
