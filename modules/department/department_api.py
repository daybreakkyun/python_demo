from flask_restx import Resource, Namespace, fields
from modules.department import department_service

api = Namespace(name="deparment", description="Basically API for Deparment")

@api.route("")
class GetDepartmentList(Resource):
    def get(self):
        return department_service.find_all(), 200     
    
@api.route("/<string:code>")
class GetPersonByCode(Resource):
    def get(self, code):
        return department_service.find_department_by_code(code), 200