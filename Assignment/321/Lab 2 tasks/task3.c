#include <stdio.h>

int main()
{
    double r;
    printf("Enter radius: ");
    scanf("%lf", &r);
    double pi = 22.0 / 7.0;
    double perimeter = 2*r*pi;
    double area = pi * r * r;
    printf("Perimeter: %lf\nArea: %lf", perimeter, area);
    return 0;
}
