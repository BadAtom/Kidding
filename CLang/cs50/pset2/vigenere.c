#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

void ProgramExitWithError(string string1) {
    printf("Process exit with fault code: 1. Error message: [%s].", string1);
    exit(1);
}

int Key_Key(int for_search, int* small) {
    for (int i = 0; i < 26; i++) {
        if (for_search == small[i])
            return i;
    }

    return 0;
}

int main(int argc, string argv[]) {
    if (argc < 2) ProgramExitWithError("No arguments initialized");
    if (argc > 2) ProgramExitWithError("More than one argument in line");

    int small_chars[26];
    for (int i = 'a', j = 0; i <= 'z'; j++, i++) {
        small_chars[j] = i;
    }

    int keys[sizeof(argv[1])];

    for (int i = 0; i < strlen(argv[1]); i++) {
        if (!isalpha(argv[1][i]))
            ProgramExitWithError("Non alphabetic character in keyword");
        else
            keys[i] = Key_Key(tolower(argv[1][i]), small_chars);
    }

    string text = GetString();

    for (int i = 0, j = 0; i < strlen(text); i++) {
        int temp = text[i];

        if (isalpha(text[i])) {
            temp = text[i] + keys[j++];
            if (j == strlen(argv[1]))
                j = 0;

            if (isupper(text[i])) {
                if (temp > 'Z') {
                    temp -= 26;
                }
            } else {
                if (temp > 'z') {
                    temp -= 26;
                }
            }
        }

        printf("%c", (char) temp);
    }

    printf("\n");
}