import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

# Connecting to server.
s.connect((host, port))

para = s.recv(1024)

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for char in para:
    if char in vowels:
        vowels[char] = vowels[char] + 1

print vowels
