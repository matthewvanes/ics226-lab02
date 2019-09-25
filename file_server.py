#!/usr/bin/python3

import sys
import socket
#from server_functions.py import recvFilename # getFileLength, getFile, sendFileLength

def recvFilename(current_socket):
    buffer = b''
    while True:
        data = current_socket.recv(1)
        if data == b'\n':
            return buffer.decode('utf-8')
        buffer = buffer + data


def getFile(file_name):
    print("./server_data/" + file_name)
    try:
        f = open("./server_data/" + file_name, "r")
        file_data = f.read()
        f.close()
        return file_data
    except:
        print("Exception: File not found")

def getFileLength(file_name):
    f = len(file_name)
    file_length = str(f)
    return file_length

def sendFile(current_socket, file_name):
    f = file_name.encode('utf-8')
    current_socket.sendall(f)


HOST = ''
PORT = 12345

# Establish TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            # TCP socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)          # More on this later...
sock.bind((HOST, PORT))                                             # Claim messages sent to port "PORT"
sock.listen(1)                                                      # Enable server to receive 1 connection at a time
print('Server: ', sock.getsockname())                               # Prints server port and IP
sc, sockname = sock.accept()                                        # Wait until a connection is established
print('Client: ', sc.getpeername())                                 # Prints current client connection

# Wait for filename from client.

file_name = b''
file_name = recvFilename(sc)
print(file_name + " <File name received!>")

# Open file
# Assign file to variable
# Assign file length to variable

file_data = getFile(file_name)
print(file_data)
file_length = getFileLength(file_data)
print(file_length)

# Send file length to client
file_length_to_server = file_length.encode('utf-8')
sc.sendall(file_length_to_server + b'\n')

# Send file to client
sendFile(sc, file_data)

# Close connection
sc.close()