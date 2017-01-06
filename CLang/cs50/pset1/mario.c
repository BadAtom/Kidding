#include <cs50.h>
#include <stdio.h>

int main(void) {
    int height = 0;

    do {
        printf("Height: ");
        height = GetInt();
    } while (height < 0 || height > 23);

    int counter = height - 1;

    for (int i = 0; i<height; i++, counter--) {
        for (int j = 0; j < counter; j++) {
            printf(" ");
        }

        for (int j = 0; j < 2 + i; j++) {
            printf("#");
        }

        printf("\n");
    }
}