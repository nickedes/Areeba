import socket
import string

key = 43
alphas = string.ascii_lowercase

def decrypt(cipher_text):
    # Decrypts the file contents.
    decrypted = ""
    for cipher in cipher_text:
        if cipher is '*':
            decrypted += ' '
        else:
            decrypted += alphas[(alphas.index(cipher) + 26 - key) % 26]
    return decrypted

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
f = open('test/test_recv.txt', 'wb')
s.listen(5)

while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    # Receive file.
    while True:
        cipher_text = c.recv(1024)
        l = decrypt(cipher_text)
        if l:
            f.write(l)
        else:
            f.close()
            break
    print 'Done Receiving.'
    c.close()
