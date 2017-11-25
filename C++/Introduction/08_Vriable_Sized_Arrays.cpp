#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,q,k,x,y;
    cin >> n >> q;
    int **ar = new int *[n];
    for (int i = 0; i < n; i++)
    {
        cin >> k;
        ar[i] = new int[k];
        for (int j = 0 ; j < k; j++)
            cin >> ar[i][j];
    }
    for (int i = 0; i < q ; i++)
    {
        cin >> x >> y;
        cout << ar[x][y] << endl;
    }
    for (int i = 0; i < n ; i++)
    {
        delete[] ar[i];
    }
    delete [] ar;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
