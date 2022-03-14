//
// Created by daria on 12/10/2021.
//
// on Windows include and link these things
#include<WinSock2.h>
// for uint16_t an so
#include<stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void treatRequest(int client_s){
    char buffer[1024];
    int length = recv(client_s, buffer, 1024, 0);
    if(length <= 0){
        perror("Error on receive");
    }
//    char* args[10];
//    int count=0;
//    char* token = strtok(buffer, (const char *) ' ');
//    while(token != NULL){
//        strcpy(args[count++], token);
//        token = strtok(NULL, (const char *) ' ');
//    }
    printf("Received %s with length: %d\n", buffer, length);

    FILE* fd = popen(buffer, (const char *) 'r');
    char currentLine[100];

    while (fgets(currentLine, sizeof(currentLine), fd) != NULL) {
        printf("got line: %s\n", currentLine);
        if(send(client_s, currentLine, strlen(currentLine), 0) <=0 ){
            perror("Error on sending standard output: ");
        }
    }
    char* over_message = "over";
    send(client_s, over_message, strlen(over_message), 0);
    int exit_code = pclose(fd);
    exit_code = htons(exit_code);
    if(send(client_s, (const char *) &exit_code, sizeof(exit_code), 0) <= 0 ){
        perror("Error on sending exit code: ");
    }
}


int main() {
#ifdef WIN32
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) < 0) {
        printf("Error initializing the Windows Sockets Library");
        return -1;
    }
#endif
    int welcoming_s = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in server, client;

    if (welcoming_s < 0) {
        printf("Eroare la crearea socketului server\n");
        return 1;
    }
    memset(&server, 0, sizeof(server));
    server.sin_port = htons(1234);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;

    if(bind(welcoming_s, (struct sockaddr*) &server, sizeof(server)) < 0){
        perror("Error on bind: ");
    }
    listen(welcoming_s, 10);
    while(1){
        int length = sizeof(client) ;
        int c = accept(welcoming_s, (struct sockaddr*)&client, &length);
        if(fork() == 0){
            treatRequest(c);
            closesocket(c);
            exit(0);
        }
        // parent
    }
    return 0;
}


