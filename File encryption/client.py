import socket 

s = socket.socket()
host = socket.gethostname()
port = 12345 
s.connect((host, port))
f = open('test_recv.txt','wb')
l = c.recv(1024)
    while (l):
        print "Receiving..."
        f.write(l)
        l = c.recv(1024)
    f.close()
print s.recv(1024)