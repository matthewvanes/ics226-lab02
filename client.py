#!/usr/bin/python3

import socket
import sys
from server_functions import *

def sendFileHeader(current_socket, file_header):
    f = file_header.encode('utf-8')
    type(f)
    current_socket.sendall(f + b'\n')

def recvFileHeader(current_socket):
    buffer = b''
    while True:
        data = current_socket.recv(1)
        if data == b'\n':
            return buffer.decode('utf-8')
        buffer = buffer + data

def writeToClient(file_name, file_data):
    file_object = open(file_name, "w")
    file_object.write(file_data)
    file_object.close()
    print(file_name + " successfully saved!")

BUF_SIZE = 1024
HOST = '127.0.0.1'
PORT = 12345

# Check if filename is provided.
if len(sys.argv) != 2:
    print(sys.argv[0] + ': Please provide a filename ')
    sys.exit()


# Initiate TCP Handshake
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP socket
sock.connect((HOST, PORT))                                  # Initiates 3-way handshake
print('Client: ', sock.getsockname())                       # Source IP and source port

# Send filename to server
file_name = sys.argv[1]
sendFileHeader(sock, file_name)

# Receive file_length from file server
file_length = recvFileHeader(sock)

# Test block: Print file_length received from server.
# print(file_length)
# print(type(file_length))

# Receive file from server
file_data = recvFileHeader(sock)
print(file_data)

# Write file to client.
writeToClient(file_name, file_data)

# Terminate connection to file_server
sock.close()


# consider creating sendFileHeader() function for length and filename
# and using a sendFile() and recvFile() for transmitting the whole file.


# handle when client sends a forward / as part of the filename.