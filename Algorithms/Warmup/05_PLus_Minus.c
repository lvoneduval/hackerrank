#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
	int n; 
	scanf("%d",&n);
	int arr[n];
	for(int arr_i = 0; arr_i < n; arr_i++){
		scanf("%d",&arr[arr_i]);
	}
	double f[3];
	for (int i = 0; i < n; i++)
	{
		f[0] += (arr[i] > 0) ? 1 : 0;
		f[1] += (arr[i] < 0) ? 1 : 0;
		f[2] += (arr[i] == 0) ? 1 : 0;
	} 
	f[0] /= n ;
	f[1] /= n ;
	f[2] /= n ;
	printf("%6f\n%6f\n%6f\n" , f[0], f[1], f[2]);
	return 0;
}
