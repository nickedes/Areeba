import socket
import string

key = 43
alphas = string.ascii_lowercase


def encrypt(plain_text):
    # Encrypts the file contents by simple substitution.
    plain_text = plain_text.lower()
    encrypted = ""
    for plain in plain_text:
        if plain is ' ':
            encrypted += '*'
        else:
            encrypted += alphas[(alphas.index(plain) + key) % 26]
    return encrypted

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.connect((host, port))
f = open('test/test.txt', 'rb')
l = f.read(1024)

while (l):
    # Send file.
    encrypted = encrypt(l)
    s.send(encrypted)
    l = f.read(1024)
f.close()
s.close()
