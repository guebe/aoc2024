#include <stdio.h>
#include <string.h>
#include <input.h>
#define ENC_DIR(dr,dc) (((dr)*2)+(dc))
int main(void) {
	static signed char visited[SZ][SZ]; int i, j, rs = 0, cs = 0, r, c, dr, dc, t = 0, tmp;
	for (i = 0; i < SZ; i++) for (j = 0; j < SZ; j++) if (grid[i][j] == '^') { rs = i; cs = j; break; } /* find start position */
	for (i = 0; i < SZ; i++) for (j = 0; j < SZ; j++) {
		if (grid[i][j] == '.') { 
			grid[i][j] = '#'; dr = -1; dc = 0; r = rs; c = cs; memset(&visited[0][0], 0, SZ*SZ); /* reset state */
			while (1) {
				if (r+dr < 0 || c+dc < 0 || r+dr >= SZ || c+dc >= SZ) { break; } /* check for out-of-bounds */
				if (visited[r+dr][c+dc] == ENC_DIR(dr,dc)) { t++; break; } /* check for endless-loop */
				if (grid[r+dr][c+dc] == '#') { tmp = dr; dr = dc; dc = -tmp; } /* turn right */
				else { r += dr; c += dc; visited[r][c] = ENC_DIR(dr,dc); } /* advance */
			}
			grid[i][j] = '.'; /* reset state */
		}
	}
	printf("%d\n", t); return 0;
}
