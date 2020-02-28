#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double f(double x){
  return x*x*x - 7;
}

double df(double x){
  return 3*x*x;
}

void regula_falsi(double a,double b, double eps){
  int i=0;
  double c;
  do {
    i++;
    c = (a*f(b) - b*f(a)) / (f(b) - f(a));
    if (f(c) == 0) {
      printf("x(%d)=%.20lf \n",i,c);
      break;
    }
    if (f(a) * f(c) < 0) { b = c; }
    if (f(a) * f(c) > 0) { a = c; }
    printf("x(%d)=%.20lf \n",i,c);
  } while (fabs(f(c)) > eps);
}

void newton(double a, double eps){
  int i=0;
  double ah;
  while(i<100) {
    printf("x(%d)=%.20lf \n",i,a);
    i++;
    ah = a - f(a)/df(a);
    if(fabs(ah - a)<eps){  //収束判定
      printf("x(%d)=%.20lf \n",i,a);
      break;
    }
    a = ah;
  }
}

int main(){
  printf("regula_falsi法:\n");
  regula_falsi(1.5,2.0,1.0e-12);
  printf("\n newton法:\n");
  newton(1.75, 1.0e-12);
  return 0;
}
