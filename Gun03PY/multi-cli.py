import socket 

def Main():
	# IP ve port numarasi
	host = '127.0.0.1'
	port = 12345

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

	# server a baglan 
	s.connect((host,port)) 

	message = "Python MultiHandler Socket Programming"
	while True: 

		# mesajı server a gonder 
		s.send(message.encode('ascii')) 

		# gelen cevabi al 
		data = s.recv(1024) 

		print('Received from the server :',str(data.decode('ascii'))) 

		ans = input('\nDo you want to continue(y/n) :') 
		if ans == 'y': 
			continue
		else: 
			break
	# close the connection 
	s.close() 

if __name__ == '__main__': 
	Main() 
