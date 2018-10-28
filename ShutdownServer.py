#!/usr/bin/env python
import socket
from thread import *

shutdownServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
shutdownServer.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

IP_address = '0.0.0.0'
Port = 2004

shutdownServer.bind((IP_address,Port))

shutdownServer.listen(500)

list_of_nodes = []

acc = ['gedit','shutdown','firefox']

def nodethread(conn, addr):


	while True:
			try:
				command = conn.recv(2048)
				if command:
					if addr[0] == '127.0.0.1' or addr[0] == '172.16.54.254':
						for x in acc:
							if x in command:
								print "[+] " + addr[0] + " " + command
								broadcast(command, conn)

				else:
					remove(conn)

			except:
				continue

def broadcast(command, connection):
	for clients in list_of_nodes:
		if clients!=connection:
			try:
				clients.send(command)
			except:
				clients.close()

				remove(clients)

def remove(connection):
	if connection in list_of_nodes:
		list_of_nodes.remove(connection)

while True:

	conn, addr = shutdownServer.accept()

	list_of_nodes.append(conn)

	print "[+] Node " + addr[0] +  " Connected"

	start_new_thread(nodethread,(conn,addr))

conn.close()
server.close()
