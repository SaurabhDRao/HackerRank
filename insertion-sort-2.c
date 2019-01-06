#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, t;
    scanf("%d", &n);
    int a[n];
    for(int i=0;i<n;i++)
        scanf("%d", &a[i]);
    
    for(int i=1;i<n;i++){
        for(int j=i-1;j>=0;j--){
            if(a[j + 1] < a[j]){
                t = a[j + 1];
                a[j + 1] = a[j];
                a[j] = t;
            }
        }
        for(int k=0;k<n;k++)
            printf("%d ", a[k]);
        printf("\n");
    }
    return 0;
}