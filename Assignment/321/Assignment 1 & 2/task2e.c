#include <stdio.h>
#include <stdbool.h>
int main()
{
    char ch[100];
    char *lpnt, *rpnt;
    scanf("%s", &ch);
    lpnt = &ch;
    rpnt = &ch;
    bool check = true;


    for(int i = 0; i<strlen(ch) - 1; i++)
    {
        rpnt++;
    }

    for(int i = 0; i<strlen(ch) / 2; i++)
    {
        if(*lpnt != *rpnt)
        {
           check = false;
           break;
        }
        else
        {
            lpnt++;
            rpnt--;
        }
    }

    if(check)
    {
        printf("Palindrome\n");
    }
    else
    {
        printf("Not a palindrome\n");
    }

    return 0;
}
