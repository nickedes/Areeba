import socket
import time
import pickle
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

while True:
    data = pickle.loads(s.recv(1024))
    data['receive'] = time.ctime()
    time.sleep(10)
    data['transmit'] = time.ctime()
    s.send(pickle.dumps(data))
    time_diff = pickle.loads(s.recv(1024))
    print "Time difference between Server and Client clocks:", time_diff
