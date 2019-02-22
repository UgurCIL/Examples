import nmap

nm = nmap.PortScanner()
result = nm.scan("192.168.248.129","1-1000")

ports = result['scan']['192.168.248.129']['tcp'].keys()

for port in ports:
    port_result = result['scan']['192.168.248.129']['tcp'].get(port)
    reason = port_result['reason']
    product = port_result['product']
    print port, product, reason
