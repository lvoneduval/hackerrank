#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

char* timeConversion(char* s) {
	// Complete this function
	char *ss = 0;
	int h;

	h = (s[0]- '0') * 10 + s[1]- '0';
	if ((ss =strstr(s, "PM")))
	{
		if (h != 12)
		{
			h += 12;
			s[0] = (h / 10) + '0';
			s[1] = (h % 10) + '0';
		}
		*ss = 0;
	}
	else if ((ss = strstr(s, "AM")))
	{
		*ss = 0;
		if (h == 12)
		{
			s[0] = '0';
			s[1] = '0';
		}
	}
	return (s);
}

int main() {
	char* s = (char *)malloc(512000 * sizeof(char));
	scanf("%s", s);
	int result_size;
	char* result = timeConversion(s);
	printf("%s\n", result);
	return 0;
}
