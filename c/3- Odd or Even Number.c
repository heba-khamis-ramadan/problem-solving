/* Find Odd or Even Number */

#include<stdio.h>

int main()
{
    int num;
    scanf("%d", &num);
    /* check if the num is dividable by 2 */
    if (num%2 == 0)
    {
        printf ("Even");
    }
    /* if the number is not dividable by 2 then it is odd */
    else
    {
        printf("Odd");
    }

    return 0;
}