#include<iostream>
using namespace std;
int gcdf(int f1, int f2, int &s, int &t);  //f1,f2に対して、s,t,d(返り値として)を求める関数

int main(){
    int a,b,s,t;
    cout << "f1を入力：";
    cin >> a;
    cout << "f2を入力：";
    cin >> b;

    cout << "d=" << gcdf(a,b,s,t) << ", s=" << s << ", t=" << t << endl;
    return 0;
}

int gcdf(int f1, int f2, int &s, int &t){
    if(f2 == 0){
        s =1;
        t =0;
        return f1;
    }
    int d =gcdf(f2,f1%f2,t,s);
    t =t -f1/f2 *s;
    return d;
}
