import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '915192a1-8625-43a7-9aa3-a1e3350fbf0f'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = "[lk_ADMIN]"
    FLASKY_MAIL_SENDER = 'LK_ADMIN<admin@pdmi.cn>'
    FLASKY_ADMIN = os.environ.get("FLASKY_ADMIN") or "liukaiqiang@pdmi.cn"

    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.pdmi.cn' 
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") or "liukaiqiang@pdmi.cn"
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") or "Tianlkq0608"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123123@10.18.74.35:3306/Flask_db"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlit:///' + os.path.join(basedir,'data-test.sqlite')

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'default':DevelopmentConfig
}
