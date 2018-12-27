#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Write Your Code Here
    int n;
    scanf("%d", &n);
    char a[9][100] = {
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    };
    if(n >= 1 && n <= 9)
        printf("%s", a + (n - 1));
    else
        printf("Greater than 9");
    return 0;
}