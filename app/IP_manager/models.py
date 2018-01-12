from .. import db

#--define network talbe
class Network(db.Model):
    __tablename__="networks"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    netname = db.Column(db.String(64),unique=True,index=True)
    desc = db.Column(db.String(64))
    vlan = db.Column(db.Integer,index=True)
    ips = db.relationship("Ips",backref='ips')

    def to_json(self):
        json_network={
		'url':url_for('api.get_network',id=self.id,_external=True),
		'netname':self.netname,
		'vlan':self.vlan,
		'desc':self.desc,
		'ip_count':Ips.query.filter(Ips.id==self.id).count()
	    }    
        return json_network

    def __repr__(self):
        return '<NetNname %r>' % self.name

#--define ip list table
class Ips(db.Model):
    __tablename__="ips"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    ip = db.Column(db.String(64),index=True)
    mac = db.Column(db.String(64))
    ports = db.Column(db.Text)
    network_id = db.Column(db.Integer,db.ForeignKey('networks.id'))
    
    def __repr__(self):
        return '<ip %r>' % self.ip

