/* Find The Absolute Value of a Number */

#include<stdio.h>

int main()
{
    int num;
    scanf("%d", &num);
    
   /* check if the num is greater than or equals zero */
    if (num >= 0)
    {
        printf("%d",num);
    }
   /* multibly the negative value with -1 to get the absolute value */
    else
    {
        num = num * -1;
        printf("%d",num);
    }

    return 0;
}