#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int *myfunc(char m[]);

int main()
{
    pthread_t t1, t2, t3;
    int *ans1, *ans2, *ans3;
    char m1[100], m2[100], m3[100];

    printf("Enter string 1: ");
    scanf("%s", &m1);
    printf("Enter string 2: ");
    scanf("%s", &m2);
    printf("Enter string 3: ");
    scanf("%s", &m3);

    pthread_create(&t1, NULL, myfunc, m1);
    pthread_join(t1, &ans1);

    pthread_create(&t2, NULL, myfunc, m2);
    pthread_join(t2, &ans2);

    pthread_create(&t3, NULL, myfunc, m3);
    pthread_join(t3, &ans3);

    if(*ans1 == *ans2 && *ans2 == *ans3)
    {
        printf("Youreka\n");
    }
    else if((*ans1 == *ans2) || (*ans2 == *ans3) || (*ans1 == *ans3))
    {
        printf("Miracle\n");
    }
    else
    {
        printf("Hasta la vista\n");
    }

    return 0;
}

int *myfunc(char m[])
{
    int ans = 0;
    for(int i = 0; i<strlen(m); i++)
    {
        ans += (int)m[i];
    }

    int *res = malloc(sizeof(int));
    *res = ans;
    return (int*) res;
}
