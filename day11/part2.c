#include <assert.h>
#include <inttypes.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SZ 4096
struct item { uint64_t key; uint64_t value; };
struct item counter[SZ] = { {41078,1}, {18,1}, {7,1}, {0,1}, {4785508,1}, {535256,1}, {8154,1}, {447,1} };
struct item new[SZ];
static inline int idx(uint64_t key) { int i; for (i = 0; i < SZ; i++) if (new[i].value == 0) { new[i].key = key; break; } else if (new[i].key == key) break; assert(i < SZ); return i; }
static inline bool split(uint64_t n, uint64_t *n1, uint64_t *n2) { char str[22]; sprintf(str, "%lu", n); size_t len = strlen(str); return len%2 ? false : (*n2 = strtoull(str+len/2,0,10), str[len/2] = 0, *n1 = strtoull(str,0,10), true); }
int main(void) {
    for (int i = 0; i < 75; i++) {
        memset(new, 0, sizeof(struct item)*SZ);
        for (int j = 0; j < SZ; j++) {
            uint64_t stone1, stone2, stone = counter[j].key, count = counter[j].value;
            if (count == 0) break; /* end of list */
            if (stone == 0) new[idx(1)].value += count; /* stone 0->1 */
            else if (split(stone, &stone1, &stone2)) { new[idx(stone1)].value += count; new[idx(stone2)].value += count; } /* split stones */
            else new[idx(stone*2024)].value += count; /* stone *= 2024 */
        }
        memcpy(counter, new, sizeof(struct item)*SZ);
    }
    uint64_t sum = 0;
    for (int i = 0; i < SZ; i++) if (counter[i].value != 0) sum += counter[i].value; else break;
    printf("%" PRIu64 "\n", sum); return 0;
}
