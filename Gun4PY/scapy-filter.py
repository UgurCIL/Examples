from scapy.all import *

ans, unans = sniff(filter="icmp and host 10.10.13.186", count=5)
ans.summary()
