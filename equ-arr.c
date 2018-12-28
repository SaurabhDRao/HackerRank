#include <stdio.h>
#include <stdlib.h>

int maxEle(int n, int* a){
    int max = a[0];
    for(int i=0;i<n;i++){
        if(max < a[i])
            max = a[i];   
    }
    return max;
}

// Complete the equalizeArray function below.
int equalizeArray(int n, int* arr) {
    
    int max = maxEle(n, arr);
    int freq[max + 1];

    for(int i=0;i<max+1;i++)
        freq[i] = 0;

    for(int i=0;i<n;i++){
        freq[arr[i]]++;
    }

    max = maxEle(max + 1, freq);
    return n - max;

}

int main(){
    int n;
    scanf("%d", &n);
    int arr[n];
    for(int i=0;i<n;i++)
        scanf("%d", &arr[i]);
    int res = equalizeArray(n, arr);
    printf("%d", res);
}