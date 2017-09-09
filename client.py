import socket, select, sys


# ENCRYPT BLOWFISH
def encrypt(msg):
  bs = Blowfish.block_size
  key = "An arbitrarily long key"
  iv = Random.new().read(bs)
  cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
  plaintext = msg
  plen = bs - divmod(len(plaintext),bs)[1]
  padding = [plen]*plen
  padding = pack('b'*plen, *padding)
  return iv + cipher.encrypt(plaintext + padding)

# SOCKET
TCP_IP = '127.0.0.1'
TCP_PORT = 62

BUFFER_SIZE = 1024
MESSAGE = "Hello, Server. Are you ready?\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, 5000))
s.send(MESSAGE)
socket_list = [sys.stdin, s]

while 1:
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])


    for sock in read_sockets:
        # incoming message from remote server
        if sock == s:
            data = sock.recv(4096)
            if not data:
                print('\nDisconnected from server')
                sys.exit()
            else:
                sys.stdout.write("\n")
                message = data.decode()
                sys.stdout.write(message)
                sys.stdout.write('<Me> ')
                sys.stdout.flush()

        else:
            msg = sys.stdin.readline()
            s.send(bytes(msg))
            sys.stdout.write('<Me> ')
            sys.stdout.flush()
