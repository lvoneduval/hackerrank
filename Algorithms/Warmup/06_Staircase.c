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
	int i = 0;
	int j = n;
	while (i < n)
	{
		j--;
		for (int k = 0; k < n; k++)
		{
			printf("%c", (k < j)?' ':'#');
		}
		printf("\n");
		i++;
	}
	return 0;
}
