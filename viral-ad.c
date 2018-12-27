#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// Complete the viralAdvertising function below.
int viralAdvertising(int n) {
    int l = 2, c = 2;
    for(int i=2;i<=n;i++){
        l = floor((l * 3) / 2);
        c += l;
    }
    return c;
}

int main(){

    int n;
    scanf("%d", &n);

    int result = viralAdvertising(n);

    printf("%d\n", result);

    return 0;

}

