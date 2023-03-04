#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <unistd.h>

#define BLOCK_SIZE 16
#define MAX_PACKET_SIZE 256
#define PADDING_SIZE 1 + BLOCK_SIZE * 2

void win(){
    int c;
    FILE *file;
    file = fopen("flag.txt", "r");
    if (file) {
        while ((c = getc(file)) != EOF)
            putchar(c);
        fclose(file);
    }
}

struct FakePacket {
    uint16_t packet_id;
    uint16_t len;
    char pad[PADDING_SIZE];
    uint8_t data[MAX_PACKET_SIZE-(PADDING_SIZE-1)];
};

void init(){
    setvbuf(stdout, NULL , _IONBF , 0);
    setvbuf(stderr, NULL , _IONBF , 0);
    setvbuf(stdin, NULL , _IONBF , 0);
}

int main(int argc, char** argv){
    init();
    struct FakePacket fp;
    memset(fp.pad, 0, PADDING_SIZE);
    printf("Enter packet data: ");
    uint8_t* recvd_bytes = (uint8_t*) calloc(1,0x256); 
    ssize_t tot = read(0, recvd_bytes, 0x256);
    if(tot < 3) {
        printf("Invalid packet header");
        exit(-1);
    }
    memcpy(&fp.packet_id, recvd_bytes, sizeof(uint16_t));
    memcpy(&fp.len, recvd_bytes + sizeof(uint16_t), sizeof(uint16_t));
    if (!(fp.len < (MAX_PACKET_SIZE - PADDING_SIZE - 1))){
        puts("Too much data!");
        exit(-1);
    }
    
    memcpy(fp.data, recvd_bytes + (sizeof(uint16_t)*2), fp.len);
    puts("Packet processed!");
    return 0;
}
