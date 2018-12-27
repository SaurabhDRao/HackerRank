#include <stdio.h>
#include <stdlib.h>

int main()
{
    int b, n, m, i, j, sum=0, flag=0, max, t;
    scanf("%d%d%d", &b, &n, &m);
    int k[n], u[m];
    printf("%d\n%d\n", n, m);
    for(i=0;i<n;i++){
        scanf("%d", &k[i]);
    }
    for(i=0;i<m;i++){
        scanf("%d", &u[i]);
        printf("%d\n", k[i]);
    }
    max = t = k[0] + u[0];
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            sum = k[i] + u[j];
            if(sum <= b && sum > max){
                max = sum;
                flag = 1;
            }
        }
    }
    if((t == max && t <= b) || flag == 1)
        printf("%d", max);
    else
        printf("-1");
    return 0;
}