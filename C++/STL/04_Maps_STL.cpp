#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int main() {
    map<string, int> mp;
    int q,type,val;
    map<string, int>::iterator it;
    string name;
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        cin >> type >> name;
        switch (type)
        {
            case 1:
                cin >> val;
                it = mp.find(name);
                if (it != mp.end())
                    mp[name] += val;
                else
                    mp[name] = val;
                break ;
            case 2:
                mp.erase(name);
                break ;
            case 3:
                map<string, int>::iterator it;
                it = mp.find(name);
                if (it != mp.end())
                    cout << mp[name] << endl;
                else
                    cout << 0 << endl;
                break ;
        }
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
