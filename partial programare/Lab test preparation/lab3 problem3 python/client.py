import select
import socket
import struct
import sys
import threading

def receive_messages():
    # listen for incoming messages from the server and other clients
    try:
        while True:
            sockets, _, _ = select.select([my_udp_socket, server_communication_socket], [], [])
            if server_communication_socket in sockets:
                operation = server_communication_socket.recv(1)
                client_ip = socket.inet_ntoa(server_communication_socket.recv(4))
                _port = struct.unpack("!H", server_communication_socket.recv(2))[0]

                if operation == b'L':
                    print("Client "+ client_ip + ":" + str(_port) + " left the chatroom.")
                    other_clients.remove((ip_address, _port))

                elif operation == b'N':
                    print("Client " + client_ip + ":" + str(_port) + " joined the chatroom.")
                    other_clients.add((client_ip, _port))
                else:
                    print("Unknown operation received from server")

            if my_udp_socket in sockets:
                message, address = my_udp_socket.recvfrom(256)
                print("Client", address[0] + ":" + str(address[1]), "-", message.decode())
    except OSError as osError:
        server_communication_socket.close()
        my_udp_socket.close()
        print("OSError:", osError.strerror)
        print("Type 'Q' to quit:")

if __name__ == "__main__":
    ip_address = sys.argv[1]
    port = int(sys.argv[2])
    server_communication_socket = socket.socket()
    server_communication_socket.connect((ip_address, port))

    # receive the list of connected clients and store them in a set
    other_clients = set()
    number_of_clients = struct.unpack("!I", server_communication_socket.recv(4))[0]

    for _ in range(number_of_clients):
        client_address = socket.inet_ntoa(server_communication_socket.recv(4))
        client_port = struct.unpack("!H", server_communication_socket.recv(2))[0]
        other_clients.add((client_address, client_port))

    # create a udp socket to communicate with the others
    my_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Do a random sent to "nowhere", to force the OS to properly allocate the port.
    my_udp_socket.sendto(b'random', ('8.8.8.8', 2355))

    # Now we can get the port associated to this socket and send it to the server
    # which will then send it to all other clients
    _, my_udp_port = my_udp_socket.getsockname()
    print("My UDP port is:", str(my_udp_port))
    server_communication_socket.send(struct.pack("!H", my_udp_port))

    threading.Thread(target=receive_messages, daemon=True).start()

    while True:
        user_input = input()
        if user_input == "Q":
            # tell the server we are leaving
            server_communication_socket.send(b'L')
            print("Leaving the chat room and shutting down")
            my_udp_socket.close()
            server_communication_socket.close()
            exit(0)
        for other_client in other_clients:
            my_udp_socket.sendto(user_input.encode(), other_client)