from flask import Blueprint

errors = Blueprint('errors',__name__)
account = Blueprint('account',__name__)
from .errors import *
from .account import *
