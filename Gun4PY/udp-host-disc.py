import socket
import os

HOST = "127.0.0.1"

# Isletim sistemine gore protokol seciliyor.
# Windows gelen butun paketleri protokolden bagimsiz sniff etmeye izin verirken
# Linux de hangi protokolu dinleyeceginizi belirtmelisiniz
if os.name == "nt":
    sock_proto = socket.IPPROTO_IP
else:
    sock_proto = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, sock_proto)

sniffer.bind((HOST,0))

# IP basligini da istedigimizi belirtiyoruz
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# Windowslar icin PROMISCUOUS mod ayarlari
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# Bir paket icin dinlemeye basla
print sniffer.recvfrom(65565)

# Windowslar icin PROMISCUOUS mod kapatiliyor
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
