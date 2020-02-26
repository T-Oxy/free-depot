#信号の標準入力を受け付ける関数
inputsignal <- function(){
  dig <-readline("ディジタル信号を入力:")
  as.numeric(unlist(strsplit(dig,",")))
}

x <- inputsignal()  #信号x(n)の標準入力を受け付ける
y <- inputsignal()  #信号y(n)の標準入力を受け付ける

N <- length(x)  #信号の長さ
sum <- numeric(2*N-1)
Rxy <- numeric(2*N-1)  #Rxyは相互相関関数

for(k in 1:N){
  sum[k] <- 0
  for(n in N:(N-k+1)){
    sum[k] = x[n]*y[n+k-N] +sum[k] #k-Nは時間差に対応
  }
  Rxy[k] <- sum[k]/(N-abs(k-N))
  print(Rxy[k])  #自己相関関数の計算結果を表示
}

for(k in (N+1):(2*N-1)){
  sum[k]<- 0
  for(n in 1:(2*N-k)){
    sum[k] = x[n]*y[n+k-N] +sum[k] #k-Nは時間差に対応
  }
  Rxy[k] <- sum[k]/(N-abs(k-N))
  print(Rxy[k])  #自己相関関数の計算結果を表示
}
#試しに問3の信号を入力したところ、正しい計算結果を得られた。
