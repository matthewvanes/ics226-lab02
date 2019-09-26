#!/usr/bin/python3

import sys
import socket
from server_functions import recvFilename, getFile, getFileLength, sendEntireFile

HOST = ''
PORT = 12345

# Establish TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            # TCP socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)          # More on this later...
sock.bind((HOST, PORT))                                             # Claim messages sent to port "PORT"

while True:

    sock.listen(1)                                                  # Enable server to receive 1 connection at a time
    print('Server: ', sock.getsockname(), '\n')                     # Prints server port and IP
    print("Awaiting incoming connection: \n")
    sc, sockname = sock.accept()                                    # Wait until a connection is established
    print('Client: ', sc.getpeername(), '\n')                       # Prints current client connection

    # Get filename from client.
    file_name = b''
    file_name = recvFilename(sc)
    print(file_name + " <File name received!>\n")

    # Open file
    file_data = getFile(file_name)
    # Get file length from opened file.
    file_length = getFileLength(file_data)

    # Send file length to client
    file_length_to_server = file_length.encode('utf-8')
    sc.sendall(file_length_to_server + b'\n')

    # Send file to client
    sendEntireFile(sc, file_data)

    # Close connection
    sc.close()