from datetime import datetime
from flask import render_template,session,redirect,url_for,request, flash,current_app, jsonify
from flask_login import login_required
from . import ipmage
from sqlalchemy import and_
from .models import Network, Ips
from .forms import addNetForm
from .. import db

@ipmage.route('/',methods=['GET'])
@login_required
def index():
    add_NetworkForm=addNetForm(request.form)
    try:
        page = request.args.get('page',1,type=int)
        pagination = Network.query.order_by(Network.network.desc()).paginate(page,per_page=current_app.config['FLASKY_NETWORK_PER_PAGE'],error_out=False)
        network_list = pagination.items
        print(network_list)
        ip_count = 0
        active_ip = 0
        for network_obj in network_list:
            ip_count = ip_count + int(network_obj.total_ip) 
            active_ip = active_ip + int(network_obj.active_ip)
        network_count = len(network_list)
    except AttributeError as e:
        error_message = "Connection Error"+e 
        return render_template('IPmanage/index.html',add_NetworkForm=add_NetworkForm,pagination=pagination,data={"networks":[],"ip_count":0,"network_count":network_count,"active_ip":0,"message":error_message})
    else:
        return render_template('IPmanage/index.html',add_NetworkForm=add_NetworkForm,pagination=pagination,data={"networks":network_list,'ip_count':ip_count,"network_count":network_count,"active_ip":active_ip,"message":"sessuce"})

@ipmage.route('/addnetwork/',methods=['POST'])
@login_required
def add_network():
    form = addNetForm(request.form)
    if form.is_submitted() and form.validate():
        if form.vlan.data:
            network = Network(netname=form.netname.data,network=form.network.data,vlan=int(form.vlan.data),desc=form.desc.data)
        else:
            network = Network(netname=form.netname.data,network=form.network.data,desc=form.desc.data)
        db.session.add(network)
        flash("添加成功！")
        return redirect(url_for('ipmage.index'))
    else:
        flash("添加失败！")
        return redirect(url_for('ipmage.index'))
        
@ipmage.route('/getnetwork/',methods=['GET'])
@login_required
def get_network():
    id= request.args.get('id',type=int)
    page = request.args.get('page',1,type=int)
    pagination = Ips.query.filter_by(network_id=id).order_by(Ips.ip.desc()).paginate(page,per_page=current_app.config['FLASKY_IP_PER_PAGE'],error_out=False)
    ip_list = pagination.items
    return render_template("IPmanage/ip_detail.html",network_id=id,ip_list=ip_list,pagination=pagination)

@ipmage.route('/ip/search_ip/',methods=['POST'])
@login_required
def search_ip():
    if request.method =="POST":
        column = request.values.get("column",None)
        input_info = request.values.get("input",None)
        network_id = request.values.get("network_id",None)
        if column and input_info:
            if column == "ip":
                search_ip = Ips.query.filter(and_(Ips.network_id==int(network_id),Ips.ip==input_info)).first()
                if search_ip:
                    search_info = search_ip.to_dic()
                    return  jsonify({"type":"ip","data":search_info})
                else:return jsonify({"data":None})
            elif column == "mac":
                search_mac = Ips.query.filter(and_(Ips.network_id==int(network_id),Ips.mac==input_info)).first()
                if search_mac:
                    search_info = search_mac.to_dic()
                    return jsonify({"type":"mac","data":search_info})
                else:return jsonify({"data":None})
            else:
                search_port = Ips.query.filter(and_(Ips.network_id==int(network_id),Ips.ports.like("%"+input_info+"%"))).all()
                if search_port:
                    search_info = [x.to_dic() for x in search_port]
                    return jsonify({"type":"ports","data":search_info})
                else:return jsonify({"data":None})
        else:
            return jsonify({"data":None})
