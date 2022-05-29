#!/usr/bin/python

import socket, fcntl, os, sys

hote = sys.argv[2]
port = sys.argv[3]

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)

f = open(sys.argv[1], "rw")

## TODO add the good ioctl 
fcntl.ioctl(0, termios.TIOCGPGRP, buf, 1)
fcntl.ioctl(0, termios.TIOCGPGRP, buf, 1)
fcntl.ioctl(0, termios.TIOCGPGRP, buf, 1)
