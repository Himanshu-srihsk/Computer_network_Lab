import socket
s=socket.socket()
print('socket created')

port=1127
s.bind(('',port))

s.listen(5)
while True:
  c,addr=s.accept()
  c.sendall("thnks for conn")
  c.close()
   

