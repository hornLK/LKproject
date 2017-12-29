from flask_wtf import FlaskForm
from wtforms import SubmitField,PasswordField,StringField,BooleanField
from wtforms.validators import InputRequired,email,Length

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[InputRequired(),email(),Length(1,64)])
    password = PasswordField('Password',validators=[InputRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField("登 陆")
