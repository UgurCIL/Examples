from scapy.all import *

def paket_callback(paket):
   print paket.src, '->', paket.dst

sniff(prn=paket_callback, store=0, count=10)
