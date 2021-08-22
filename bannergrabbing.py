#!/usr/bin/python

import sys,socket

if len(sys.argv) <=2 :

	print ("Modo de Uso: 192.168.20.1 80")

else :
	ip = sys.argv[1]
	porta = int(sys.argv[2])
	meu_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	meu_socket.connect((ip,porta))
	banner = meu_socket.recv(1024)

	print "BANNER:",banner



