#include <stdio.h>

/*
Assumptions:
Numeric digit input only.
Input string is less then BUFSIZ.
*/

int
main(int argc, char *argv[])
{
	char buf[BUFSIZ], c, *ptr = buf;

	while ((c = getchar()) && c != EOF && c != '\n')
		if (ptr < buf + sizeof(buf))
			*ptr++ = c;

	/* Remove these few lines later. */
	while (--ptr >= buf)
		putchar(*ptr);

	/* Find the minimum digit (value) and swap it with the lowest digit (in order). */

	putchar('\n');
	return 0;
}
