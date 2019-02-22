#!/usr/bin/env python3

import socket

HOST = "127.0.0.1" # Baglanilacak adres
PORT = 4444  # Baglanilacak port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
   sock.connect((HOST, PORT))
   sock.sendall(b"Selamlar..")
   data = sock.recv(1024)

print("Received", repr(data))
