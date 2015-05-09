import socket
import pickle
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

print pickle.loads(s.recv(1024))
