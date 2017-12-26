from flask import render_template,session,redirect,url_for

from .. import cmdb 

@cmdb.errorhandler(404)
def page_not_foud(e):
    return render_template('errors/404.html'),404

@cmdb.errorhandler(500)
def page_not_foud(e):
    return render_template('errors/500.html'),500

