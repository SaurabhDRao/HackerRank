#include <stdio.h>
#include <stdlib.h>

// Complete the insertionSort1 function below.
void insertionSort1(int n, int* a) {
    int t = a[n - 1], i;
    for(i=n-2;i>=0;i--){
        if(a[i] > t){
            a[i + 1] = a[i];
            for(int j=0;j<n;j++)
                printf("%d ", a[j]);
            printf("\n");
        } else {
            a[i + 1] = t;
            for(int j=0;j<n;j++)
                printf("%d ", a[j]);
            printf("\n");
            break;
        }
    }
    if(i == -1 && a[0] == a[1]){
        a[0] = t;
        for(int j=0;j<n;j++)
            printf("%d ", a[j]);
        printf("\n");
    }
}

int main(){
    int n;
    scanf("%d", &n);
    int a[n];
    for(int i=0;i<n;i++)
        scanf("%d", &a[i]);

    insertionSort1(n, a);

    return 0;
}

