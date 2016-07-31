#!/usr/bin/python

from functions import *

project_name()
# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

host = "lev-pc"
port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

clientsocket,addr = serversocket.accept()
while True:
    choice = menu()
    if choice == "1":
        clientlist = []
        if addr not in clientlist:
            clientlist.append(addr)
            print clientlist
        back2menu = raw_input("Back To Main Menu? >> y/n")
        if back2menu == "y":
            menu()
        elif back2menu == type(int):
            print "please choose y or n !!!"
        else:
            print "goodbuy!"
            clientsocket.close()
            break
    elif choice == "2":
        print 2
    elif choice == "3":
        print 3
    elif choice == "4":
        print 4
    elif choice == "5":
        print 5
    else:
        print "What about a bit of thinking?????"

clientsocket.close()
serversocket.close()
