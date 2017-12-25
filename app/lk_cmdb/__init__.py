from flask import Blueprint

cmdb = Blueprint('cmdb',__name__)
from . import views, errors
from .. import db
from .. import mail
