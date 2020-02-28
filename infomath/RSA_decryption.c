#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//拡張ユークリッド互除法
void extgcd( int a, int b, int* x, int* y, int* d ){
    int u, v, q, tmp;
    *x = 1; *y = 0; u = 0; v = 1;
    while ( b > 0 ) {
        q = a / b;
        tmp = u; u = *x - q * u; *x = tmp;
        tmp = v; v = *y - q * v; *y = tmp;
        tmp = b; b = a - q * b; a = tmp;
    }
    *d = a;
}

////メイン関数////
int main(){
    int n = 323;  //公開鍵
    int e = 23;  //公開鍵
    int d;  //秘密鍵
    int A[] = {304,61,307,103,304,224,260,181,278,260,102,245,176,224,144,245,103,176};  //暗号
    int bit[32];  //２進計算法で使用する配列
    int Anumber = sizeof A/sizeof A[0]; //Aの要素数
    int x, y, pq, i, j, B, C;
//p*qを求める
    for(i=2; i<sqrt(n); i++){
        if(n%i==0) {
            pq = (i-1)*((n/i)-1);
            break;
        }
    }
//dを求める
    extgcd(e,pq,&d,&x,&y);
    if(d<0){ d += pq; }


//線形計算法
    for(i=0; i<Anumber; i++){
        B = A[i]%n;  //Bが解読文字
        for(j=0; j<d-1; j++){
            B = (B*A[i]) %n;
        }
        printf("%c",B);
    }
    printf("\n");
    
//２進計算法
    for(i=0; d>0; i++){  //偶奇分けする配列作成
        bit[i] = d%2;
        d = d/2;
    }
    x = i-1;

    for(i=0; i<Anumber; i++){
        C=1;  //Cが解読文字
        for(j=x; j>-1; j--){
            C = C*C % n;
            if(bit[j] == 1) { C = C*A[i] % n; }
        }
        printf("%c",C);
    }
    printf("\n");
    
    return 0;
}



