#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N, q;
    int tmp;
    vector<int>::iterator k;
    vector<int> v;
    
    cin >> N;
    for (int i = 0; i < N ; i++)
    {
        cin >> tmp;
        v.push_back(tmp);
    }
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        cin >> tmp;
        k = lower_bound(v.begin(), v.end(), tmp);
        cout << ((v[k - v.begin()] == tmp) ? "Yes " : "No ") << k - v.begin() + 1 << endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
