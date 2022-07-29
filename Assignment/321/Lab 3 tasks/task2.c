#include <stdio.h>

int main()
{
    int a, b, c;
    printf("Enter angles: ");
    scanf("%d %d %d", &a, &b, &c);

    if(a + b + c == 180 && a != 0 && b != 0 && c != 0)
    {
        printf("\nTraingle");
    }
    else
    {
        printf("\nNot a triangle");
    }
    return 0;
}
