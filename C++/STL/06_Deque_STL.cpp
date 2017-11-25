#include <iostream>
#include <deque> 
using namespace std;
int new_max(deque<int>& dq)
{
    int max = 0;
    int tmp;
    int s;
    
    s = dq.size();
    for (int i = 0; i < s ;i++)
    {
        tmp = dq[i];
        max = max > tmp ? max : tmp;
    }
    return(max);
}

void print(deque<int>& dq)
{
    int max = 0;
    int tmp;
    int s;
    
    s = dq.size();
    for (int i = 0; i < s ;i++)
    {
        printf("%d ",dq[i]);
    }
    printf("\n");
}

void printKMax(int arr[], int n, int k){
    int i = 0;
    int tmp;
    int max = 0;
    deque<int> dq;
    for (; i < k ; i ++)
    {
        tmp = arr[i];
        dq.push_back(tmp);
        max = max > tmp ? max : tmp;
    }
    cout << max;
    for (; i < n; i++)
    {
        cout << ' ';
        tmp  = arr[i];
        dq.push_back(tmp);
        if (dq[0] == max)
        {
            dq.pop_front();
            max = new_max(dq);
        }
        else
        {
            dq.pop_front();
            max = max > tmp ? max : tmp;
        }
        cout << max;
    }
    cout << endl;
   //Write your code here.
}
int main(){
  
   int t;
   cin >> t;
   while(t>0) {
      int n,k;
       cin >> n >> k;
       int i;
       int arr[n];
       for(i=0;i<n;i++)
            cin >> arr[i];
       printKMax(arr, n, k);
       t--;
     }
     return 0;
}
