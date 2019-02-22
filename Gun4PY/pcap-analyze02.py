from scapy.all import *

packets = rdpcap('narsiv.pcap')

file = open("IECache.7z", "w")

for packet in packets:
    file.write(packet[Raw].load[4:])

file.close()
