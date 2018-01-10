from datetime import datetime
from flask import render_template,session,redirect,url_for
from flask_login import login_required
from .. import ipmage

@ipmage.route('/',methods=['GET'])
@login_required
def index():
    return render_template('IPmanage/index.html')
