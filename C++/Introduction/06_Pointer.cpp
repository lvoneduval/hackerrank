#include <stdio.h>

int abs(int a)
{
   return(a < 0 ? -a : a);
}
void update(int *a,int *b) {
    int tmp = *b;
    *b = abs(*b - *a);
    *a += tmp;
    // Complete this function    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", pa, pb);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
