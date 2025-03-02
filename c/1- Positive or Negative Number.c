/* Find Positive or Negative Number*/

#include <stdio.h>

int main()
{
    int num;
    scanf("%d", &num);
    
    /* check if the num is less than zero */
    if (num < 0)
    {
        printf ("Negative");
    }
    /* check if the num is greater than zero */
    else if (num > 0)
    {
      printf ("Positive");  
    }
    /* check if the num is equal to zero */
    else
    {
        printf("Neither positive nor negative");
    }
    
    return 0;
}