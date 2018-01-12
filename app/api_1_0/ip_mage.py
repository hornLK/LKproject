from flask import request
from ..IP_manager.models import Network, Ips
from . import api

@api.route('/networks/')
def get_networks():
    pass
