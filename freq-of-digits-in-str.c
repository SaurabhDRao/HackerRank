#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i, a[10];
    for(i=0;i<10;i++)
        a[i] = 0;
    char str[1000];
    scanf("%s", str);
    for(i=0;i<strlen(str);i++){
        if(isdigit(str[i]) != 0)
            a[str[i] - '0']++;
    }  
    for(i=0;i<10;i++)
        printf("%d ", a[i]);
    return 0;
}
