#! /usr/bin/python
# -*- coding: utf-8 -*-

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

x=np.array([40,65,95,180,205,225])
y=np.array([4.5,0,-2.9,-2.2,0,5.6])
f= interp1d(x, y, kind='cubic')  #3次スプライン補間

#作図------
a1 = np.linspace(x[0],x[-1],num=100,endpoint=True)
b1 = f(a1)
plt.plot(x, y, 'ro',label="controlpoint")
plt.plot(a1,b1,label="interp1d")
plt.title("spline")
plt.xlim([0, 250])
plt.ylim([-10, 10])
plt.legend(loc='lower right')
plt.grid(which='major',color='black',linestyle='-')
plt.grid(which='minor',color='black',linestyle='-')
plt.xticks(list(filter(lambda x: x%1==0, np.arange(0,250))))
plt.yticks(list(filter(lambda x: x%1==0, np.arange(-10,10))))
plt.show()

#黄金分割
def gold(a, b, eps, val, ind, max, fun) :
    x      = 0.0
    tau    = (np.sqrt(5.0) - 1.0) / 2.0
    count  = 0
    ind[0] = -1
    x1     = b - tau * (b - a)
    x2     = a + tau * (b - a)
    f1     = fun(x1)
    f2     = fun(x2)
    
    while count < max and ind[0] < 0 :
        count += 1
        if f2 > f1 :
            if (abs(b-a) < eps) and (abs(b-a) < eps*abs(b)) :
                ind[0] = 0
                x      = x1
                val[0] = f1
            else :
                b  = x2
                x2 = x1
                x1 = a + (1.0 - tau) * (b - a)
                f2 = f1
                f1 = fun(x1)
        else :
            if (abs(b-a) < eps) and (abs(b-a) < eps*abs(b)) :
                ind[0] = 0
                x      = x2
                val[0] = f2
                f1     = f2
            else :
                a  = x1
                x1 = x2
                x2 = b - (1.0 - tau) * (b - a)
                f1 = f2
                f2 = fun(x2)

    if ind[0] == 0 :
        ind[0] = count
        print("eps=" + str(abs(b-a)))
        fa     = fun(a)
        fb     = fun(b)
        if fb < fa :
            a  = b
            fa = fb
        if fa < f1 :
            x      = a
            val[0] = fa

    return x

# 設定と実行
a   = 95
b   = 180
eps = 1.0e-7
max = 100
val = np.empty(1, np.float)
ind = np.empty(1, np.int)

x = gold(a, b, eps, val, ind, max, f)

print("x=" + str(x) + " y=" + str(val[0]) + " ind=" + str(ind[0]))
