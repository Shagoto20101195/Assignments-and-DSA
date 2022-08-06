#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
    for(int i = 1; i<argc-1; i++)
    {
        int min_val = atoi(argv[i]);
        int min_ind = i;
        for(int j = i+1; j<argc; j++)
        {
            if(atoi(argv[j]) < min_val)
            {
                min_val = atoi(argv[j]);
                min_ind = j;
            }
        }

        int temp = argv[min_ind];
        argv[min_ind] = argv[i];
        argv[i] = temp;
    }

    for(int i = argc; i>=1; i--)
    {
        printf("%s\n", argv[i]);
    }

    return 0;
}
