import socket
import struct
import sys
import threading
import time
import re
import datetime

port=1235
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
client_socket.bind(("0.0.0.0", port))   # because we cannot bind to a broadcast address
broadcast_address = sys.argv[1]

peers = []

def time_query_worker(sock):
    while True:
        time.sleep(3)
        message = "TIMEQUERY"
        print("Sending time query\n")
        sock.sendto(message.encode(), (broadcast_address, port))

def date_query_worker(sock):
    while True:
        time.sleep(10)
        message = "DATEQUERY"
        print("Sending date query")
        sock.sendto(message.encode(), (broadcast_address, port))

def process_request(sock):
    while True:
        message, address = sock.recvfrom(32)
        print(peers)
        message = message.decode()
        if message == "TIMEQUERY":
            current_time = "TIME " + time.strftime("%H:%M:%S")
            sock.sendto(current_time.encode(), address)
        elif message == "DATEQUERY":
            current_date = "DATE " + str(datetime.date.today())
            sock.sendto(current_date.encode(), address)

        elif re.search("TIME [0-9][0-9]:[0-9][0-9]:[0-9][0-9]", message):
            peers.append(address)
            print("Got time " + message)

        elif re.search("DATE [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", message):
            peers.append(address)
            print("Got date " + message)
        else:
            print("Malformed ", message)


if __name__ == '__main__':
    tq_thread = threading.Thread(target=time_query_worker, args=(client_socket,))
    dq_thread = threading.Thread(target=date_query_worker, args=(client_socket,))
    pr_thread = threading.Thread(target=process_request, args=(client_socket,))

    tq_thread.start()
    dq_thread.start()
    pr_thread.start()

    tq_thread.join()
    dq_thread.join()
    pr_thread.join()