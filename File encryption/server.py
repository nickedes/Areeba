import socket

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
        l = c.recv(1024)
        if l:
            f.write(l)
        else:
            f.close()
            break
    print 'Done Receiving.'
    c.close()
