#include <stdio.h>

void diameter(double r);
void circumference(double r);
void area(double r);

int main()
{
    double r;
    printf("Enter radius: ");
    scanf("%lf", &r);

    diameter(r);
    circumference(r);
    area(r);

    return 0;
}

void diameter(double r)
{
    double ans = r * 2;
    printf("Diameter: %lf\n", ans);
}

void circumference(double r)
{
    double ans = 2 * 22.0/7.0 * r;
    printf("Circumference: %lf\n", ans);
}

void area(double r)
{
    double ans = 22.0/7.0 * r * r;
    printf("Area: %lf\n", ans);
}
