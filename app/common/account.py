from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user, login_required,logout_user

from .account_forms import LoginForm
from .registration_forms import RegistrationForm
from .models import Department, User
from .. import db
from . import account

@account.route("/",methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        print(dir(user))
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('cmdb.index'))
        flash("无效的用户或者密码","danger")
    return render_template('account/login.html',form=form)

@account.route('/register',methods=["POST","GET"])
def register():
    form = RegistrationForm(request.form)
    if form.is_submitted() and form.validate():
        user = User(email=form.email.data,password=form.password.data,department_id=form.department.data)
        db.session.add(user)
        flash("注册成功，请等待核实！")
        return redirect(url_for('account.login'))
    form.department.choices = [(g.id, g.departmentname) for g in Department.query.order_by('departmentname')]
    return render_template('account/register.html',form=form)

@account.route("/logout")
@login_required
def logout():
    logout_user()
    flash('谢谢使用！')
    return redirect(url_for('cmdb.index'))
