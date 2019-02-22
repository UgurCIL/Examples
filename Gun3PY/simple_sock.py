import socket

target_host = "www.google.com"
target_port = 80

# socket objesi oluşturuluyor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# istemci bağlanıyor
client.connect((target_host,target_port))

# veri transferi gerçekleştiriliyor
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# veri alınıyor
response = client.recv(4096)

print response
