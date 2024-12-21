#include <assert.h>
#include <stdio.h>
#include "input.h"
#define MAX 1024
struct point { int x; int y; };
static struct point antenna[MAX];
static char antinode[SZ][SZ];
static inline int in_bounds(struct point p) { return p.x >= 0 && p.y >= 0 && p.x < SZ && p.y < SZ; }
static inline struct point sub(struct point p1, struct point p2) { return (struct point){.x = p1.x - p2.x, .y = p1.y - p2.y }; }
static inline struct point add(struct point p1, struct point p2) { return (struct point){.x = p1.x + p2.x, .y = p1.y + p2.y }; }
static inline int is_antinode(struct point p) { return (antinode[p.y][p.x] != '#') ? (antinode[p.y][p.x] = '#', 1) : 0; }
int main(void) {
	int result = 0;
	for (char c = '0'; c <= 'z'; c++) { /* all possible frequencies */
		int cnt = 0;
		for (int y = 0; y < SZ; y++) for (int x = 0; x < SZ; x++) if (grid[y][x] == c) {
			assert(cnt < MAX); antenna[cnt++] = (struct point){.x=x, .y=y}; /* build a list of same-frequency antennas */
		}
		for (int i = 0; i < cnt-1; i++) for (int j = i+1; j < cnt; j++) {
			struct point a1 = antenna[i], a2 = antenna[j], delta = sub(a1, a2); /* calc delta for all antenna pairs */
			do result += is_antinode(a1); while (in_bounds(a1 = add(a1, delta))); /* add antinodes until oob */
			do result += is_antinode(a2); while (in_bounds(a2 = sub(a2, delta))); /* sub antinodes until oob */
		}
	}
	printf("%d\n", result); return 0;
}
