from .run_celery import app
from celery.utils.log import get_task_logger
from datetime import datetime
import requests,logging,nmap,json
from config import *

logger = get_task_logger(__name__)

logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='/tmp/auto_nmap.log',  
                    filemode='w')  

@app.task(bind=True)
def div(self,x,y):
    logger.info(('Executing task id {0.id},args:{0.args!r} kwargs:{0.kwargs!r}').format(self.request))
    try:
        result = x/y
    except ZeroDivisionError as e:
        raise self.retry(exec=e,countdown=5,max_retries=3)
    with open('/tmp/div.log','a+') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+str(result))
    return result

def to_postjson(network_id,scan):
    Ips = {}
    try:
        for ip,data in scan.items():
            if data["status"]["state"] == "up":
                Ips[ip] = {
		    "ip" : data["addresses"].get("ipv4"),
                    "mac" : data["addresses"].get("mac",""),
                    "ports" : ",".join([str(x) for x in data.get("tcp",{}).keys()]),
                    "status": True,
		    "network_id" : network_id
		} 
            else:
                Ips[ip] = {
		    "ip" : data["addresses"].get("ipv4"),
		    "mac" : "",
		    "ports" : "",
		    "status" : False,
		    "network_id" : network_id
		}
        return Ips
    except Exception as e:
        print (e)

def scan_host(networks):
    nm = nmap.PortScanner()
    url = "http://"+SERVER_HOST+":"+str(SERVER_PORT)+"/api/v1.0/ips/post_ips/"
    for network_dic in networks:
        network_data = {}
        res = nm.scan(hosts=network_dic.get("network",None),arguments="-F -T4 -n -PI -PT")
        ips =to_postjson(int(network_dic.get("id")),res.get("scan")) 
        print(ips)
        network_data={"network_id":network_dic.get("id"),"uphosts":res["nmap"]["scanstats"].get("uphosts"),"totalhosts":res["nmap"]["scanstats"].get("totalhosts"),"ips":ips}
        responst_res = requests.post(url,auth=(SERVER_TOKEN,""),data=json.dumps(network_data))

@app.task
def nmap_host():
    url = "http://"+SERVER_HOST+":"+str(SERVER_PORT)+"/api/v1.0/networks/list_network/"
    try:
        response_res = requests.get(url,auth=(SERVER_TOKEN,""))
        if response_res.status_code == 200:
            network_list=response_res.json().get("networks")
            scan_host(network_list)
            return network_list
        elif response_res.status_code == 401:
            print("401")
            logging.error('error invade auth status code 401') 
            return  None
        else:
            print("error")
            logging.error("unexpected error",status_code)
            return None
    except Exception as e:
        if e is None:
            e="server is not running"
            logging.error('error-'+e) 


