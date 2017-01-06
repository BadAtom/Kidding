#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int ForUpper(int bukva, int key) {
    int result = bukva + key;
    if (result > 'Z')
        result -= 26;
    return result;
}

int ForLower(int bukva, int key) {
    int result = bukva + key;
    if (result > 'z')
        result -= 26;
    return result;
}

int main(int argc, string argv[]) {
    if (argc == 2) {
        if (argv != NULL) {
    

        for (int i = 0; i < strlen(argv[1]); ++i) {
            if (isalpha(argv[1][i]) || argv[1][i] == ' ') {
                printf("%i\n", 1);
                return 1;
            }
        }

        int k = atoi(argv[1]);
        if (k < 0) {
            printf("%i\n", 1);
            return 1;
        }
        if (k > 26)
            do {
                k = k % 26;
            } while (k > 26);

        string text = GetString();
    // printf("%s, %i", text, k);
        if (text != NULL)
            for (int j = 0; j < strlen(text); ++j) {
                if (isalpha(text[j])) {
                    if (isupper(text[j])) {
                        printf("%c", ForUpper(text[j], k));
                    } else printf("%c", ForLower(text[j], k));
                } else printf("%c", text[j]);
            }
        else {
            printf("%i\n", 1);
            return 1;
        }
        
        printf("\n");
        
        }
    } else {
        printf("%i\n", 1);
            return 1;
    }
}