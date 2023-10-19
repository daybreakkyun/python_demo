from flask import Blueprint, request
from modules.person import person_service
from shared.event_handler.callback_model import Callback

api = Blueprint("person_blueprint", __name__, url_prefix="/person")
callback = Callback()

@api.route("/", methods = ["GET"])
def get_persons():
    return person_service.find_all(), 200

@api.route("/<id>", methods = ["GET"])
def get_person_by_id(id):
    return person_service.find_by_id(id), 200

@api.route("/<id>", methods = ["DELETE"])
def delete_person(id):
    person_service.delete(id)
    return "Succeeded!", 200

@api.route("/", methods = ["POST"])
def post_person():
    person_service.save(request.get_json())
    return "Succeeded!", 201