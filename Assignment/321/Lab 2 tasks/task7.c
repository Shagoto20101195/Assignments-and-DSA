#include <stdio.h>

int main()
{
    int a, b;
    printf("Enter numbers: ");
    scanf("%d %d", &a, &b);
    int temp = a;
    a = b;
    b = temp;
    printf("Swapped numbers: %d %d\n", a, b);
    return 0;
}
