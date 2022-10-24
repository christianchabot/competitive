#include <stdio.h>

/*
Assumptions:
The input string length will fit into a long long integer.
The input character set is lowercase latin characters.
*/
static unsigned long long seen['z' - 'a'];

int
main(int argc, char *argv[])
{
	unsigned long long index = 0;
	char c;

	while ((c = getchar()) && c != EOF && c != '\n')
		if (c <= 'z' && c >= 'a' && !seen[c - 'a'])
			seen[c - 'a'] = ++index;

	unsigned long long min_index, si;
	do {
		unsigned long long i;

		min_index = index;
		for (i = 0; i < 'z' - 'a'; ++i)
			if (seen[i] && seen[i] <= min_index)
				min_index = seen[si = i];

		if (min_index < index)
			putchar('a' + si), seen[si] = 0;
	} while (min_index < index);

	putchar('a' + si);
	return putchar('\n'), 0;
}
