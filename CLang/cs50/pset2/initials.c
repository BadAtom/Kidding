#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>

void
init(string string1) {
    if (isalpha(string1[0]))
        printf("%c", toupper(string1[0]));

    for (int i = 0; i < strlen(string1); ++i) {
        if (string1[i] == ' ') {
            if (isalpha(string1[i+1])) {
                printf("%c", toupper(string1[i+1]));
            }
        }
    }

    printf("\n");
}

int
main(void) {
    string string1;
    
    do {
        string1 = GetString();
    } while (string1 == NULL);

    init(string1);
}