#include <stdio.h>

int main()
{
    char ch;
    printf("Enter character: ");
    scanf("%c", &ch);

    int temp = (int)ch;

    if(temp == 65 || temp == 69 || temp == 73 || temp == 79 || temp == 85 || temp == 97 || temp == 101 || temp == 105 || temp == 111 || temp == 117)
    {
        printf("\nVowel");
    }
    else
    {
        printf("\nConsonant");
    }
    return 0;
}
