#include<stdio.h>
#include<stdlib.h>
int main()
{
    char alpha[27];
    int index;
    char standard[30] = "0ETAOINSRHLDUCFMWYGPBVkxjqz";
    for(int i=1;i<=21;i++)
    {
        scanf("%d",&index);
        alpha[index] = standard[i];
         printf("alpha[%d]=%c\n",index,alpha[index]);
    }
    int oper;
    for(int i=1;i<=21;i++)
    {
        printf("%c",alpha[i]);
    }
    printf("\n");
   
    while(1)
    {
        if(scanf("%d",&oper)==EOF)
        {
            break;
        }
        if(oper==0)
        {
            printf("\n");
        }
        if(oper==-1)
        {
            printf(" ");
        }
        if(oper>0)
        {
            printf("%c",alpha[oper]);
        }
    }
 }