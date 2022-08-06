#include <stdio.h>
#include<sys/types.h>
#include <unistd.h>

int main(void) {
	pid_t pid1, pid2;
    pid1 = fork();
    wait();

    if(pid1 == 0)
    {
        pid2 = fork();
        wait();

        if(pid2 == 0)
        {
            printf("I am grandchild\n");
        }
        else
        {
            printf("I am child\n");
        }
    }
    else
    {
        printf("I am parent\n");
    }



	return 0;
}
