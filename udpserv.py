import socket
import sys
import time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
print("server start on host:",host)
port=11237

s.bind((host,port))
print("server bound success:")

while 1:
  print("waiting for client")
  data,addr=s.recvfrom(1024)
  print("messge:",data)
  
