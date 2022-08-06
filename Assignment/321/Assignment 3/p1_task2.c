#include <stdio.h>

int check(int n);

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);

    for(int i = a; i<=b; i++)
    {
        if(check(i))
        {
            printf("%d\n", i);
        }
    }

    return 0;
}

int check(int n)
{
    int sum = 0;
    for(int i = 1; i<n; i++)
    {
        if(n % i == 0)
        {
            sum += i;
        }
    }

    if(sum == n)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
