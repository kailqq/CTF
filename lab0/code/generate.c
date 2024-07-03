#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

struct hbpkt
{
    uint32_t size;
    uint32_t timestamp;
    uint32_t index;
    uint32_t cred;
    char data[];
};

int main()
{
    struct hbpkt pkt;
    pkt.size=0x1000;//修改这里制造不同的pkt

    pkt.timestamp=0;
    pkt.index=0;
    pkt.cred=1;
    char buffer[0x2000];
    FILE *f=fopen("pkt1","w");
    fwrite(&pkt,sizeof(pkt),1,f);
    memset(buffer,'A',0x20);
    fwrite(buffer,0x20,1,f);
    fclose(f);


}