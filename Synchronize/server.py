import socket, time
import pickle
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
data = {}
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    # msg = raw_input("enter plaintext:")
    data['orignal'] = time.ctime()
    c.send(pickle.dumps(data))
