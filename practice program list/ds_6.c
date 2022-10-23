#include<stdio.h>
int main(void)
{ 
    int j,i,k=1;
    for(i=1;i<=4;i++)
  {
      k=i;
    for(j=1;j<=4;j++)
    {
        if(j<=i)
        {
           printf("%d",k);
           
        }
        else
           printf(" ");
    }
    printf("\n");
  }    
}