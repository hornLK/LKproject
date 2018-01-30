from flask import request, jsonify,g,url_for,current_app
from .. import db
from ..IP_manager.models import Network, Ips
from . import api
from .errors import forbidden
import json

@api.route('/networks/list_network/',methods=['GET'])
def get_networks():
    try:
        networks=Network.query.all()
    except errorclass as e:
        return None
    else:
        return jsonify({"networks":[network.to_json() for network in networks]})

@api.route('/networks/network/<int:id>/')
def get_network(id):
    network = Network.query.get_or_404(id)
    return jsonify(network.to_json())

@api.route('/networks/mage/',methods=["POST"])
def post_network():
    if request.method == "POST":
        network = Network.from_json(request.json)
        db.session.add(network)
        db.session.commit()
        return jsonify(network.to_json()),201,\
                {'Location':url_for('api.get_network',id=network.id)}
        
@api.route('/ips/post_ips/',methods=["POST"])         
def post_ip():
    if request.method == "POST":
                  
        """
        if Ips.from_json(post_data):
            ip = Ips(ip=post_data.get("ip"),mac=post_data.get("mac"),ports=post_data.get("ports"),status=post_data.get("status"),network_id=post_data.get("network_id"))
        """
        try:
            post_data = json.loads(request.data)
            network_obj = Network.query.get_or_404(int(post_data.get('network_id')))
            network_ips = network_obj.ips
            network_obj.active_ip = int(post_data.get('uphosts'))
            network_obj.total_ip = int(post_data.get('totalhosts'))-2
            db.session.add(network_obj)
            db.session.commit()
            if network_ips == [] and post_data:
                for ip,data in post_data.get("ips").items():
                    ip_obj = Ips(ip=ip,mac=data.get("mac"),ports=data.get("ports"),status=data.get("status"),network_id=data.get("network_id")) 
                    db.session.add(ip_obj)
                db.session.commit()
                return jsonify({"create":",".join(post_data.get("ips").keys())}),201
            else:
                db_dic = {}
                for ip in network_ips:
                    db_dic[ip.ip]=ip
                else:
                    #add/update/delete  ip list
                    update_dic = {
		    "update":[i for i in db_dic.keys() if i in post_data.get("ips").keys()],
		    "add":list(set(post_data.get("ips").keys()).difference(set(db_dic.keys()))),
                    "delete":list(set(db_dic.keys()).difference(set(post_data.get("ips").keys())))
		    } 
                    #add ip
                    if update_dic.get("add"):
                        for addip in update_dic.get("add"):
                            data = post_data.get("ips").get(addip)
                            ip_obj = Ips(ip=addip,mac=data.get("mac"),ports=data.get("ports"),status=data.get("status"),network_id=data.get("network_id"))
                            db.session.add(ip_obj)
                        db.session.commit() 
                    if update_dic.get("update"):
                        for updateip in update_dic.get("update"):
                            if not db_dic.get(updateip).to_dic() == post_data.get("ips")[updateip]:
                                db_dic.get(updateip).mac = post_data.get("ips")[updateip]["mac"]
                                db_dic.get(updateip).ports = post_data.get("ips")[updateip]["ports"]
                                db_dic.get(updateip).status = post_data.get("ips")[updateip]["status"]
                                db.session.add(db_dic.get(updateip))
                                print(updateip)
                            db.session.commit()
                   
                    if update_dic.get("delete"):
                        for deleteip in update_dic.get("delete"):
                            db.session.delete(db_dic.get(deleteip))
                            db.session.commit()              
                print(update_dic)
                return "ok"
        except KeyError as e:
            return "error"

