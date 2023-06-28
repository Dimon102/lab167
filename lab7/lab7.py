import math
from decimal import Decimal
import matplotlib.pyplot as plt

mas_P0 = []
mas_P1 = []
mas_P2 = []
mas_P3 = []
mas_P4 = []
mas_P5 = []
mas_P6 = []
mas_P7 = []
mas_P8 = []
mas_P9 = []
mas_P10 = []
mas_P11 = []
mas_P12 = []
mas_P13 = []
mas_P14 = []
mas_P15 = []
mas_t = []

def f0(P0,P1,P2,P3):
    return 2*(-3*P0+P1+P2+P3)

def f1(P0,P1,P4,P5):
    return 2*(-3*P1+P0+P4+P5)
def f2(P0,P2,P6,P7):
    return 2*(-3*P2 + P0+P6+P7)
def f3(P0,P3,P8,P9):
    return 2*(-3*P3+P0+P8+P9)
def f4(P1,P4,P10):
    return 2*(-2*P4+P1+P10)

def f5(P1,P5,P11):
    return 2*(-2*P5+P1+P11)

def f6(P2,P6,P12):
    return 2*(-2*P6+P12+P2)

def f7(P2,P7,P13):
    return 2*(-2*P7+P13+P2)

def f8(P3,P8,P14):
    return 2*(-2*P8+P3+P14)

def f9(P3,P9,P15):
    return 2*(-2*P9+P3+P15)

def f10(P4,P10):
    return 2*(-P10+P4)

def f11(P5,P11):
    return 2*(-P11+P5)

def f12(P6,P12):
    return 2*(-P12+P6)

def f13(P7,P13):
    return 2*(-P13+P7)

def f14(P8,P14):
    return 2*(-P14+P8)

def f15(P9,P15):
    return 2*(-P15+P9)

def eiler(P0, P1, P2, P3, P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14, P15,a, b, h):
    global mas_t, mas_P15,mas_P14,mas_P13,mas_P12,mas_P11,mas_P10,mas_P9,mas_P8,mas_P7,mas_P6,mas_P5,mas_P4, mas_P3, mas_P2, mas_P1, mas_P0
    t = a
    while t < b:
        P0 += (f0(P0,P1,P2,P3)*h)
        P1 += (f1(P0,P1,P4,P5)*h)
        P2 += (f2(P0,P2,P6,P7)*h)
        P3 += (f3(P0,P3,P8,P9)*h)
        P4 += (f4(P1,P4,P10)*h)
        P5 += (f5(P1,P5,P11) * h)
        P6 += (f6(P2,P6,P12) * h)
        P7 += (f7(P2,P7,P13) * h)
        P8 += (f8(P3,P8,P14) * h)
        P9 += (f9(P3, P9, P15) * h)
        P10 += (f10(P4, P10) * h)
        P11 += (f11(P5, P11) * h)
        P12 += (f12(P6, P12) * h)
        P13 += (f13(P7, P13) * h)
        P14 += (f14(P8, P14) * h)
        P15 += (f15(P9, P15) * h)
        mas_P0.append(P0)
        mas_P1.append(P1)
        mas_P2.append(P2)
        mas_P3.append(P3)
        mas_P4.append(P4)
        mas_P5.append(P5)
        mas_P6.append(P6)
        mas_P7.append(P7)
        mas_P8.append(P8)
        mas_P9.append(P9)
        mas_P10.append(P10)
        mas_P11.append(P11)
        mas_P12.append(P12)
        mas_P13.append(P13)
        mas_P14.append(P14)
        mas_P15.append(P15)

        mas_t.append(t)
        t += h
    print(P0, P1, P2, P3, P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14, P15)

a = 0
b = 20
h = 0.001

eiler(1, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0, a, b, h)

fig, axs = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(10)

axs.grid(color='black',
linewidth=1,
linestyle='--')

axs.axis([mas_t[0], mas_t[-1], 0, 1.1])
axs.plot(mas_t, mas_P0, 'r', label='P0', linewidth=2)
axs.plot(mas_t, mas_P1, 'g', label='P1', linewidth=2)
axs.plot(mas_t, mas_P2, 'b', label='P2', linewidth=2)
axs.plot(mas_t, mas_P3, 'y', label='P3', linewidth=2)
axs.plot(mas_t, mas_P4, 'c', label='P4', linewidth=2)
axs.plot(mas_t, mas_P5, 'm', label='P5', linewidth=2)
axs.plot(mas_t, mas_P6, 'k', label='P6', linewidth=2)
axs.plot(mas_t, mas_P7, 'gold', label='P7', linewidth=2)
axs.plot(mas_t, mas_P8, 'plum', label='P8', linewidth=2)
axs.plot(mas_t, mas_P9, 'blue', label='P9', linewidth=2)
axs.plot(mas_t, mas_P10, 'violet', label='P10', linewidth=2)
axs.plot(mas_t, mas_P11, 'r', label='P11', linewidth=2)
axs.plot(mas_t, mas_P12, 'g', label='P12', linewidth=2)
axs.plot(mas_t, mas_P13, 'plum', label='P13', linewidth=2)
axs.plot(mas_t, mas_P14, 'y', label='P14', linewidth=2)
axs.plot(mas_t, mas_P15, 'k', label='P15', linewidth=2)
axs.legend(loc='upper right')

plt.show()
