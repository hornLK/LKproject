from flask import url_for
from .. import db

#--define network talbe
class Network(db.Model):
    __tablename__="networks"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    netname = db.Column(db.String(64),unique=True,index=True)
    active_ip = db.Column(db.Integer)
    total_ip = db.Column(db.Integer)
    network = db.Column(db.String(32),unique=True,index=True)
    desc = db.Column(db.String(64))
    vlan = db.Column(db.String(10),index=True)
    ips = db.relationship("Ips",backref='ips')
    
    def to_json(self):
        json_network={
		'url':url_for('api.get_network',id=self.id,_external=True),
		'id':self.id,
		'netname':self.netname,
		'network':self.network,
		'vlan':self.vlan,
		'desc':self.desc,
		'ip_count':self.ips.__len__()
	    }    
        return json_network
    def page_json(self):
        json_network={
		'url':url_for("ipmage.get_network",id=self.id,page=1,_external=True)
	    }
        return json_network
    def __repr__(self):
        return '<NetNname %r>' % self.netname

#--define ip list table
class Ips(db.Model):
    __tablename__="ips"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    ip = db.Column(db.String(64),index=True)
    mac = db.Column(db.String(64))
    ports = db.Column(db.Text)
    status = db.Column(db.Boolean)
    network_id = db.Column(db.Integer,db.ForeignKey('networks.id'))

    @staticmethod
    def from_json(json_post):
        ip = json_post.get('ip')
        if ip is None or ip == "":
            raise ValidationError("post does not have a IP!")
        return json_post

    def to_dic(self):
        json_ips = {
            "ip" : self.ip,
            "mac" : self.mac,
	    "ports" : self.ports,
	    "status" : self.status,
            "network_id" : self.network_id
        }
        return json_ips
    def __repr__(self):
        return '<ip %r>' % self.ip

