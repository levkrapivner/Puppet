#!/usr/bin/python
import time
import socket
import struct


def current_time():
    return time.strftime("%X")
current_time()


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
get_ip_address()

def get_dns():
    data = open("/etc/resolv.conf").read().split()
    for item in data:
        if len(item.split(".")) == 4:
           return item
get_dns()

def get_default_gateway():
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                continue
            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
get_default_gateway()

def project_name():
    print " "
    print "      Python Project 102 "
    print "      Name: Lev          "
    print "      Current Time:", current_time()
    print (30 * '#')

    # print my ip, resolv.conf and gatewa
    print "Segmant: ", get_ip_address()
    print "DNS:     ", get_dns()
    print "Gateway:", get_default_gateway()
    print (30 * '#')



def menu():
    print (30 * '#')
    print "             Menu"
    print (30 * '#')
    print """
    1) Show all clients
    2) Send commands to all client
    3) Transfer file to clients all clients
    4) Install something on all clients
    5) Remove something from all clients
    """
    return  raw_input('Enter your choice [1-5] : ')




