import select, socket, sys
from Crypto.Cipher import Blowfish
from struct import pack
from threading import Thread


# DECRYPT BLOWFISH
def decrypt(msg):
  bs = Blowfish.block_size
  key = "An arbitrarily long key"
  ciphertext = msg
  iv = ciphertext[:bs]
  ciphertext = ciphertext[bs:]

  cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
  msg = cipher.decrypt(ciphertext)

  last_byte = msg[-1]
  msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
  return (repr(msg))


class ClientThread(Thread):

  def __init__(self,ip,port):
    Thread.__init__(self)
    self.ip = ip
    self.port = port
    print "[+] New thread started for "+ip+":"+str(port)


  def run(self):
    while True:
        data = conn.recv(2048)
        if not data: break
        print "received data:", data
        conn.send("<Server> Got your data. Send some more\n")

TCP_IP = '127.0.0.1'
TCP_PORT = 62
BUFFER_SIZE = 1024  # Normally 1024
threads = []

# SOCKET
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("127.0.0.1", 5000))
sock.listen(10)

read_sockets, write_sockets, error_sockets = select.select([sock], [], [])


while True:
  print "Waiting for incoming connections..."
  for sock in read_sockets:
      (conn, DESTINATION) = sock.accept()
      newthread = ClientThread("127.0.0.1", 5000)
      newthread.start()
      threads.append(newthread)

for t in threads:
    t.join()

# try:
#   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   sock.bind(DESTINATION)
#   print "socket bind complete"
# except:
#   print "Algo de errado nao esta certo"
#   sys.exit()

# while True:  
#   msg, addr = sock.recvfrom(1024)
#   print "received message:", decrypt(msg)
#   print "received message:", addr
