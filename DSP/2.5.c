#include<stdio.h>

int main(){
  int n,i;
  int x[n][4];
  int y[n];

  for(n=0;n<6;n++){
    y[n]=0;
    for(i=0;i<4;i++){
      y[n] += x[n][i];
    }
    y[n] = y[n]/4;
    printf("y[%d] = %d",n, y[n]);
  }
  return 0;
}
