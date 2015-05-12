import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
f.open('test.txt','wb')
s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    # Send file.
    print 'Sending...'
    l = f.read(1024)
    while l:
    	print 'Sending..'
    	c.send(l)
    	l = f.read(1024)
    f.close()
    print 'Done Sending.'
