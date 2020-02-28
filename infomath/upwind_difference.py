#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

pi = math.pi  # 円周率
t1 = 3.0
dt = 0.0001  # 時間ステップ
step = int(t1/dt)  # ステップ数
nx = 100.0  # x方向の分点数
L = 5.0  # 領域幅
dx = L / nx  # x方向のメッシュ幅
x = np.arange(0, L, dx)  # x座標
# u = u(x)の初期条件(関数)
u = np.sin(pi*x) #0<=x<=1,つまりu[0]~u[20]を確定
for i in range(21,99):
    u[i] = 0.0  #0<=x<=1以外、つまりu[21]~u[49]も確定
c = 0.04*math.sqrt(13)+1# 移流速度
ims = []  # グラフの格納場所

# クーラン数, CFL条件（courant<1）を満たさないときは停止する
courant = c*dt/dx
print('courant number is ', courant)
if courant >= 1:
    print('CFL condition is not satisfied.')
    sys.exit(1)

# 波数を返す
def get_k(i):
    if i <= nx/2:
        return (2*pi/L)*i
    else:
        return (2*pi/L)*(i-nx)

# 1階導関数を返す
def differentiate(in_data_F):
    out_data_F = np.zeros(int(nx/2+1), dtype=np.complex) # 出力データ
    for i in range(int(nx/2+1)):# 微分
        k = get_k(i)
        Re = in_data_F[i].real
        Im = in_data_F[i].imag
        out_data_F[i] = np.complex(-k*Im, k*Re)
    return out_data_F

# メイン
def main():
    fig = plt.figure()
    u_F = np.fft.rfft(u)
    
    for n in range(step):
        # 導関数
        drv_u_F = differentiate(u_F)
        u_F -= c * dt * drv_u_F
        # プロット用に実空間に戻す
        # u_plotted = np.fft.irfft(u_F)
        #im = plt.plot(x, u_plotted, 'r')
        #ims.append(im)

    u_plotted = np.fft.irfft(u_F)
    print(u_plotted)
    im = plt.plot(x, u_plotted, 'r')
    ims.append(im)
    plt.show()


#for n in range(step):
        # 導関数
        #       drv_u_F = differentiate(u_F)
        #u_F -= c * dt * drv_u_F
        #print(u_F)
        # プロット用に実空間に戻す
        #u_plotted = np.fft.irfft(u_F)
        #im = plt.plot(x, u_plotted, 'r')
#ims.append(im)
    
    #    ani = animation.ArtistAnimation(fig, ims, interval=1)
#ani.save('LinearAdvectionSample.gif', writer='imagemagick')

if __name__ == '__main__':
    main()
