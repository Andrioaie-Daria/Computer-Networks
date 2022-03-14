#include <iostream>
#include <winsock2.h>

int main() {
    WSADATA wsaData;
    WSAStartup(MAKEWORD(2,2), &wsaData);

    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    char flag = '1';
    if(setsockopt(sock, SOL_SOCKET, SO_BROADCAST, &flag, sizeof(flag)) < 0)
    {
        printf("Error in setting Broadcast option");
        closesocket(sock);
        return 0;
    }
    struct sockaddr_in broadcast;
    broadcast.sin_family = AF_INET;
    broadcast.sin_port = htons(1234);
    broadcast.sin_addr.s_addr = inet_addr("192.168.100.255");
    int length = sizeof(struct sockaddr_in);

    char message[] = "Hello world";
    sendto(sock, message, strlen(message)+1,0,(struct sockaddr*)&broadcast, length);

    return 0;
}
