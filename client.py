#!/usr/bin/python

import socket, fcntl, os, sys

hote = sys.argv[2]
port = sys.argv[3]

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)

f = open(sys.argv[1], "rw")

## TODO add the good ioctl
fcntl.ioctl(f, termios.NBD_SET_SIZE, 134217728)
fcntl.ioctl(f, termios.NBD_CLEAR_SOCK)
fcntl.ioctl(f, termios.NBD_SET_SOCK, socket)
fcntl.ioctl(f, termios.NBD_DO_IT)
