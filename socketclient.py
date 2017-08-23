'''
Created on 20-Jun-2017

@author: BALASUBRAMANIAM
'''
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
BUFFER_SIZE=1000
print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
print('connecting....')

try:
    
    # Send data
    message = 'repeated.'
    print (sys.stderr, 'sending "%s"' % message)
    #sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(BUFFER_SIZE)
        amount_received += len(data)
        print (sys.stderr, 'received "%s"' % data)
finally:
      print (sys.stderr, 'closing socket')
      
      #sock.close()