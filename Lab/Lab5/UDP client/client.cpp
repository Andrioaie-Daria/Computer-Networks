#include <iostream>
// on Windows include and link these things
#include<WinSock2.h>
#include "strings.h"

// for uint16_t an so

#include<cstdint>

#pragma comment(lib,"Ws2_32.lib")

int main() {
#ifdef WIN32
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) < 0) {
        printf("Error initializing the Windows Sockets LIbrary");
        return -1;
    }
#endif
    int sock = socket(AF_INET, SOCK_DGRAM,0);
    if(sock < 0){
        perror("error on creating socket");
    }
    struct sockaddr_in server;
    struct sockaddr_in from;
    memset(&server, 0, sizeof(server));

    server.sin_family = AF_INET;
    server.sin_port = htons(1234);
    server.sin_addr.s_addr = inet_addr("192.168.100.18");

    int length = sizeof (struct sockaddr_in);

    char buffer[1024];

    printf("Enter string: ");
    scanf("%s", buffer);
    if(sendto(sock, buffer, 1024, 0, (sockaddr*)&server, length) <0){
        printf("Error on send");
    }


    int received = recvfrom(sock, buffer, 1024,0, (sockaddr*)&from, &length);
    if(received < 0){
        printf("Error on receive");
    }
    printf("%s", buffer);
    return 0;
}
