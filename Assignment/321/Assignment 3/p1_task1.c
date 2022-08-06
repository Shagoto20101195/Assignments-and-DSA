#include <stdio.h>

struct Paratha
{
    int quantity;
    float unit_price;
};

struct Vegetable
{
    int quantity;
    float unit_price;
};

struct Mineral_Water
{
    int quantity;
    float unit_price;
};



int main()
{
    struct Paratha p;
    struct Vegetable v;
    struct Mineral_Water m;

    printf("Quantity of Paratha: ");
    scanf("%d", &p.quantity);
    printf("Unit price: ");
    scanf("%f", &p.unit_price);

    printf("Quantity of Vegetable: ");
    scanf("%d", &v.quantity);
    printf("Unit price: ");
    scanf("%f", &v.unit_price);

    printf("Quantity of Mineral Water: ");
    scanf("%d", &m.quantity);
    printf("Unit price: ");
    scanf("%f", &m.unit_price);

    int n;
    printf("Number of People: ");
    scanf("%d", &n);

    float res = (p.quantity*p.unit_price) + (v.quantity*v.unit_price) + (m.quantity*m.unit_price);
    res /= n;
    printf("Individual people will pay: %f tk", res);

    return 0;
}
