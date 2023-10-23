from flask_restx import Resource, Namespace, fields
from modules.person import person_service

api = Namespace(name="person", description="Basically API for Person")

resource_fields = api.model('Person', {
    'birth_date': fields.Date,
    'gender': fields.String
})

@api.route("")
class GetPersonList(Resource):
    def get(self):
        return person_service.find_all(), 200

    def post(self):
        person_service.save(api.payload)
        return "", 201        
    
@api.route("/<string:id>")
class GetPersonById(Resource):
    def get(self, id):
        return person_service.find_by_id(id), 200

    def delete(self, id):
        person_service.delete(id)
        return "", 201        