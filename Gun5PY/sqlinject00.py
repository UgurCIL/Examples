import requests
import sys

url = raw_input('Site adresini gitiniz: ')

req = requests.get(url + '=1\' or 1 == 1')
data = req.text

if 'You have an error in your SQL syntax' in data:
    print 'Syfada SQLi zafiyeti mevcut'
else:
    print 'Sayfa temiz..'
