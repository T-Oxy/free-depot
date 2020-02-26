x <- c(0.0,3.0,4.0 ,1.0 ,-2.0 ,-1.0 ,0.0 ,10 ,-1.0 ,0.0)
sum =0
N =length(x)
for(i in 1:N){
  sum = sum +x[i]
}
mean <- (sum / N)    #平均値
