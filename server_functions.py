#!/usr/bin/python3

#Functions for file_server.py  -----------------------------------------------------------

def recvFilename(current_socket):
    buffer = b''
    while True:
        data = current_socket.recv(1)
        if data == b'\n':
            return buffer.decode('utf-8')
        buffer = buffer + data

def getFile(file_name):
    try:
        f = open("./server_data/" + file_name, "rb")
        file_data = f.read()
        f.close()
        return file_data
    except:
        print("Exception: File not found")

def getFileLength(file_data):
    f = len(file_data)
    file_length = str(f)
    return file_length

def sendEntireFile(current_socket, file_data):
    current_socket.sendall(file_data)

# Functions for client.py -------------------------------------------------------

def sendFileName(current_socket, file_header):
    f = file_header.encode('utf-8')
    type(f)
    current_socket.sendall(f + b'\n')

def recvFileLength(current_socket):
    buffer = b''
    while True:
        data = current_socket.recv(1)
        if data == b'\n':
            file_length = int(buffer)
            return file_length
        buffer = buffer + data

def recvEntireFile(current_socket, file_length):
    buffer = b''
    data = b''
    for x in range (0, file_length):
        buffer = current_socket.recv(1)
        data = data + buffer
    return data

def writeToClient(file_name, file_data):
    file_object = open(file_name, "wb")
    file_object.write(file_data)
    file_object.close()
    print(file_name + " successfully saved!")