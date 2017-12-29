from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user

from .account_forms import LoginForm
from . import account

@account.route("/",methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    print(form.validate(),form.csrf_token())
    print(form.errors)
    if request.method == "POST" and form.validate():
        useremail = form.email.data
        password = form.password.data
    else:
        flash("无效的用户或者密码","error")
    return render_template('account/login.html',form=form)
