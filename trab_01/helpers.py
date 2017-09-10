from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack

KEY = "&*%7e7oq%=r^o)z_kqc^(n63340va$xkn8zx^=)k(zn$#zod+7"

# DECRYPT BLOWFISH
def decrypt(msg):
  bs = Blowfish.block_size
  ciphertext = msg
  iv = ciphertext[:bs]
  ciphertext = ciphertext[bs:]

  cipher = Blowfish.new(KEY, Blowfish.MODE_CBC, iv)
  msg = cipher.decrypt(ciphertext)

  last_byte = msg[-1]
  msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
  return (repr(msg))


# ENCRYPT BLOWFISH
def encrypt(msg):
  bs = Blowfish.block_size
  iv = Random.new().read(bs)
  cipher = Blowfish.new(KEY, Blowfish.MODE_CBC, iv)
  plaintext = msg
  plen = bs - divmod(len(plaintext),bs)[1]
  padding = [plen]*plen
  padding = pack('b'*plen, *padding)
  return iv + cipher.encrypt(plaintext + padding)
