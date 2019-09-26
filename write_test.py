#!/usr/bin/python3

import sys

# Get file name from user.
file_name = sys.argv[1]
# Get file contents from user.
file_contents = sys.stdin.readline()
# Call write function and write file to current directory.
file_object = open(file_name, "w")
file_object.write(file_contents)
file_object.close()

def writeToClient(file_name, file_data):
    file_object = open(file_name, "w")
    file_object.write(file_contents)
    file_object.close()