from flask import Blueprint

cmdb = Blueprint('cmdb',__name__)
from .views import index
from .views import errors
from .. import db
from .. import mail
