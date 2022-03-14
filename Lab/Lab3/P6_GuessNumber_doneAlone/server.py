import random
import socket
import struct
import threading
import time

start = 1
stop = 2 ** 17 - 1
server_number = random.randint(start, stop)
threads = []
client_count = 0
winner_thread = 0
triesOfClients = {}
lock = threading.Lock()
event = threading.Event()
event.clear()
client_guessed = False
barrier = threading.Barrier(3)


def worker(client_s):
    global lock, client_count, threads, triesOfClients, server_number, client_guessed, winner_thread

    #barrier.wait()
    thread_id = threading.get_ident()
    print("Client #", thread_id)
    triesOfClients[thread_id]=0

    client_name = client_s.getpeername()[0]
    error_message = 'Hello client #' + client_name + ' ! You are entering the number guess competion now !'
    client_socket.sendall(bytes(error_message, 'ascii'))
    while not client_guessed:
        try:
            client_number = client_s.recv(4)
            client_number = struct.unpack('!I', client_number)[0]
            triesOfClients[thread_id] += 1
            if client_number > server_number:
                client_socket.sendall(b'smaller')
            if client_number < server_number:
                client_socket.sendall(b'larger')
            if client_number == server_number:
                lock.acquire()
                client_guessed = True
                winner_thread = thread_id
                lock.release()
        except socket.error as error_message:
            print('Error:', error_message.strerror)
            break

    if client_guessed:
        if thread_id == winner_thread:
            win_message = bytes('You won within ' + str(triesOfClients[thread_id]) + ' tries.', 'ascii')
            client_socket.sendall(win_message)
            print('We have a winner', client_socket.getpeername())
            print("Thread ", thread_id, " winner")
            event.set()
        else:
            lost_message = bytes('You lost after ' + str(triesOfClients[thread_id]) + ' tries.', 'ascii')
            client_socket.sendall(lost_message)
            print("Thread ", thread_id, " looser")
    time.sleep(1)
    client_socket.close()
    print("Worker Thread ", thread_id, " end")



def resetServer():
    global lock, client_count, threads, triesOfClients, server_number, client_guessed, winner_thread
    while True:
        event.wait()
        for thread in threads:
            thread.join()
        event.clear()
        lock.acquire()
        threads = []
        client_guessed = False
        client_count = 0
        server_number = random.randint(start, stop)
        print("Server number: ", server_number)
        lock.release()


if __name__ == '__main__':
    try:
        welcoming_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        welcoming_socket.bind(('0.0.0.0', 1234))
        welcoming_socket.listen(10)
        print('Listening fot incoming connections.\n')
    except socket.error as message:
        print(message)
        exit(-1)

    t = threading.Thread(target=resetServer, daemon=True)
    t.start()

    while True:
        client_socket, client_info = welcoming_socket.accept()

        new_thread = threading.Thread(target=worker, args=(client_socket,))
        threads.append(new_thread)
        client_count += 1
        new_thread.start()
