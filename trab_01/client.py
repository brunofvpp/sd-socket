# -*- coding: utf-8 -*-
import socket, select, sys
from helpers import encrypt

msg = sys.argv[1]
# SOCKET
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 5005))
sock.sendall(encrypt(msg))
data = sock.recv(1024)
if msg == data:
  print "O servidor retornou com a mensagem correta. =D : ", msg
  sys.exit()
print "O servidor não conseguiu desencriptar a mensagem. =( : ", msg
