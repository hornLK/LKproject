from flask import Blueprint

cmdb = Blueprint('cmdb',__name__)
from .views import index
from .. import db
from .. import mail
