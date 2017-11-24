#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
	int *arr = malloc(sizeof(int) * 5);
	long long int a = 0;
	for(int arr_i = 0; arr_i < 5; arr_i++){
		scanf("%d",&arr[arr_i]);
		a += arr[arr_i];
	}
	long long int min = a;
	long long int max = -a;
	long long int cur;
	for (int i = 0; i < 5; i++)
	{
		cur = (a - arr[i]);
		min = (min < cur) ? min : cur;    
		max = (max > cur) ? max : cur;
	}
	printf("%lld %lld\n", min, max);
	return 0;
}
