#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    int *l = new int[n];
    for (int i = 0; i < n; i++)
    {
        std::cin >> l[i];
    }
    for (int i = n - 1; i >= 0; i--)
    {
        std::cout << l[i];
        if (i)
            std::cout << ' ';
    }
    delete []l;
    std::cout <<std::endl;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
