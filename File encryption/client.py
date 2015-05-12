import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
f = open('test/test.txt', 'rb')
l = f.read(1024)
print l
while (l):
    # Send file.
    # TODO:Encrypt this.
    s.send(l)
    l = f.read(1024)
    print l
f.close()
s.close()
