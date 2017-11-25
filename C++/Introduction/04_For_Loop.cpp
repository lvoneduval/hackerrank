#include <iostream>
#include <cstdio>

int main(){
    int n, m, tmp;
    const char *word[11] = {"even","one","two","three","four","five","six","seven","eight","nine", "odd"};
    std::cin >> n >> m;
    for (int i = n; i <= m; i++)
    {
        tmp = (i <= 9) ? i : (i % 2) == 0 ? 0 : 10;
        std::cout << word[tmp] << std::endl;
    }
    // your code goes here
    return 0;
}
