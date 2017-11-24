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
	int a[n][n];
	for(int a_i = 0; a_i < n; a_i++){
		for(int a_j = 0; a_j < n; a_j++){

			scanf("%d",&a[a_i][a_j]);
		}
	}
	int i = 0;
	int som1 = 0;
	int som2 = 0;

	while (i < n)
	{
		som1 += a[i][i];
		som2 += a[n - i - 1][i];
		i++;
	}  
	printf("%d\n", (abs(som1 - som2)));
	return 0;
}
