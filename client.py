#!/usr/bin/python
from socket import *

client = socket(AF_INET,SOCK_STREAM)            # select socket type
client.connect(("ip",port))                     # connect to the server

while True:
    client.sendall(raw_input(""))                    # send the command to the server
    print client.recv(4096)                         # receive the data from the server

client.close()                                  # you need to close the socket, but!! you are the client so who cares...
