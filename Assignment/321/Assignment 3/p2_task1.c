#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
    FILE* fp;
    fp = fopen(argv[1], "w+");

    while(1)
    {
        char str[100];
        scanf("%s", &str);

        if(strcmp(str, "-1") == 0)
        {
            break;
        }
        else
        {
            fputs(strcat(str, "\n"), fp);
        }
    }

    fclose(fp);

    return 0;
}
