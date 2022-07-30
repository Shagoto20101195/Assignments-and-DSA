#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE *fp;
    fp = fopen("temp.txt", "r");

    FILE *nfp;
    nfp = fopen("new_temp.txt", "w");

    char buff[255];
    fgets(buff, 255, fp);

    char ans[255];
    char *word = strtok(buff, " ");
    while(word != NULL)
    {
        strcat(ans, word);
        strcat(ans, " ");
        word = strtok(NULL, " ");
    }
    fputs(ans, nfp);

    fclose(fp);
    fclose(nfp);
}
