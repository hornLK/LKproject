import nmap

def callback_print(host,scan_data):
    with open("nmap.log","wb") as f:
        f.write(host)
nm = nmap.PortScannerAsync()
nm.scan(hosts="10.18.74.0/24",arguments='-sP -PI -PT',callback=callback_print)
print(dir(nm))
