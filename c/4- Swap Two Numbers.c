/* Swap Two Numbers */

#include<stdio.h>

int main()
{
    int a, b;
    scanf("%d%d", &a, &b);
    
    /* decleare an extra temperory variable to hold the initial value of a */
    int temp;
    temp = a;
    a = b;
    b = temp;
    
    printf("%d %d\n", a, b);
    return 0;
}