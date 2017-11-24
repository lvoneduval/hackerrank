#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
int cmpfunc (const void * a, const void * b)
{
	return ( *(int*)a - *(int*)b );
}

int birthdayCakeCandles(int n, int ar_size, int* ar) {
	// Complete this function
	qsort(ar, ar_size, sizeof(int), cmpfunc);
	int j = 0;
	n--;
	int max = ar[n];
	while (ar[n] == max)
	{
		j++;
		n--;
	}
	return(j);
}

int main() {
	int n; 
	scanf("%i", &n);
	int *ar = malloc(sizeof(int) * n);
	for(int ar_i = 0; ar_i < n; ar_i++){
		scanf("%i",&ar[ar_i]);
	}
	int result = birthdayCakeCandles(n, n, ar);
	printf("%d\n", result);
	return 0;
}
