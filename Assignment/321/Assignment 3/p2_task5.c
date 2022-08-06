#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{
	pid_t parent, child, grandchild;

	parent = fork();

	if(parent == 0)
    {
        child = fork();

        if(child == 0)
        {
            for(int i = 0; i<3; i++)
            {
                grandchild = fork();

                if(grandchild != 0)
                {
                    printf("Grandchild process ID: %d\n", grandchild);
                }
            }
        }
        else
        {
            printf("Child process ID: %d\n", child);
        }
    }
    else
    {
        printf("Parent process ID: %d\n", parent);
    }

	return 0;
}
