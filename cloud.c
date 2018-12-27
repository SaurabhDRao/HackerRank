#include <stdio.h>
#include <stdlib.h>

int jumpingOnClouds(int n, int* c){
    int count = 0, i = 0, flag = 0;
    
    if(n == 2 && c[0] == 0 && c[1] == 0)
        return 1;

    while((i + 2) < n){
        if(c[i+2] != 1){
            i += 2;
            count++;
            flag = 2;
        } else {
            i++;
            count++;
            flag = 1;
        }
        printf("%d ", i);
    }

    if(i == n-2 && flag == 2 && c[i+1] != 1)
        count++;

    return count;
}

int main(){
    int n;
    scanf("%d", &n);
    int c[n];
    for(int i=0;i<n;i++)
        scanf("%d", &c[i]);
    printf("%d", jumpingOnClouds(n, c));
}