import nmap

nm = nmap.PortScanner()
nm.scan("10.10.1.1", "1-1000", arguments='--script bannser.nse')

print "-" * 30
print "[+] Komut: " + str(nm.command_line())	#ekrana calisan komutu basar

for host in nm.all_hosts():			#tarama sonucu donen tum IP adreslerinin uzerinden gecer
   if nm[host].state() == "up":			#host aktif mi
      print "[+] Host Aktif: " + str(host)
      for proto in nm[host].all_protocols():	#host ustundeki tum protokollerin uzerinden gecer
         print "Protokol: " + str(proto)
         portlar = nm[host][proto].keys()	#host-protokol ustundeki tum portlarin uzerinden gecer
            for port in portlar:
               print "Port: {}\t Durumu: {}".format(port, nm[host][proto][port]["state"])

      #######################################################
      # NSE scriptlerinin sonuclarini burada duzenlemeli ve #
      # kullanici icin anlamlı hale getirmeliyiz            #
      #######################################################
   else:
      print "[-] Host Down: " + str(host)
