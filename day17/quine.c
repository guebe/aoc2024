#include <stdio.h>
const char f[] = "#include <stdio.h>%cconst char f[] = %c%s%c;%cint main(void) {%c    printf(f,10,34,f,34,10,10,10,10);%c}%c";
int main(void) {
    printf(f,10,34,f,34,10,10,10,10);
}
