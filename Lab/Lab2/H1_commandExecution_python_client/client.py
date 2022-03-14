import socket
import struct

# 1.   The client takes a string from the command line and sends it to the server.
# The server interprets the string as a command with its parameters.
# It executes the command and returns the standard output and the exit code to the client.

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.100.18", 1234))
    string = input("Enter command: ")
    bytes_string = bytes(string, 'ascii') + b'\x00'
    s.send(bytes_string)

    output = s.recv(100)
    output = output.decode("utf-8")
    while output != "over":
        print(output)
        print("\n")
        output = s.recv(100)
        output = output.decode("utf-8")

    exit_code = s.recv(4)
    exit_code = struct.unpack("!i", exit_code)
    print(exit_code)
    

main()