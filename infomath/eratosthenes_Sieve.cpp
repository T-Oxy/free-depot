#include <iostream>
#include <math.h>
#define MAX 10000
using namespace std;

int main(){
    int N[MAX];
    int i,j,count=0;
	for(i = 0; i < MAX; i++){
		N[i] = 1;
    }
	for(i = 2; i < sqrt(MAX); i++){
		if(N[i]==1){
			for(j = 2; i*j < MAX; j++){
				N[i*j] = 0;  //素数でない場合はフラグを0にする
			}
		}
    }
	for(int i = 2; i < MAX; i++){
		if(N[i]==1){
			cout << i << " ";
            count +=1;
		}
	}
    cout << endl << "素数の個数:" << count << endl;
    return 0;
}
