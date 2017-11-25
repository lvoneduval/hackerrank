#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;



int main() {
    vector<int> v;
    int N;
    int tmp1, tmp2;
    cin >> N;
    tmp2 = N;
    while (tmp2 > 0)
    {
        cin >> tmp1; 
        v.push_back(tmp1);
        tmp2--;
    }
 //   sort(v.begin(), v.end());
    cin >> tmp1;
    v.erase(v.begin() + tmp1 - 1);
    cin >> tmp1 >> tmp2;
    v.erase(v.begin() + tmp1 - 1, v.begin() + tmp2 - 1);
    cout << v.size() <<endl;
    for (auto i : v)
    {
        cout << i << ' ';
    }
    cout << endl;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
