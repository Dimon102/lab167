from scipy.integrate import odeint
import numpy as np
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
mas_t = []


def f(P, t):
    P0, P1, P2, P3, P4, P5, P6, P7, P8 = P
    return [f0(P0, P1, P2, P3, P4, P5, P6, P7, P8), f1(P0, P1, P2, P3, P4, P5, P6, P7, P8),
            f2(P0, P1, P2, P3, P4, P5, P6, P7, P8), f3(P0, P1, P2, P3, P4, P5, P6, P7, P8),
            f4(P0, P1, P2, P3, P4, P5, P6, P7, P8), f5(P0, P1, P2, P3, P4, P5, P6, P7, P8),
            f6(P0, P1, P2, P3, P4, P5, P6, P7, P8), f7(P0, P1, P2, P3, P4, P5, P6, P7, P8),
            f8(P0, P1, P2, P3, P4, P5, P6, P7, P8)]


def f0(P0, P1, P2, P3, P4, P5, P6, P7, P8):
    return 2 * (-3 * P0 + P1 + P2 + P3)

def f1(P0, P1, P2, P3, P4, P5, P6, P7, P8):
    return 2 * (-3 * P1 + P0 + P4 + P6)

def f2(P0, P1, P2, P3, P4, P5, P6, P7, P8):
    return 2 * (-3 * P2 + P0 + P5 + P7)

def f3(P0, P1, P2, P3, P4, P5, P6, P7, P8):
    return 2 * (-3 * P3 + P0)

def f4(P0, P1, P2, P3, P4, P5, P6, P7, P8):
    return 2 * (-2 * P4 + P1 + P8)

def f5(P0, P1, P2, P3, P4, P5, P6, P7, P8):
    return 2 * (-2 * P5 + P2 + P8)

def f6(P0, P1, P2, P3, P4, P5, P6, P7, P8):
    return 2 * (-2 * P6 + P3 + P1)

def f7(P0, P1, P2, P3, P4, P5, P6, P7, P8):
    return 2 * (-2 * P7 + P3 + P2)

def f8(P0, P1, P2, P3, P4, P5, P6, P7, P8):
    return 2 * (-2 * P8 + P4 + P5 + P6 + P7)

def ode_int(P, a, b):
    global mas_t, mas_P8, mas_P7, mas_P6, mas_P5, mas_P4, mas_P3, mas_P2, mas_P1, mas_P0
    t = np.linspace(a, b, 10000)
    res = odeint(f, P, t)
    print(res)
    print(len(res))
    for i in range(len(res)):
        mas_P0.append(res[i][0])
        mas_P1.append(res[i][1])
        mas_P2.append(res[i][2])
        mas_P3.append(res[i][3])
        mas_P4.append(res[i][4])
        mas_P5.append(res[i][5])
        mas_P6.append(res[i][6])
        mas_P7.append(res[i][7])
        mas_P8.append(res[i][8])
    mas_t = t

a = 0
b = 100

P = [1, 0, 0, 0, 0, 0, 0, 0, 0]
ode_int(P, a, b)

fig, axs = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(10)

axs.grid(color='black',
         linewidth=0.5,
         linestyle='--')
axs.axis([mas_t[0], mas_t[-1], 0, 1.1])
axs.plot(mas_t, mas_P0, 'r', label='P0', linewidth=2)
axs.plot(mas_t, mas_P1, 'g', label='P1', linewidth=2)
axs.plot(mas_t, mas_P2, 'b', label='P2', linewidth=2)
axs.plot(mas_t, mas_P3, 'y', label='P3', linewidth=2)
axs.plot(mas_t, mas_P4, 'pink', label='P4', linewidth=2)
axs.plot(mas_t, mas_P5, 'm', label='P5', linewidth=2)
axs.plot(mas_t, mas_P6, 'k', label='P6', linewidth=2)
axs.plot(mas_t, mas_P7, 'gold', label='P7', linewidth=2)
axs.plot(mas_t, mas_P8, 'plum', label='P8', linewidth=2)
axs.legend(loc='upper right')

plt.show()