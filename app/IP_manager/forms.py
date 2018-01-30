from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Required, Length,Regexp
from wtforms import ValidationError
from .models import Network,Ips

class addNetForm(FlaskForm):
    netname = StringField('网络名',validators=[Required(),Length(1,64)])
    network = StringField('网段',validators=[Required()])
    vlan = StringField('vlan')
    desc = StringField("描述",)
    submit = SubmitField("添加")

    def validate_netname(self,netname):
        if Network.query.filter_by(netname=netname.data).first():
            raise ValidationError('这个网络已经添加') 
