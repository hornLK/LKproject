from flask import jsonify
from ..exceptions import ValidationError
from . import api

def forbidden(message):
    response = jsonify({'error':"forbidden","message":message})
    response.status_code = 403
    return response

def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response

@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
