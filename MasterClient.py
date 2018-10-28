#!/usr/bin/env python
import socket
import select
import sys
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = '127.0.0.1'
Port = 2004
acc = ['firefox','shutdown','gedit']

while True:
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((IP_address, Port))

        while True:
            print "Shell> "
            sockets_list = [sys.stdin, server]

            read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

            for socks in read_sockets:
                if socks == server:
                		raise Exception("NOT VALID")
                		continue

                else:
                    command = sys.stdin.readline()
                    server.send(command)
                    sys.stdout.flush()
    except:
        time.sleep(10)
        continue



server.close()
