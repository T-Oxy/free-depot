#信号の標準入力を受け付ける関数
inputsignal <- function(){
  dig <-readline("ディジタル信号を入力:")
  as.numeric(unlist(strsplit(dig,",")))
}

x <- inputsignal()    #信号の標準入力を受け付ける

N <- length(x)  #信号の長さ
sum <- numeric(N)
Rxx <- numeric(N)  #Rxxは自己相関関数

for(m in 0:(N-1)){  #mは時間のズレ
  sum[m+1] <- 0
  for(n in 1:(N-m)){  #nは時点
    sum[m+1] = x[n]*x[n+m] +sum[m+1]
  }
  Rxx[m+1] <- sum[m+1]/(N-abs(m))  #ベクトルRxx[m+1]は、実際のRxx(m)に対応
  print(Rxx[m+1])  #自己相関関数の計算結果を表示
}
#試しに問1の信号を入力したところ、正しい計算結果を得られた。
