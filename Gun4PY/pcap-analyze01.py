from scapy.all import *

# PCAP dosyasini Scapy dek' rdpcap ile okuduk
packets = rdpcap('example.pcap')

# Herbir paket uzerinden sirayla geciyoruz
for packet in packets:
    # Sadece DNS Round Robin katmani olan paketleri dikkate aliyoruz
    if packet.haslayer(DNSRR):
        # an(swer)
        if isinstance(packet.an, DNSRR):
            print packet.an.rrname
