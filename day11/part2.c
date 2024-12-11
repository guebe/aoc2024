#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#define SZ 8192
struct item { uint64_t stone; uint64_t count; };
//struct item counter[SZ] = { { 125, 1}, {17, 1} };
struct item counter[SZ] = { {41078,1}, {18,1}, {7,1}, {0,1}, {4785508,1}, {535256,1}, {8154,1}, {447,1} };
struct item new[SZ];
void update(uint64_t key, uint64_t value) {
    bool found = false;
    int i;
    for (i = 0; i < SZ; i++) {
        uint64_t k = new[i].stone;
        uint64_t v = new[i].count;
        if (k == key) {
            new[i].count += value;
            found = true;
            break;
        }
        else if (v == 0) break; /* end of list */
    }
    if (!found) {
        new[i].stone = key;
        new[i].count = value;
    }
}

void dbg(void) {
    for (int i = 0; i < SZ; i++) {
        uint64_t k = counter[i].stone;
        uint64_t v = counter[i].count;
        if (v == 0) break;
        printf("%lu:%lu ",k,v);
    }
    printf("\n");
}

int main(void) {
    for (int i = 0; i < 75; i++) {
        memset(new, 0, sizeof(struct item)*SZ);
        printf("at %d\n", i);
        for (int j = 0; j < SZ; j++) {
            uint64_t stone = counter[j].stone;
            uint64_t count = counter[j].count;
            if (count == 0) break; /* end of list */
            if (stone == 0) update(1, count); /* stone 0->1 */
            else {
                char str[22];
                sprintf(str, "%lu", stone);
                size_t len = strlen(str);
                if (len % 2 == 0) {
                    uint64_t stone2 = strtoull(str+len/2,NULL,10);
                    str[len/2] = 0;
                    uint64_t stone1 = strtoull(str,NULL,10);
                    update(stone1, count);
                    update(stone2, count);
                }
                else update(stone*2024, count);
            }
        }
        memcpy(counter, new, sizeof(struct item)*SZ);
        dbg();
    }

    uint64_t total = 0;
    for (int i = 0; i < SZ; i++) {
        uint64_t count = counter[i].count;
        if (count == 0) break; /* end of list */
        total += count;
    }
    printf("%lu\n", total); /*FIXME*/
    return 0;
}
