#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main(){
    int n;
    string word[10] = {"Greater than 9","one","two","three","four","five","six","seven","eight","nine"};
    cin >> n;
    n = (n <= 9) ? n : 0;
    cout << word[n] << endl;
    // your code goes here
    return 0;
}
