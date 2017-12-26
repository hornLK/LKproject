from flask import render_template
from . import errors


@errors.app_errorhandler(404)
def page_not_foud(e):
    return render_template('errors/404.html')

@errors.app_errorhandler(500)
def page_not_foud(e):
    return render_template('errors/500.html')

