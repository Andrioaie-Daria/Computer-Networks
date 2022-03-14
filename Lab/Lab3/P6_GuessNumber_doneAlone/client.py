# 6.   The server chooses a random integer number.
# Each client generates a random integer number and send it to the server.
# The server answers with the message “larger” if the client has sent a
# smaller number than the server’s choice, or with message “smaller”
# if the client has send a larger number than the server’s choice.
# Each client continues generating a different random number
# (larger or smaller than the previous) according to the server’s indication.
# When a client guesses the server choice – the server sends back to
# the winner the message “You win – within x tries”. It also sends back to all
# other clients the message “You lost – after y retries!”
# (x and y are the number of tries of each respective client).
# The server closes all connections upon a win and it chooses a
# different random integer for the next game (set of clients)

import struct, socket, random


def main():
    try:
        server = socket.create_connection(('localhost', 1234))
    except socket.error as message:
        print(message)
        exit(-1)

    finished = False
    start_random = 1
    end_random = 2**17 -1
    random.seed()

    welcoming_message = server.recv(1024)
    print(welcoming_message.decode('ascii'))
    steps_taken = 0

    while not finished:
        my_number = random.randint(start_random, end_random)
        try:
            server.sendall(struct.pack('!I', my_number))
            answer = server.recv(30)
        except socket.error as message:
            print(message)
            server.close()
            exit(-2)

        answer = answer.decode('ascii')

        print("Sent " + my_number.__str__())
        print("Answer ", answer)

        if answer == 'larger':
            start_random = my_number
        elif answer == 'smaller':
            end_random = my_number
        else:
            finished = True

    server.close()

main()
