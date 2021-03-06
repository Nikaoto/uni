// Author: Nika Otiashvili
// K&R exercise "longest"

#include <stdio.h>
#define MAXLINE 1000

int get_line(char s[], int lim);
void copy(char to[], char from[]);

int main(void)
{
	 int len; // Current line length
	 int max; // Max length so far
	 char line[MAXLINE]; // Current line content
	 char longest[MAXLINE]; // Longest line content so far

	 max = 0;
	 while ((len = get_line(line, MAXLINE)) > 0)
		  if (len > max) {
			   max = len;
			   copy(longest, line);
		  }

	 // If a at least one line was input
	 if (max > 0)
		  printf("%s", longest);

	 return 0;
}

// Reads a line into s, returns length
int get_line(char s[], int lim)
{
	 int c, i;

	 for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i) {
		  s[i] = c;
	 }
	 if (c == '\n') {
		  s[i] = c;
		  ++i;
	 }
	 s[i] = '\0';
	 return i;
}

void copy(char to[], char from[])
{
	 int i;
	 i = 0;
	 while ((to[i] = from[i]) != '\0')
		  ++i;
}
