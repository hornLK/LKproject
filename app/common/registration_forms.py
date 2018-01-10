from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from .models import User,Department

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[Required(),EqualTo('password2',message="Passwords must match.")])
    password2 = PasswordField('Confirm password',validators=[Required()])
    department = SelectField("department",default=1,coerce=int,choices = [(2, '大数据部'), (1, '平台运维部'), (3, '技术研发部')])
    submit = SubmitField("Register")

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.') 
