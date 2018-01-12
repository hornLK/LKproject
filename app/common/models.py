from .. import db
from .. import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

##--define role table
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship("User",backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

##--define user table
class User(UserMixin,db.Model):
    __tablename__="users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(64),unique=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    group_id = db.Column(db.Integer,db.ForeignKey('groups.id'))
    department_id = db.Column(db.Integer,db.ForeignKey('departments.id'))
    
    #--if get password return error
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def generate_auth_token(self,expiration):
        s = Serializer(current_app.config['SECRET_KEY'],expires_in=expiration)
        return s.dumps({'id':self.id})
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def __repr__(self):
        return '<User %r>' % self.email

##--define group table
class Group(db.Model):
    __tablename__="groups"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    groupname = db.Column(db.String(64),unique=True)
    users = db.relationship("User",backref='group')

    def __repr__(self):
        return '<User %r>' % self.groupname
##--define department
class Department(db.Model):
    __tablename__="departments"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    departmentname = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref="department")
