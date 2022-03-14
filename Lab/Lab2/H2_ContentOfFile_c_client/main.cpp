#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int c;
    uint16_t fileLength;
    struct sockaddr_in server;
    char filePath[1024];
    c = socket(AF_INET, SOCK_STREAM, 0);
    if (c < 0) {
        printf("Eroare la crearea socketului client\n");
        return 1;
    }
    memset(&server, 0, sizeof(server));
    server.sin_port = htons(1234);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr("192.168.100.15");

    if (connect(c, (struct sockaddr *) &server, sizeof(server)) < 0) {
        printf("Eroare la conectarea la server\n");
        return 1;
    }
    printf("Enter string: ");
    scanf("%s", filePath);
    int length = strlen(filePath);
    length = htons(length);
    send(c, &length, sizeof(length), 0);

    send(c, filePath, sizeof(filePath), 0);
    recv(c, &fileLength, sizeof(fileLength), 0);
    fileLength = ntohs(fileLength);
    printf("The length of the file %d\n", fileLength);
    close(c);
    return(0);
}