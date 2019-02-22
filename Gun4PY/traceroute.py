import os
from scapy.all import *

'''
ans, unans = sr(IP(dst="104.20.229.42", ttl=(4,25), id=RandShort())/TCP(flags=0x2))

for snd,rcv in ans:
   print snd.ttl, rcv.src, isinstance(rcv.payload, TCP)
'''

hostname = raw_input('Hedefi girin: ')
ttl = 1

while True:
   #paket = sr1(IP(dst=hostname, ttl=ttl)/ICMP(id=os.getpid()), verbose=0)
   paket = sr1(IP(dst=hostname, ttl=ttl)/ICMP(), verbose=0)
   if paket[ICMP].type == 11 and paket[ICMP].code == 0:
      print ttl, '->', paket.src
      ttl += 1
   elif paket[ICMP].type == 0:
      print ttl, '->', paket.src
      break
