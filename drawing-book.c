#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, p, res;
    scanf("%d%d", &n, &p);

    if(p <= n / 2){
         if(p % 2 == 0)
            res = p / 2;
        else
            res = (p - 1) / 2;
    } else {
        p = n - p;
        if(p == 1 && n % 2 == 0)
            res = 1;
        else{
            if(p % 2 == 0)
                res = p / 2;
            else   
                res = (p - 1) / 2;
        }
    }
    printf("%d", res);
    return 0;
}