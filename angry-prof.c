#include <stdio.h>
#include <stdlib.h>

char* angryProfessor(int k, int n, int* a) {

    int count = 0, flag = 0;
    for(int i=0;i<n;i++){
        if(a[i] <= 0)
            count++;
        
        if(count == k){
            flag = 1;
            break;
        }
    }
    
    return flag == 0 ? "YES" : "NO";

}

int main(){
    int t, n, k;
    scanf("%d", &t);
    for(int j=0;j<t;j++){
        scanf("%d%d", &n, &k);
        int a[n];
        for(int l=0;l<n;l++)
            scanf("%d", &a[l]);
        char* result = angryProfessor(k, n, a);
        printf("%s\n", result);
    }
}