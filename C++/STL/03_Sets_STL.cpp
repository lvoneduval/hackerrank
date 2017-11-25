#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    set<int> s;
    int q,type,val;
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        cin >> type >> val;
        switch (type)
        {
            case 1:
                s.insert(val);
                break ;
            case 2:
                s.erase(val);
                break ;
            case 3:
                if (s.find(val) != s.end())
                    cout << "Yes" << endl;
                else
                    cout << "No" << endl;
        }
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
