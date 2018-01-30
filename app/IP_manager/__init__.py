from flask import Blueprint

ipmage = Blueprint('ipmage',__name__)
from . import views 
from .. import db
from .. import mail
