from flask import Blueprint

ipmage = Blueprint('ipmage',__name__)
from .views import index
from .. import db
from .. import mail
