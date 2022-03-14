# Implement a server application that generates a random integer P and
# communicates to the clients the number of digits of that number – when the client connects.
#
# Implement a client application that receives from a server the number of digits of P.
#
# The client generates a random digit every N seconds and sends the digit to the server.
# The server answers with the positions where the digit is found on the server’s number.
#
# Spawn multiple clients. The server will announce all clients when it has a winner using UDP.
# You should design a method for the server to infer the IP and port where is should
# communicate with each peer over UDP.
#
# Note: For extra points implement the client and the server in two different languages.

import socket
import threading
import random
import struct
import sys
import time

random.seed()
start = 1
stop = 2 ** 17 - 1
server_number = random.randint(start, stop)
my_lock = threading.Lock()
event = threading.Event()
event.clear()
client_count=0
threads=[]
winner_thread = 0
client_guessed = False
number_of_digits = 0

def worker(client_socket, client_info):
    client_udp_port = struct.unpack("!I", client_socket.recv(4))[0]
    print("New client from " + client_info[0] + ":" + str(client_info[1]) + " with udp port "+ str(client_udp_port))

    global my_lock, client_guessed, winner_thread, server_number, threads, event, client_count

    guessed_positions = {}
    for pos in range(number_of_digits):
        guessed_positions[pos] = False


    client_socket.sendall(struct.pack("!I", number_of_digits))

    while not client_guessed:
        try:
            # receive the number
            client_number = client_socket.recv(4)
            client_number = struct.unpack("!I", client_number)[0]

            print(client_info[0] + ":" + str(client_info[1]) + "  -->  " + str(client_number))


            positions = []
            # find the positions of the digit in the server number
            number_as_string = str(server_number)
            for position in range(number_of_digits):
                if int(number_as_string[position]) == client_number:
                    positions.append(position)
                    guessed_positions[position] = True

            # send the positions
            list_length = len(positions)
            client_socket.send(struct.pack("!I", list_length))
            for position in positions:
                client_socket.send(struct.pack("!I", position))



            # see if it won
            i_won = True
            for pos in range(number_of_digits):
                if guessed_positions[pos] == False:
                    i_won = False

            if i_won:
                my_lock.acquire()
                client_guessed = True
                winner_thread = threading.get_ident()
                my_lock.release()

        except socket.error as message:
            print('Error:', message.strerror)
            break

    if client_guessed:
        #print("Client " + client_info[0] + ":" + str(client_info[1]) + " won")
        # announce the others
        if winner_thread == threading.get_ident():
            winner_message = "You are the winner"
            winner_message = winner_message.encode()
            server_udp_socket.sendto(winner_message, (client_info[0], client_udp_port))
            event.set()
        else:
            loser_message = "You lost!"
            loser_message = loser_message.encode()
            server_udp_socket.sendto(loser_message, (client_info[0], client_udp_port))

    client_socket.close()

def reset_server():
    global my_lock, client_guessed, winner_thread, server_number, threads, event, client_count
    while True:
        event.wait()
        for thread in threads:
            thread.join()
        print("all threads are finished now")

        event.clear()
        my_lock.acquire()
        server_number = random.randint(start, stop)
        number_of_digits = len(str(server_number))
        print('Server number: ', server_number)
        my_lock.release()


if __name__ == '__main__':
    try:
        welcoming_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        welcoming_socket.bind(('0.0.0.0', 1234))
        welcoming_socket.listen(5)
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    server_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    new_thread = threading.Thread(target=reset_server, daemon=True)   # daemon threads run in the background
    new_thread.start()

    server_number = random.randint(100, 999)
    number_of_digits = len(str(server_number))
    print('Server number: ', server_number)

    while True:
        client_socket, client_info = welcoming_socket.accept()
        new_thread = threading.Thread(target=worker, args=(client_socket, client_info,))
        threads.append(new_thread)
        client_count += 1
        new_thread.start()