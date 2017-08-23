'''
Created on 20-Jun-2017

@author: BALASUBRAMANIAM
'''
#activate telnet client to test
#telnet 127.0.0.1 72 
#socket types(stream socket,datagram socket,raw sockets,sequenced packet sockets)
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 72
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
 
conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    conn.send(data)  # echo
conn.close()