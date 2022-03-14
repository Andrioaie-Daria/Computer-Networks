import socket
import struct
import os

# 2.   The client sends the complete path to a file.
# The server returns back the length of the file and its content in the case the file exists.
# When the file does not exist the server returns a length of -1 and no content.
# The client will store the content in a file with the same name as the input file with the suffix –copy appended
# (ex: for f.txt => f.txt-copy).

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 1234)) # listen on every address of the server
    s.listen(10)
    print("Listening for incoming connections.\n")
    while True:
        connection_socket, client_info = s.accept()
        print("Connected client\n")
        argument_length = connection_socket.recv(4)
        argument_length = struct.unpack("!i", argument_length)

        filename = connection_socket.recv(argument_length)
        filename = filename.decode("latin-1")

        file_handle = open(filename)
        file_length = os.path.getsize(filename)

        file_length = struct.pack("!H", file_length)
        connection_socket.send(file_length)
        connection_socket.close()

main()