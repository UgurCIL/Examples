from time import sleep
from threading import Thread

def tekrarla(yazi, sure, sayi):
   try:
      while sayi > 0:
         print yazi,
         sleep(sure)
         sayi -= 1
   except KeyboardInterrupt:
      print 'Cikiyor..'
      sys.exit()

if __name__ == '__main__':
   an = Thread(target = tekrarla, args = ("\nan",1, 6))
   ka = Thread(target = tekrarla, args = ("ka",0.5, 6))
   ra = Thread(target = tekrarla, args = ("ra\n",3, 6))

   an.start()
   ka.start()
   ra.start()
