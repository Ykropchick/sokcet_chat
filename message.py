# -*- coding: utf-8 -*-
import sys
import socket




s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0',11719))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

name = input()
msg = input()


def sendproc():
	sock.sendto((name+':'+msg).encode(),('255.255.255.255',11719))




while 1:
	name = input('Hick:')
	msg = input('Message:')
	sendproc()
