#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  int i, j, maxa = 0, maxo = 0, maxx = 0;
  for(i=1;i<n;i++){
      for(j=i+1;j<=n;j++){
        if(((i&j) > maxa) && ((i&j) < k))
            maxa = i&j;
        if(((i|j) > maxo) && ((i|j) < k))
            maxo = i|j;
        if(((i^j) > maxx) && ((i^j) < k))
            maxx = i^j;
      }
  }
  printf("%d\n%d\n%d", maxa, maxo, maxx);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}