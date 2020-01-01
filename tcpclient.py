import socket
s=socket.socket()
print('socket created')

port=1127
s.connect(('127.0.0.1',port))

print(s.recv(1024))

