import requests
from time import time

siteler = ('http://www.python.org',
           'http://www.metu.edu.tr',
           'http://www.udemy.com',
           'http://github.com',
           'http://www.coursera.com',
           'http://www.geeksforgeeks.org',
           'http://pypi.org')

start = time()

for site in siteler:
   req = requests.get(site)
   print req.url, req.status_code
   req.close()

print 'Gecen sure: %f' % (time() - start)
