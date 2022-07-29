#include <stdio.h>

int main()
{
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter array: ");

    for(int i = 0; i<n; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("Reverse order:\n");
    for(int i = n-1; i>=0; i--)
    {
        printf("%d\n", arr[i]);
    }
    return 0;
}
