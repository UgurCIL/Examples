from threading import Thread
from Queue import Queue
from time import time
import requests

queue = Queue()

siteler = ('http://www.python.org',
           'http://www.metu.edu.tr',
           'http://www.udemy.com',
           'http://github.com',
           'http://www.coursera.com',
           'http://www.geeksforgeeks.org',
           'http://pypi.org')

def getSite(queue):
   while True:
      site = queue.get()
      req = requests.get(site)
      print req.url, req.status_code
      req.close()
      queue.task_done()

if __name__ == '__main__':
   basla = time()
   for i in range(5):
      t = Thread(target = getSite, args = (queue,))
      t.daemon = True
      t.start()

   for site in siteler:
      queue.put(site)

   queue.join()
   print 'Gecen sure: %f' % (time() - basla)
