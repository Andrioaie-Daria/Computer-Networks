////
//// Created by daria on 07/10/2021.
////
//
//#include <sys/types.h>
//#include <sys/socket.h>
//#include <stdio.h>
//#include <netinet/in.h>
//#include <netinet/ip.h>
//#include <string.h>
//#include <unistd.h>
//#include <arpa/inet.h>
//#include <string.h>
//
//int main(){
//    int c, length;
//    struct sockaddr_in server;
//    uint16_t count = 0;
//    char* array = (char*)malloc(100);
//    strcpy(array, "Ana are multe mere.");
//
//
//    c = socket(AF_INET, SOCK_STREAM, 0);
//    if(c < 0){
//        printf("Eroare la creearea socketului.\n");
//        return 1;
//    }
//    memset(&server, 0, sizeof(server));
//    server.sin_port = htons(1234);
//    server.sin_family = AF_INET;
//    server.sin_addr.s_addr = inet_addr("192.168.100.15");
//
//    if(connect(c, (struct sockaddr*) &server, sizeof(server)) <0 ){
//        printf("Eroare la conectarea la server\n");
//        return 1;
//    }
//
//    length = strlen(array);
//    length = htons(length);
//    if(send(c, &length, sizeof(length), 0) < sizeof(length)){
//        printf("Error on sending length");
//    }
//    if(send(c, array, length, 0) < length){
//        printf("Error on sending array");
//    }
//    if(recv(c, &count, sizeof(count), 0) < sizeof(count)){
//        printf("Error on receiving count of spaces\n");
//    }
//    count = ntohs(count);
//    printf("The number of spaces is %hu.\n", count);
//    close(c);
//}