from scapy.all import *

def SendICMP():
   ip = IP(ttl=10, dst="8.8.8.8", src="10.10.10.1")
   icmp = ICMP(type=8, code=0)
   paket = ip/icmp
   send(paket, inter=1, count=5)

def SendICMPEth():
   eth = Ether(src="00:00:00:00:00:00", dst="00:00:00:00:00:00")
   ip = IP(ttl=10, dst="8.8.8.8", src="10.10.10.1")
   icmp = ICMP(type=8, code=0)
   paket = eth/ip/icmp
   sendp(paket, inter=1, count=5)

def SendTCP():
   tcp = TCP(sport=8080, dport=22, flags="S")
   ip = IP(src="127.0.0.1", dst="127.0.0.1")
   paket = ip/tcp
   send(paket, inter=1, count=3)

def SendDNS():
   ip = IP(dst="8.8.8.8")
   udp = UDP(dport=53)
   dns = DNS(rd=1, qd=DNSQR(qname="www.stm.com.tr"))
   paket = ip/udp/dns
   send(paket, inter=1, count=3)

def SendDHCP():
   ip = IP(src="0.0.0.0", dst="255.255.255.255")
   udp = UDP(sport=68, dport=67)
   dhcp = DHCP(options=[("lease_time", 70000)])
   paket = ip/udp/dhcp
   send(paket, inter=1, count=3)
