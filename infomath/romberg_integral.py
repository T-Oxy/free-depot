#! /usr/bin/python
# -*- coding: utf-8 -*-

from scipy.interpolate import interp1d
from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np

x=np.array([40,65,95,180,205,225])
y=np.array([4.5,0,-2.9,-2.2,0,5.6])
f= interp1d(x, y, kind='cubic')  #3次スプライン補間

##これはひどい。(for文で書けば何行削れる?)
X1 = np.linspace(65, 205, num=2**1+1)
Y1 = f(X1)
yRomb1 = integrate.romb(Y1,X1[1]-X1[0])
print("Romb1= ",yRomb1)     # 結果の表示
X2 = np.linspace(65, 205, num=2**2+1)
Y2 = f(X2)
yRomb2 = integrate.romb(Y2,X2[1]-X2[0])
print("Romb2= ",yRomb2)     # 結果の表示
X3 = np.linspace(65, 205, num=2**3+1)
Y3 = f(X3)
yRomb3 = integrate.romb(Y3,X3[1]-X3[0])
print("Romb3= ",yRomb3)     # 結果の表示
X4 = np.linspace(65, 205, num=2**4+1)
Y4 = f(X4)
yRomb4 = integrate.romb(Y4,X4[1]-X4[0])
print("Romb4= ",yRomb4)     # 結果の表示
X5 = np.linspace(65, 205, num=2**5+1)
Y5 = f(X5)
yRomb5 = integrate.romb(Y5,X5[1]-X5[0])
print("Romb5= ",yRomb5)     # 結果の表示
X6 = np.linspace(65, 205, num=2**6+1)
Y6 = f(X6)
yRomb6 = integrate.romb(Y6,X6[1]-X6[0])
print("Romb6= ",yRomb6)     # 結果の表示
X7 = np.linspace(65, 205, num=2**7+1)
Y7 = f(X7)
yRomb7 = integrate.romb(Y7,X7[1]-X7[0])
print("Romb7= ",yRomb7)     # 結果の表示
X8 = np.linspace(65, 205, num=2**8+1)
Y8 = f(X8)
yRomb8 = integrate.romb(Y8,X8[1]-X8[0])
print("Romb8= ",yRomb8)     # 結果の表示
X9 = np.linspace(65, 205, num=2**9+1)
Y9 = f(X9)
yRomb9 = integrate.romb(Y9,X9[1]-X9[0])
print("Romb9= ",yRomb9)     # 結果の表示
X10 = np.linspace(65, 205, num=2**10+1)
Y10 = f(X10)
yRomb10 = integrate.romb(Y10,X10[1]-X10[0])
print("Romb10= ",yRomb10)     # 結果の表示
X11 = np.linspace(65, 205, num=2**11+1)
Y11 = f(X11)
yRomb11 = integrate.romb(Y11,X11[1]-X11[0])
print("Romb11= ",yRomb11)     # 結果の表示
