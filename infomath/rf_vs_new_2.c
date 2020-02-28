#include<stdio.h>
#include<math.h>
#define EPS (1.0e-10)  //小数第10位まで確定
#define f(x) (x*x*x-7)
#define df(x) (3*x*x)

//regula_falsi
double regula_falsi (double a, double b) {
  double c;
  do {
    c = (a*f(b) - b*f(a)) / (f(b) - f(a));
    if (f(c) == 0) { break; }
    if (f(a) * f(c) < 0) { b = c; }
    if (f(a) * f(c) > 0) { a = c; }
  } while (fabs(f(c)) > EPS);
  return c;
}

int main (void) {
  double alpha;
  alpha = regula_falsi(1.5, 2);
  printf("%.10f\n", alpha);
    
//Newton
  double xn, xo; // x_new x_old
  xn = (xo = 2) + 1;
  while(fabs(xn - xo) > EPS){
    xo = xn;
    xn = -1 *f(xo) / df(xo) + xo;
  }
  printf("%.10f\n", xn);
    
  return 0;
}
