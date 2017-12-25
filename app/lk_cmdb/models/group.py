from .. import db

class Group(db.Model):
    __tablename__="group"
    id = db.Column(db.Integer,primary_key=True)
    groupname = db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<User %r>' % self.groupname
