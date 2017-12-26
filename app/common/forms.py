from flask_wtf import FlaskForm
from wtforms import SubmitField,PasswordField,StringField,BooleanField
from wtforms.validators import Required,Email,Length

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Email(),Length(1,64)])
    password = PasswordField("Password",validators=[Required()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('登陆') 
