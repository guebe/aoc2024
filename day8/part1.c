#include <assert.h>
#include <stdio.h>
#include <string.h>
#include "input.h"
#define MAX 1024
struct point { int r; int c; };
int main(void) {
	static struct point antenna[MAX];
	static char antinodes[SZ][SZ];
	int t = 0;

	for (char j = '.'+1; j <= 'z'; j++) {
		int i = 0;
		for (int r = 0; r < SZ; r++) for (int c = 0; c < SZ; c++) if (grid[r][c] == j) {
			assert(i < MAX);
			antenna[i] = (struct point){.r=r, .c=c};
			i++;
		}
		if (i > 0) printf("%c\n", j);
		for (int k = 0; k < i; k++) { printf("(%d, %d)\n", antenna[k].r, antenna[k].c); }
		for (int k = 0; k < i-1; k++) for (int l = k+1; l < i; l++) {
			printf("%d %d\n", k, l);
			struct point a1 = antenna[k];
			struct point a2 = antenna[l];
			int dr = a1.r - a2.r;
			int dc = a1.c - a2.c;
			struct point n1 = (struct point){.r = a1.r + dr, .c = a1.c + dc};
			struct point n2 = (struct point){.r = a2.r - dr, .c = a2.c - dc};
			printf("(%d, %d), (%d, %d) delta %d %d -> (%d, %d) (%d, %d)\n", a1.r, a1.c, a2.r, a2.c, dr, dc, n1.r, n1.c, n2.r, n2.c);
			if (n1.r >= 0 && n1.c >= 0 && n1.r < SZ && n1.c < SZ) {
				if (antinodes[n1.r][n1.c] != '#') t++;
				antinodes[n1.r][n1.c] = '#';
			}
			if (n2.r >= 0 && n2.c >= 0 && n2.r < SZ && n2.c < SZ) {
				if (antinodes[n2.r][n2.c] != '#') t++;
				antinodes[n2.r][n2.c] = '#';
			}
	       	}
       	}
	printf("%d\n", t);
	return 0;
}
