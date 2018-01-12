import nmap

def callback_print(host,scan_data):
    print("heheh")
    print(host,scan_data)
nm = nmap.PortScannerAsync()
nm.scan(hosts="10.18.74.0/24",arguments='-sP -PI -PT',callback=callback_print)
