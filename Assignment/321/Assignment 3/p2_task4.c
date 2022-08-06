#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
    pid_t a;
    a = fork();

    if(a == 0)
    {
        execl("sort", "sort", argv, NULL);
    }
    else
    {
        wait();
        execl("oddeven", "oddeven", argv, NULL);
    }
    return 0;
}
