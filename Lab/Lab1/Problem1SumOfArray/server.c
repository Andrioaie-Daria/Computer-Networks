#include <stdio.h>
#include <WinSock2.h>
#include "stdint.h"

#pragma clang diagnostic push
#pragma ide diagnostic ignored "EndlessLoop"
int main() {
    SOCKET s;
    struct sockaddr_in server, client;
    int c, l, err;

#ifdef WIN32
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) < 0) {
        printf("Error initializing the Windows Sockets LIbrary");
        return -1;
    }

#endif

    // create a welcoming socket
    s = socket(AF_INET, SOCK_STREAM, 0);
    if(s<0){
        printf("Error on creating server socket");
        return 1;
    }

    memset(&server, 0, sizeof(server));
    server.sin_port = htons(1234);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;

    if(bind(s, (struct sockaddr*) &server, sizeof(server)) <0 ){
        perror("Bind error: ");
        return 1;
    }

    listen(s, 5);
    l = sizeof(client);
    memset(&client, 0, sizeof(client));

    while(1){
        uint16_t sum = 0, length, currentNumber;
        printf("Listening for incoming connections\n");
        c = accept(s, (struct sockaddr *) &client, &l);

        err = errno;
#ifdef WIN32
        err = WSAGetLastError();
#endif
        if (c < 0) {
            printf("accept error: %d", err);
            continue;
        }

        printf("Incomming connected client from: %s:%d\n", inet_ntoa(client.sin_addr), ntohs(client.sin_port));

        // serving the connected client
        int result = recv(c, (char*)&length, sizeof(length), 0);
        //check we got an unsigned short value
        if (result != sizeof(length)) printf("Error receiving array length\n");
        length = ntohs(length);

        for(int i=0; i<length; i++){
            // serving the connected client
            result = recv(c, (char*)&currentNumber, sizeof(currentNumber), 0);
            //check we got an unsigned short value
            if (result != sizeof(currentNumber))
                printf("Error receiving array element\n");
            else{
                currentNumber = ntohs(currentNumber);
                sum += currentNumber;
            }
        }
        sum = htons(sum);
        result = send(c, (char*)&sum, sizeof(sum), 0);
        if(result != sizeof(sum)){
            printf("Error sending result\n");
        }
        closesocket(c);
    }
#ifdef WIN32
    WSACleanup();
#endif

}

#pragma clang diagnostic pop