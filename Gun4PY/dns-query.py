from scapy.all import *

dns_server = raw_input("DNS Sunucu Adresi: ")
pack = IP(dst=dns_server)/UDP()/DNS(rd=1, qd=DNSQR(qname="www.google.com"))

result = sr1(pack)

print 'Adres : ' + result.an.rdata
