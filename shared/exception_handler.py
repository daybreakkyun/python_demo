from flask import Blueprint
from marshmallow.exceptions import ValidationError
from .custom_exception import EntityNotFound
import traceback
import logging
import uuid

error = Blueprint(name="error_handlers", import_name=__name__)

@error.app_errorhandler(ValidationError)
def handleException(e):
    log_error()
    return "{}".format(e), 400

@error.app_errorhandler(EntityNotFound)
def handleException(e):
    log_error()
    return "{}".format(e), 404

# Generic error is being thrown over here
@error.app_errorhandler(Exception)
def handleException(e):
    exception_key = log_error()
    return "Server Error: {} | Exception-Key: {}".format(e, exception_key), 500

# Setting up exception key so error is going to be easier to find in logs
def log_error():
    exception_key = uuid.uuid4()
    logging.error("Exception-Key: %s", exception_key)
    traceback.print_exc()
    return exception_key