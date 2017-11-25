#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    vector<int> v;
    int N, n;
    int tmp;
    cin >> N;
    n = N;
    while (n > 0)
    {
        cin >> tmp; 
        v.push_back(tmp);
        n--;
    }
    sort(v.begin(), v.end());
    for (int i = 0; i < N; i ++)
    {
        if (i)
            cout << ' ';
        cout << v[i];
    }
    cout << endl;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
