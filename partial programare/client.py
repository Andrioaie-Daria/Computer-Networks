import socket, struct, random,sys, time, select, threading
finished = False

def listen_to_end_message(my_udp_socket):
    global finished
    while True:
        sockets, _, _ = select.select([my_udp_socket], [], [])
        if my_udp_socket in sockets:
            message, _ = my_udp_socket.recvfrom(256)
            print(message.decode())
            print("Shutting down...")
            finished = True
            server_socket.close()
            my_udp_socket.close()
            exit(0)

if __name__ == '__main__':

    try:
        server_socket = socket.create_connection(('localhost', 1234))
    except socket.error as msg:
        print("Error: ", msg.strerror)
        exit(-1)

    my_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Do a random sent to "nowhere", to force the OS to properly allocate the port.
    my_udp_socket.sendto(b'random', ('8.8.8.8', 2355))

    _, my_udp_port = my_udp_socket.getsockname()

    print("My UDP port is:", str(my_udp_port))
    server_socket.send(struct.pack("!I", my_udp_port))
    number_of_digits = struct.unpack("!I", server_socket.recv(4))[0]


    threading.Thread(target=listen_to_end_message, daemon=True, args=(my_udp_socket,)).start()

    while not finished:
        random.seed()
        my_number = random.randint(0, 9)
        try:
            server_socket.sendall(struct.pack("!I", my_number))
            list_length = struct.unpack("!I", server_socket.recv(4))[0]
            positions = []
            for _ in range(list_length):
                new_pos = struct.unpack("!I", server_socket.recv(4))[0]
                positions.append(new_pos)

            if list_length == 0:
                print("The digit " + str(my_number) + " is not in the number")
            else:
                print("The digit " + str(my_number) + " is on positions " + str(positions))

        except socket.error as msg:
            print('Error: ', msg.strerror)
            server_socket.close()
            exit(-2)

        N = random.randint(1, 3)
        time.sleep(N)
