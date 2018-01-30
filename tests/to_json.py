def to_postjson(network_id,scan):
    ips = {}
    for ip,data in scan.items():
        if data["status"]["state"] == "up":
            ips[ip] = {
                "ip" : data["addresses"]["ipv4"],
                "mac" : data["addresses"]["mac"],
                "ports" : ",".join([str(x) for x in data.get("tcp",[]).keys()]),
                "status": True,
                "network_id" : int(network_id)
            }
        else:
            ips[ip] = {
                "ip" : data["addresses"]["ipv4"],
                "mac" : "",
                "ports": "",
                "status": False,
                "network_id" : int(network_id)
            }

    print(ips)

if __name__ == "__main__":
    js={'10.18.74.1': {'hostnames': [{'name': '', 'type': ''}], 'addresses': {'ipv4': '10.18.74.1', 'mac': 'A0:36:9F:70:71:88'}, 'vendor': {'A0:36:9F:70:71:88': 'Intel Corporate'}, 'status': {'state': 'up', 'reason': 'arp-response'}, 'tcp': {22: {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 3306: {'state': 'open', 'reason': 'syn-ack', 'name': 'mysql', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 5000: {'state': 'open', 'reason': 'syn-ack', 'name': 'upnp', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 8000: {'state': 'open', 'reason': 'syn-ack', 'name': 'http-alt', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 8080: {'state': 'open', 'reason': 'syn-ack', 'name': 'http-proxy', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}}}, '10.18.74.2': {'hostnames': [{'name': '', 'type': ''}], 'addresses': {'ipv4': '10.18.74.2', 'mac': 'A0:36:9F:71:67:D8'}, 'vendor': {'A0:36:9F:71:67:D8': 'Intel Corporate'}, 'status': {'state': 'up', 'reason': 'arp-response'}, 'tcp': {22: {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 139: {'state': 'open', 'reason': 'syn-ack', 'name': 'netbios-ssn', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 445: {'state': 'open', 'reason': 'syn-ack', 'name': 'microsoft-ds', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 3306: {'state': 'open', 'reason': 'syn-ack', 'name': 'mysql', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 5000: {'state': 'open', 'reason': 'syn-ack', 'name': 'upnp', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 9100: {'state': 'open', 'reason': 'syn-ack', 'name': 'jetdirect', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}}}}
    to_postjson(2,js)
