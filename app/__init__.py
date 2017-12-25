from flask import Flask,render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config

mail = Mail()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .lk_cmdb import cmdb as cmdb_blueprint
    app.register_blueprint(cmdb_blueprint)

    db.init_app(app)
    mail.init_app(app)

    return app
