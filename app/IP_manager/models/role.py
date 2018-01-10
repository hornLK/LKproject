from .. import db
from users import User
from group import Group

class Role(db.Model):
    __tablename = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship("User",backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name
