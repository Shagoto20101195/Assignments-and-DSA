#include <stdio.h>

void subtract(int a, int b);
void add(int a, int b);
void multiply(int a, int b);

int main()
{
    int a, b;
    char op;
    printf("Enter numbers and operator: ");
    scanf("%d %d %c", &a, &b, &op);

    if(a > b)
    {
        subtract(a, b);
    }
    else if(a < b)
    {
        add(a, b);
    }
    else
    {
        multiply(a, b);
    }

    return 0;
}

void subtract(int a, int b)
{
    printf("Result: %d\n", (a-b));
}

void add(int a, int b)
{
    printf("Result: %d\n", (a+b));
}

void multiply(int a, int b)
{
    printf("Result: %d\n", (a*b));
}
