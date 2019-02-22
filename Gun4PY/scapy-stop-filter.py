from scapy.all import *
import sys

def kontrol(pkt):
   if pkt.haslayer(TCP):
      sys.exit()

reply = sniff(stop_filter = kontrol)
print reply.summary()
