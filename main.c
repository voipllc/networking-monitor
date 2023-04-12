#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>

#define BUF_SIZE 512

int main() {
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    char buf[BUF_SIZE];
    
    // Open the "/proc/net" directory and read its contents
    fp = fopen("/proc/net", "r");
    if (fp == NULL) {
        perror("fopen");
        exit(EXIT_FAILURE);
    }
    
    // Read each file in the directory and parse the packet information
    while ((read = getline(&line, &len, fp)) != -1) {
        if (strstr(line, "tcp") != NULL || strstr(line, "udp") != NULL) {
            snprintf(buf, BUF_SIZE, "/proc/net/%s", line);
            FILE* net_fp = fopen(buf, "r");
            if (net_fp == NULL) {
                perror("fopen");
                exit(EXIT_FAILURE);
            }
            printf("Packet information in %s:\n", buf);
            while ((read = getline(&line, &len, net_fp)) != -1) {
                printf("%s", line);
            }
            fclose(net_fp);
        }
    }
    
    fclose(fp);
    if (line) free(line);
    exit(EXIT_SUCCESS);
}