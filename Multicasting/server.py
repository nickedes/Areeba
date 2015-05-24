import socket
from thread import start_new_thread


def client_work(conn, paragraph):
    conn.send(paragraph)

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

para = raw_input("Enter text:")

while True:
    c, addr = s.accept()
    start_new_thread(client_work, (c, para))
