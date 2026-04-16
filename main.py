# AIM: Write a Python program to print a 
# triangle pattern (give any), emphasizing
# the transition from C to Python syntax.
# Coder: Khan Ayaan Shakeel
# Date:4/2/26


# Write your code here
#include <stdio.h>

int main() {
    int i, j, rows = 5;

    for(i = 1; i <= rows; i++) {
        for(j = 1; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }

    return 0;
}
