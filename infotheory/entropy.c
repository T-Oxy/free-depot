#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define N 128

void read_file(unsigned char image[],char name[]);

int main(){
  int i;
  unsigned char image[N*N]; //画像の一次元データ
  char name[10]; //画像データの名前
  int M0=0, M1=0,M00=0,M01=0,M10=0,M11=0,M000=0,M001=0,M010=0,M011=0,M100=0,M101=0,M110=0,M111=0;//出力記号の個数カウンター
  double P[18];  //出力記号の確率
  double H1,H2,H3,HS0,HS1,HS2,HS3; //エントロピー

  printf("画像データの名前：");
  scanf("%s",name);  //ファイル名を指定
  read_file(image,name); //データ読み込み

//各個数を求める
  for(i=0;i<N*N-2;i++){  //
    if(image[i]==0) {
      M0++;
      if(image[i+1]==0){
        M00++;
        if(image[i+2]==0){
          M000++;
        } else {
          M001++;
        }
      } else {
        M01++;
        if(image[i+2]==0){
          M010++;
        } else {
          M011++;
        }
      }
    } else {  //image[i]==1
      M1++;
      if(image[i+1]==0){
        M10++;
        if(image[i+2]==0){
          M100++;
        } else {
          M101++;
        }
      } else {
        M11++;
        if(image[i+2]==0){
          M110++;
        } else {
          M111++;
        }
      }
    }
  }
  if(image[N*N-2]==0){
    M0++;
    if(image[N*N-1]==0){
      M0++;
      M00++;
    } else {
      M1++;
      M01++;
    }
  } else {
    M1++;
    if(image[N*N-1]==0){
      M0++;
      M10++;
    } else {
      M1++;
      M11++;
    }
  }

//確率計算
  P[0]=(double)M0/(M0+M1);
  P[1]=(double)M1/(M0+M1);
  P[2]=(double)M00/(M00+M01);
  P[3]=(double)M01/(M00+M01);
  P[4]=(double)M10/(M10+M11);
  P[5]=(double)M11/(M10+M11);
  P[6]=(double)M00/(M00+M01+M10+M11);
  P[7]=(double)M01/(M00+M01+M10+M11);
  P[8]=(double)M10/(M00+M01+M10+M11);
  P[9]=(double)M11/(M00+M01+M10+M11);
  P[10]=(double)M000/(M000+M001);
  P[11]=(double)M001/(M000+M001);
  P[12]=(double)M010/(M010+M011);
  P[13]=(double)M011/(M010+M011);
  P[14]=(double)M100/(M100+M101);
  P[15]=(double)M101/(M100+M101);
  P[16]=(double)M110/(M110+M111);
  P[17]=(double)M111/(M110+M111);

  printf("無記憶情報源の場合:\nP0=%f, P1=%f\n",P[0],P[1]);
  for(i=0;i<2;i++){  //0log2(0)=0に特別の配慮
    if(P[i]==0) {P[i]=1;}
  }
  H1=(-P[0]*log(P[0])-P[1]*log(P[1])) / log(2);  //式(4)の計算
  printf("H1=%f\n\n",H1);

  printf("単純マルコフ情報源の場合:\nP0=%f, P1=%f, P2=%f, P3=%f, P4 =%f, P5=%f\n",P[0],P[1],P[2],P[3],P[4],P[5]);
  for(i=0;i<6;i++){
    if(P[i]==0) {P[i]=1;} //0log2(0)=0に特別の配慮
  }
  HS0= (-P[2]*log(P[2])-P[3]*log(P[3])) / log(2);  //式(3)の計算
  HS1= (-P[4]*log(P[4])-P[5]*log(P[5])) / log(2);  //式(3)の計算
  H2= P[0]*HS0+P[1]*HS1;  //式(2)の計算
  printf("H2=%f\n\n",H2);

  printf("2次のマルコフ情報源の場合:\nP6=%f, P7=%f, P8=%f, P9=%f, P10 =%f, P11=%f, P12=%f, P13=%f, P14=%f, P15=%f, P16 =%f, P17=%f\n",P[6],P[7],P[8],P[9],P[10],P[11],P[12],P[13],P[14],P[15],P[16],P[17]);
  for(i=6;i<18;i++){
    if(P[i]==0) {P[i]=1;} //0log2(0)=0に特別の配慮
  }
  HS0= (-P[10]*log(P[10])-P[11]*log(P[11])) / log(2);  //式(3)の計算
  HS1= (-P[12]*log(P[12])-P[13]*log(P[13])) / log(2);  //式(3)の計算
  HS2= (-P[14]*log(P[14])-P[15]*log(P[15])) / log(2);  //式(3)の計算
  HS3= (-P[16]*log(P[16])-P[17]*log(P[17])) / log(2);  //式(3)の計算
  H3 = P[6]*HS0+P[7]*HS1+P[8]*HS2+P[9]*HS3;  //式(2)の計算
  printf("H3=%f\n",H3);

  return 0;
}

//ファイル読み込み用関数
void read_file(unsigned char image[],char name[]){
  FILE *fp;
  char c[N*N+1];
  int i;

  if((fp=fopen(name,"r"))==NULL){
    printf("error\n");
    exit(1);
  }
  fgets(c,N*N+1,fp);
  for(i=0;i<N*N;i++) {image[i] = c[i]-48;}
}
