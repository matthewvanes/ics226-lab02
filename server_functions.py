#!/usr/bin/python3


def recvFilename(current_socket):
    buffer = b''
    while True:
        data = current_socket.recv(1)
        if data == b'\n':
            return buffer.decode('utf-8')
        buffer = buffer + data

def getFileLength(file_name):
    f = len(file_name)
    file_length = str(f)
    return file_length

def getFile(file_name):
    print("./server_data/" + file_name)
    try:
        f = open("./server_data/" + file_name, "r")
        file_data = f.read()
        f.close()
        return file_data
    except:
        print("Exception: File not found")

def sendFileLength(current_socket, file_length):
    f = file_length.encoded('utf')
    current_socket.sendall(file_length)

def sendFile(current_socket, file_name):
    f = file_name.encode('utf-8')
    current_socket.sendall(f)