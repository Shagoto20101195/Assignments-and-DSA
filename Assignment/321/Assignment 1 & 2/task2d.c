#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int check(char temp[]);

int main()
{
    char inp[100];
    scanf("%s", &inp);

    if(check(inp) == 0)
    {
        printf("Email address is okay\n");
    }
    else
    {
        printf("Email address is outdated\n");
    }

    return 0;
}

int check(char temp[])
{
    int checker = 0;
    char res[100];
    for(int i = 0; i<strlen(temp); i++)
    {
        if(checker == 1)
        {
            if(temp[i] == 's')
            {
                return 0;
            }
            else
            {
                return 1;
            }
        }
        else if(temp[i] == '@')
        {
            checker = 1;
        }
    }
}
