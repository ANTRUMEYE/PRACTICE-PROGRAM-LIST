#include<stdio.h>//incomplete mistake//
int mains()
{
    int num,r,sum=0,temp;
    printf("Enter a number:");
    for(temp=num;num!=0;num=num/10)
    {
        r=num%10;
        sum=sum+(r*r*r);
    }
     if(sum==temp)
     {
       printf("%d is an Armstrong number\n",temp);
     else
       printf("%d is not an Armstrong number",temp);
     }
     printf("reverse number=%d",reverse);
     return 0;
}