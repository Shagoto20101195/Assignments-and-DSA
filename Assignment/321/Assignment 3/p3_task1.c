#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *myfunc(char *str);

int main()
{
    pthread_t t1, t2, t3, t4, t5;

    char *m1 = "Thread 1";
    char *m2 = "Thread 2";
    char *m3 = "Thread 3";
    char *m4 = "Thread 4";
    char *m5 = "Thread 5";

    pthread_create(&t1, NULL, myfunc, m1);
    pthread_join(t1, NULL);
    printf("%s closed\n", m1);

    pthread_create(&t2, NULL, myfunc, m2);
    pthread_join(t2, NULL);
    printf("%s closed\n", m2);

    pthread_create(&t3, NULL, myfunc, m3);
    pthread_join(t3, NULL);
    printf("%s closed\n", m3);

    pthread_create(&t4, NULL, myfunc, m4);
    pthread_join(t4, NULL);
    printf("%s closed\n", m4);

    pthread_create(&t5, NULL, myfunc, m5);
    pthread_join(t5, NULL);
    printf("%s closed\n", m5);

    return 0;
}

void *myfunc(char *str)
{
    printf("%s running\n", str);
}
