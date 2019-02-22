from scapy.all import *

def pkt_callback(pkt):
    if pkt.haslayer(ICMP):
        print pkt.src, "->", pkt.dst

sniff(prn=pkt_callback, count=10)
