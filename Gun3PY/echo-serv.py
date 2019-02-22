#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"
PORT = 4444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
   sock.bind((HOST, PORT))
   sock.listen()
   conn, addr = sock.accept()
   with conn:
      print("Baglandi: ", addr)
      while True:
         data = conn.recv(1024)
         if not data:
            break
         conn.sendall(data)
