#include <stdio.h>
#include <input.h>
int main(void) {
	static char visited[SZ][SZ]; int i, j, r = 0, c = 0, dr = -1, dc = 0, t = 0, tmp;
	for (i = 0; i < SZ; i++) for (j = 0; j < SZ; j++) if (grid[i][j] == '^') { r = i; c = j; break; } /* find start position */
	while (1) {
	        if (r+dr < 0 || c+dc < 0 || r+dr >= SZ || c+dc >= SZ) break; /* check for out-of-bounds */
		if (grid[r+dr][c+dc] == '#') { tmp = dr; dr = dc; dc = -tmp; } /* turn right */
		else { r += dr; c += dc; visited[r][c] = 'X'; } /* advance */
	}
	for (i = 0, c = 0; i < SZ; i++) for (j = 0; j < SZ; j++) if (visited[i][j] == 'X') t++; /* count visited */
	printf("%d\n", t); return 0;
}
