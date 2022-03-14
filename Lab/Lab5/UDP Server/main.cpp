//
// Created by daria on 26/10/2021.
//
#include <stdio.h>
#include <iostream>
#ifndef WIN32
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

#else
// on Windows include and link these things
#include<WinSock2.h>
// for uint16_t an so
#include<cstdint>
#endif
#pragma comment(lib,"Ws2_32.lib")

int main(){
#ifdef WIN32
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) < 0) {
        printf("Error initializing the Windows Sockets LIbrary");
        return -1;
    }
#endif
    int sock = socket(AF_INET, SOCK_DGRAM,0);
    if(sock < 0){
        perror("Error on creating socket: ");
    }
    struct sockaddr_in server;
    struct sockaddr_in from;
    memset(&server, 0, sizeof(server));

    server.sin_family = AF_INET;
    server.sin_port = htons(1234);
    server.sin_addr.s_addr = inet_addr("127.0.0.1");

    memset(&server, 0, sizeof(server));
    if (bind(sock,(struct sockaddr *)&server, sizeof(server))<0) {
        perror("Error on binding: ");
    }
    int length = sizeof (struct sockaddr_in);
    char buffer[1024];
    int n = recvfrom(sock, buffer, sizeof(buffer), 0, (struct sockaddr*) &from, &length);

    if(n<0){
        perror("Error on creating socket: ");
    }
    int s = sendto(sock, "got your message\n", 17, 0, (struct sockaddr*)&from, length);
    if(s<0){
        perror("Error on creating socket: ");
    }


    return 0;
}

