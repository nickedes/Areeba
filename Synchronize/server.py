import socket
import time
import pickle
import datetime as dt


def calc(start, end):
    start_dt = dt.datetime.strptime(start[11:19], '%H:%M:%S')
    end_dt = dt.datetime.strptime(end[11:19], '%H:%M:%S')
    diff = (end_dt - start_dt)
    return diff.seconds / 60

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
    data['original'] = time.ctime()
    c.send(pickle.dumps(data))
    data = pickle.loads(c.recv(1024))
    data['returned'] = time.ctime()
    print(data)
    sending_time = calc(data['receive'], data['original'])
    receiving_time = calc(data['returned'], data['transmit'])
    # Round-trip time
    rtt = sending_time + receiving_time
    time_diff = calc(data['receive'], data['original']) - rtt / 2
    c.send(pickle.dumps(time_diff))
