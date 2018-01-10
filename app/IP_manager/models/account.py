from .. import db

##--define role table
class Role(db.Model):
    __tablename = 'roles'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship("User",backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

##--define user table
class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(64),unique=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    group_id = db.Column(db.Integer,db.ForeignKey('group.id'))
    def __repr__(self):
        return '<User %r>' % self.username

##--define group table
class Group(db.Model):
    __tablename__="group"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    groupname = db.Column(db.String(64),unique=True)
    users = db.relationship("User",backref='group')

    def __repr__(self):
        return '<User %r>' % self.groupname
