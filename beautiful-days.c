#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int reverse(int n){
    int r, rev = 0;
    while(n > 0){
        r = n % 10;
        rev = rev * 10 + r;
        n = n / 10;
    }
    return rev;
}

// Complete the beautifulDays function below.
int beautifulDays(int i, int j, int k) {
    int count = 0, c;
    for(c=i;c<=j;c++){
        if(abs(c - reverse(c)) % k == 0)
            count++;
    }
    return count;
}

int main(){

    int i, j, k;
    scanf("%d%d%d", &i, &j, &k);

    int result = beautifulDays(i, j, k);

    printf("%d\n", result);

    return 0;
}

