#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void) {
    float money = 0;
    
    printf("O hai! ");

    do {
        printf("How much change is owed?\n");
        money = GetFloat();
    } while (money < 0);

    int iMoney = (int) round(money * 100);

    int coinCounter = 0;

    while (iMoney >= 25) {
        coinCounter++;
        iMoney -= 25;
    }

    while (iMoney >= 10) {
        coinCounter++;
        iMoney -= 10;
    }

    while (iMoney >= 5) {
        coinCounter++;
        iMoney -= 5;
    }

    while (iMoney > 0) {
        coinCounter++;
        iMoney -= 1;
    }

    printf("%d\n", coinCounter);
}