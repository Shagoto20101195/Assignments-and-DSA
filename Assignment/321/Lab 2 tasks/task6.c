#include <stdio.h>

int main()
{
    int n;
    printf("Enter seconds: ");
    scanf("%d", &n);
    int hour = n / 3600;
    n %= 3600;
    int min = n / 60;
    int sec = n % 60;
    printf("Hour: %d Minute: %d Second: %d\n", hour, min, sec);
    return 0;
}
