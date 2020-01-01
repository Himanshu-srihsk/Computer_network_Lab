import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('socket created')
host=raw_input(str('enter host name'))
port=11237

message="hello"
s.sendto(message,(host,port))

