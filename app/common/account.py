from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user

from .forms import LoginForm
from . import account

@account.route("/",methods=['GET','POST'])
def login():
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        useremail = form.email.data
        password = form.password.data
        print(useremail)
    else:
        useremail="guest"
        flash("无效的用户或者密码")
    return render_template('account/login.html',form=form,useremail=useremail)
