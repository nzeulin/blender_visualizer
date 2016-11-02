#!/usr/bin/env python

import socket
import pickle
import sys

port = 7777
host = ''

list = {"node1":(5, 0, 0)}
sock = socket.socket()

def create_connection(sock, host, port):
    try:
        sock.bind((host, port))
        sock.listen(1)
        print("Listening port: " + str(port))
    except socket.error as err:
        print("Error: {0}".format(err))
        close_sock(sock)
    except socket.timeout as err:
        print("Timeout: {0}".format(err))

def close_sock(sock):
    print("Connection closed")
    sock.shutdown(0)
    sock.close()

create_connection(sock, host, port)

conn, addr = sock.accept()

print('Connected:' + str(addr))

while True:
    command = conn.recv(1024)
    command = bytes.decode(command)
    print ("Command: " + command)
    if not command:
        close_sock(conn)
        sock.listen(1)
        print("Listening port: " + str(port))
        conn, addr = sock.accept()
        print('Connected:' + str(addr))
        continue
    if (command == "send_list"):
    	pickled_list = pickle.dumps(list)
    	conn.send(sys.getsizeof(pickled_list))
    	conn.send(pickled_list)