from scapy.all import *

paketler = rdpcap("yeniarsiv.pcap")
file = open("IECache.7z", "w")

for paket in paketler:
    file.write(paket[Raw].load[4:])

file.close()
