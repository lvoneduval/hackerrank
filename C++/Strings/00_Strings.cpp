#include <iostream>
#include <string>
using namespace std;

void swap(char *a, char *b)
{
    char c;
    c = *a;
    *a = *b;
    *b = c;
}

int main() {
   // Complete the program
    int sizea, sizeb;
    string a, b, c;
    cin >> a >> b;
    sizea = a.size();
    sizeb = b.size();
    c = a + b;
    cout << sizea << ' ' << sizeb << endl;
    cout << c << endl;
    swap(&a[0], &b[0]);
    cout << a << ' ' << b <<endl;
    return 0;
}
