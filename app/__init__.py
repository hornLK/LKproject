from flask import Flask,render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .lk_cmdb import cmdb as cmdb_blueprint
    from .IP_manager import ipmage as ipmage_blueprint
    from .common import errors as errors_blueprint
    from .common import  account as account_blueprint
    from .api_1_0 import api   as api_blueprint
    app.register_blueprint(cmdb_blueprint,url_prefix='/cmdb')
    app.register_blueprint(errors_blueprint,url_prefix='/errors')
    app.register_blueprint(account_blueprint,url_prefix='/account')
    app.register_blueprint(ipmage_blueprint,url_prefix='/ipmage')
    app.register_blueprint(api_blueprint,url_prefix='/api/v1.0')

    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    return app
