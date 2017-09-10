# -*- coding: utf-8 -*-
import select, socket
from helpers import decrypt


# SOCKET
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 5005))
sock.listen(99)

while True:
  conn, address = sock.accept()
  buf = conn.recv(4096)
  msg = decrypt(buf)[1:-1] # WORKAROUND: DURANTE O DECRYPT E ADICIONADO ASPAS NO INICIO E FIM
  print msg
  conn.send(msg)