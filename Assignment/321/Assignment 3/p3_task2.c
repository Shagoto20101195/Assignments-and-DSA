#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *myfunc(int n);

int main()
{
    pthread_t t1, t2, t3, t4, t5;

    pthread_create(&t1, NULL, myfunc, 1);
    pthread_join(t1, NULL);

    pthread_create(&t2, NULL, myfunc, 6);
    pthread_join(t2, NULL);

    pthread_create(&t3, NULL, myfunc, 11);
    pthread_join(t3, NULL);

    pthread_create(&t4, NULL, myfunc, 16);
    pthread_join(t4, NULL);

    pthread_create(&t5, NULL, myfunc, 21);
    pthread_join(t5, NULL);

    return 0;
}

void *myfunc(int n)
{
    int thread_num = n / 5 + 1;
    for(int i = n; i<n+5; i++)
    {
        printf("Thread %d prints %d\n", thread_num, i);
    }
}
