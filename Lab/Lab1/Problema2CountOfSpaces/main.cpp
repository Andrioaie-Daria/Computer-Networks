// exists on all platforms

#include <stdio.h>

// this section will only be compiled on NON Windows platforms
#ifndef WIN32
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <errno.h>
#define closesocket close
typedef int SOCKET;
#else

// on Windows include and link these things

#include<WinSock2.h>

// for uint16_t an so

#include<stdint.h>

#endif

int main(){
    SOCKET s;
    struct sockaddr_in welcoming, communication;
    int c, l, err;

#ifdef WIN32
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) < 0) {
        printf("Error initializing the Windows Sockets LIbrary");
        return -1;
    }
#endif
    s = socket(AF_INET, SOCK_STREAM, 0);
    if(s < 0){
        perror("Error on socket:");
        return 1;
    }
    memset(&welcoming, 0, sizeof(welcoming));
    welcoming.sin_port = htons(1234);
    welcoming.sin_family = AF_INET;
    welcoming.sin_addr.s_addr = INADDR_ANY;

    if(bind(s, (struct sockaddr*) &welcoming, sizeof(welcoming)) < 0 ){
        perror("Bind error");
        return 1;
    }
    listen(s, 5);
    l = sizeof(communication);
    memset(&welcoming, 0, l);
    while(1){
        printf("Listening for incoming connections..\n");
        c = accept(s, (struct sockaddr*) &communication, &l);
        err = errno;
#ifdef WIN32
        err = WSAGetLastError();
#endif
        if(c<0){
            printf("accept error: %d", err);
            continue;
        }
        printf("Incoming connected client from address %s, port %d\n", inet_ntoa(communication.sin_addr), ntohs(communication.sin_port));

        uint16_t length;
        if(recv(c, (char*)&length, sizeof(length), 0) != sizeof(length)){
            printf("Error on receiving length\n");
        }
        length = ntohs(length);
        printf("Length of array is %d.\n", length);
        //char* string = (char*)malloc(length+1);
        char string[length+1];

        int result = recv(c, string, length, 0);
        if( result != length){
            printf("Error on receiving array\n");
            printf("Received %d bytes\n", result);

        }
        // printf("Array is %s\n", string); ??? prints empty array
        uint16_t count=0;

        for(int i = 0; i< length; i++){
            if(string[i] == ' ')
                count += 1;
        }
        count = htons(count);
        if(send(c, (char*)&count, sizeof(count), 0) != sizeof(count)){
            printf("Error on sending count");
        }
        printf("Done\n");
        //free(string);
        closesocket(c);
    }
    // never reached
    // Release the Windows Sockets Library
#ifdef WIN32
    WSACleanup();
#endif
}