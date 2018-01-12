from flask import render_template, request, jsonify
from . import errors


@errors.app_errorhandler(404)
def page_not_foud(e):
    if request.accept_mimetypes.accept_json and \
	    not request.accept_mimetypes.accept_html:
        response = jsonify({'error':"not found"})
        response.status_code = 404
        return response
    return render_template('errors/404.html')

@errors.app_errorhandler(500)
def page_not_foud(e):
    if request.accept_mimetypes.accept_json and \
	    not request.accept_mimetypes.accept_html:
        response = jsonify({'error':"network error"})
        response.status_code = 500
        return response
    return render_template('errors/500.html')

