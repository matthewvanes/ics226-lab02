#!/usr/bin/python3

import socket
import sys
from server_functions import sendFileName, recvFileLength, writeToClient, recvEntireFile

BUF_SIZE = 1
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
sendFileName(sock, file_name)

# Receive file_length from file server
file_length = recvFileLength(sock)

# Receive file from server
file_data = recvEntireFile(sock, file_length)

# Write file to client.
writeToClient(file_name, file_data)

# Terminate connection to file_server
sock.close()