#include <stdio.h>

int main()
{
    char s1[500];
    char s2[500];
    printf("Enter first string: ");
    gets(s1);
    printf("Enter second string: ");
    gets(s2);

    strcat(s1, s2);
    printf("%s\n", s1);
    return 0;
}
