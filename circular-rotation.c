#include <stdio.h>
#include <stdlib.h>

int main(){

    int n, k, q, qi;
    scanf("%d%d%d", &n, &k, &q);
    int rot = k % n;
    int a[n];
    for(int i=0;i<n;i++)
        scanf("%d", &a[i]);
    for(int i=0;i<q;i++){
        scanf("%d", &qi);
        if(qi - rot >= 0)
            printf("%d\n", a[qi - rot]);
        else
            printf("%d\n", a[qi - rot + n]);
    }

    return 0;
}

