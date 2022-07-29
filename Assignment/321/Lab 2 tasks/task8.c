#include <stdio.h>

int main()
{
    char ch;
    printf("Enter a character: ");
    ch = getchar();
    int ans = (int)ch;
    printf("ASCII: %d\n", ans);
    return 0;
}
