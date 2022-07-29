#include <stdio.h>

struct student
{
    char name[100];
    int id;
};

int main()
{
    struct student s1;
    printf("Enter name: ");
    scanf("%s", &s1.name);
    printf("Enter id: ");
    scanf("%d", &s1.id);

    printf("Student name is %s and id is %d\n", s1.name, s1.id);
    return 0;
}
