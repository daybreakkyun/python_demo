from flask import Blueprint
from modules.department import department_service

api = Blueprint("department_blueprint", __name__, url_prefix="/department")

@api.route("/", methods = ["GET"])
def get_departments():
    return department_service.find_all_departments(), 200

@api.route("/<code>", methods = ["GET"])
def get_department_by_code(code):
    return department_service.find_department_by_code(code)
