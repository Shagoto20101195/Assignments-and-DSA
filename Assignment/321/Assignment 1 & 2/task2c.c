#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    char pass[100];
    scanf("%s", &pass);

    bool um = false;
    bool lm = false;
    bool dm = false;
    bool sm = false;

    for(int i = 0; i<strlen(pass); i++)
    {
        int temp = pass[i];

        if(temp >= 65 && temp <= 90)
        {
            um = true;
        }
        else if(temp >= 97 && temp <= 122)
        {
            lm = true;
        }
        else if(temp >= 48 && temp <= 57)
        {
            dm = true;
        }
        else if(pass[i] == '_' || pass[i] == '$' || pass[i] == '#' || pass[i] == '@')
        {
            sm = true;
        }
    }

    if(um && lm && dm && sm)
    {
        printf("OK\n");
    }
    else
    {
        if(!um)
        {
            printf("Uppercase missing\n");
        }
        if(!lm)
        {
            printf("Lowercase missing\n");
        }
        if(!dm)
        {
            printf("Digit missing\n");
        }
        if(!sm)
        {
            printf("Special missing\n");
        }
    }

    return 0;
}
