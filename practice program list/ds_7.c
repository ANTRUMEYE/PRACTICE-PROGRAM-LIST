#include<stdio.h>
int main(void)
{ 
    int j,i,k;
    for(i=1;i<=4;i++)
  {
    for(j=1;j<=7;j++)
    {
        if(j>=5-i && j<=3+i)
        {
           printf("%d",k);
           k=k+1;
           
        }
        else
           printf(" ");
    }
    printf("\n");
  }    
}