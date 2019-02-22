import socket, sys
from struct import *

def eth_addr (a) :
  b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
  return b

try:
	s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
except socket.error , msg:
	print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

while True:
	packet = s.recvfrom(65565)
	
	packet = packet[0]
	
	# Ethernet baslik uzunlugu
	eth_length = 14
	
	eth_header = packet[:eth_length]
	eth = unpack('!6s6sH' , eth_header)
	eth_protocol = socket.ntohs(eth[2])
	print 'Hedef MAC : ' + eth_addr(packet[0:6]) + ' Kaynak MAC : ' + eth_addr(packet[6:12]) + ' Protokol : ' + str(eth_protocol)

	# IP paketini ayristirir
	if eth_protocol == 8 :
		#Ilk 20 karakter IP basligi
		ip_header = packet[eth_length:20+eth_length]
		
		#unpack
		iph = unpack('!BBHHHBBH4s4s' , ip_header)

		version_ihl = iph[0]
		version = version_ihl >> 4
		ihl = version_ihl & 0xF

		iph_length = ihl * 4

		ttl = iph[5]
		protocol = iph[6]
		s_addr = socket.inet_ntoa(iph[8]);
		d_addr = socket.inet_ntoa(iph[9]);

		print 'Versyon : ' + str(version) + ' IP Bas. Uz. : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protokol : ' + str(protocol) + ' Kaynak Adres : ' + str(s_addr) + ' Hedef Adres : ' + str(d_addr)

		#TCP protokol
		if protocol == 6 :
			t = iph_length + eth_length
			tcp_header = packet[t:t+20]

			#unpack
			tcph = unpack('!HHLLBBHHH' , tcp_header)
			
			source_port = tcph[0]
			dest_port = tcph[1]
			sequence = tcph[2]
			acknowledgement = tcph[3]
			doff_reserved = tcph[4]
			tcph_length = doff_reserved >> 4
			
			print 'Kaynak Port : ' + str(source_port) + ' Hedef Port : ' + str(dest_port) + ' SN : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP Bas. Uz. : ' + str(tcph_length)
			
			h_size = eth_length + iph_length + tcph_length * 4
			data_size = len(packet) - h_size
			
			#Kalan kisim veri
			data = packet[h_size:]
			
			print 'Data : ' + data

		#ICMP paketi
		elif protocol == 1 :
			u = iph_length + eth_length
			icmph_length = 4
			icmp_header = packet[u:u+4]

			#unpack
			icmph = unpack('!BBH' , icmp_header)
			
			icmp_type = icmph[0]
			code = icmph[1]
			checksum = icmph[2]
			
			print 'Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' + str(checksum)
			
			h_size = eth_length + iph_length + icmph_length
			data_size = len(packet) - h_size
			
			#Kalan kisim veri
			data = packet[h_size:]
			
			print 'Data : ' + data

		#UDP paketi
		elif protocol == 17 :
			u = iph_length + eth_length
			udph_length = 8
			udp_header = packet[u:u+8]

			#unpack
			udph = unpack('!HHHH' , udp_header)
			
			source_port = udph[0]
			dest_port = udph[1]
			length = udph[2]
			checksum = udph[3]
			
			print 'Kaynak Port : ' + str(source_port) + ' Hedef Port : ' + str(dest_port) + ' Length : ' + str(length) + ' Checksum : ' + str(checksum)
			
			h_size = eth_length + iph_length + udph_length
			data_size = len(packet) - h_size
			
			#Kalan kisim veri
			data = packet[h_size:]
			
			print 'Data : ' + data

		#Diger IP paketleri
		else :
			print 'Gelen Protokol TCP/UDP/ICMP degil, islem yapilamiyor.'
			
		print
