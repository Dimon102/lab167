import math
from decimal import Decimal
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def f(P, t):
    P0, P1, P2, P3, P4, P5, P6, P7, P8 = P
    return [P0func(P0, P1, P2, P3),
            P1func(P0, P1, P4, P6),
            P2func(P0, P2, P5, P7),
            P3func(P0, P3),
            P4func(P1, P4, P8),
            P5func(P2, P5, P8),
            P6func(P1, P3, P6),
            P7func(P2, P3, P7),
            P8func(P4, P5, P6, P7, P8)]


def P0func(P0, P1, P2, P3):
    return 2 * (-3 * P0 + P1 + P2 + P3)

def P1func(P0, P1, P4, P6):
    return 2 * (-3 * P1 + P0 + P4 + P6)

def P2func(P0, P2, P5, P7):
    return 2 * (-3 * P2 + P0 + P5 + P7)

def P3func(P0, P3):
    return 2 * (-3 * P3 + P0)

def P4func(P1, P4, P8):
    return 2 * (-2 * P4 + P1 + P8)

def P5func(P2, P5, P8):
    return 2 * (-2 * P5 + P2 + P8)

def P6func(P1, P3, P6):
    return 2 * (-2 * P6 + P3 + P1)

def P7func(P2, P3, P7):
    return 2 * (-2 * P7 + P3 + P2)

def P8func(P4, P5, P6, P7, P8):
    return 2 * (-2 * P8 + P4 + P5 + P6 + P7)

def euler(P0, P1, P2, P3, P4, P5, P6, P7, P8, a, b, h, mas_x, mas_P0, mas_P1, mas_P2, mas_P3, mas_P4, mas_P5, mas_P6, mas_P7, mas_P8):
    x = a
    while x < b:
        P0 += (P0func(P0, P1, P2, P3) * h)
        P1 += (P1func(P0, P1, P4, P6) * h)
        P2 += (P2func(P0, P2, P5, P7) * h)
        P3 += (P3func(P0, P3) * h)
        P4 += (P4func(P1, P4, P8) * h)
        P5 += (P5func(P2, P5, P8) * h)
        P6 += (P6func(P1, P3, P6) * h)
        P7 += (P7func(P2, P3, P7) * h)
        P8 += (P8func(P4, P5, P6, P7, P8) * h)
        mas_P0.append(P0)
        mas_P1.append(P1)
        mas_P2.append(P2)
        mas_P3.append(P3)
        mas_P4.append(P4)
        mas_P5.append(P5)
        mas_P6.append(P6)
        mas_P7.append(P7)
        mas_P8.append(P8)
        mas_x.append(x)
        x += h

def func(vars: list, t):
    P0 = vars[0]
    P1 = vars[1]
    P2 = vars[2]
    P3 = vars[3]
    P4 = vars[4]
    P5 = vars[5]
    P6 = vars[6]
    P7 = vars[7]
    P8 = vars[8]
    return [P0func(P0, P1, P2, P3),
            P1func(P0, P1, P4, P6),
            P2func(P0, P2, P5, P7),
            P3func(P0, P3),
            P4func(P1, P4, P8),
            P5func(P2, P5, P8),
            P6func(P1, P3, P6),
            P7func(P2, P3, P7),
            P8func(P4, P5, P6, P7, P8)]

def solve():
    global P0, P1, P2, P3, P4, P5, P6, P7, P8, a, b, h
    a_x = np.arange(a, b, h)
    return odeint(func, [P0, P1, P2, P3, P4, P5, P6, P7, P8], a_x)


a = 0
b = 50
h = 0.0001
P0 = 1
P1 = 0
P2 = 0
P3 = 0
P4 = 0
P5 = 0
P6 = 0
P7 = 0
P8 = 0
mas_x = []
mas_P0 = []
mas_P1 = []
mas_P2 = []
mas_P3 = []
mas_P4 = []
mas_P5 = []
mas_P6 = []
mas_P7 = []
mas_P8 = []
a_x = []
a_mas_P0 = []
a_mas_P1 = []
a_mas_P2 = []
a_mas_P3 = []
a_mas_P4 = []
a_mas_P5 = []
a_mas_P6 = []
a_mas_P7 = []
a_mas_P8 = []

def make_plot():
    global a_x, a_mas_P0, a_mas_P1, a_mas_P2, a_mas_P3, a_mas_P4, a_mas_P5, a_mas_P6, a_mas_P7, a_mas_P8, result
    a_x = np.arange(a, b, h)
    for i in result:
        a_mas_P0.append(i[0])
        a_mas_P1.append(i[1])
        a_mas_P2.append(i[2])
        a_mas_P3.append(i[3])
        a_mas_P4.append(i[4])
        a_mas_P5.append(i[5])
        a_mas_P6.append(i[6])
        a_mas_P7.append(i[7])
        a_mas_P8.append(i[8])


euler(P0, P1, P2, P3, P4, P5, P6, P7, P8, a, b, h, mas_x, mas_P0, mas_P1, mas_P2, mas_P3, mas_P4, mas_P5, mas_P6, mas_P7, mas_P8)
print('Решение методом Эйлера')
print(f'P0 = {mas_P0[-1]}')
print(f'P1 = {mas_P1[-1]}')
print(f'P2 = {mas_P2[-1]}')
print(f'P3 = {mas_P3[-1]}')
print(f'P4 = {mas_P4[-1]}')
print(f'P5 = {mas_P5[-1]}')
print(f'P6 = {mas_P6[-1]}')
print(f'P7 = {mas_P7[-1]}')
print(f'P8 = {mas_P8[-1]}')
summ = mas_P0[-1] + mas_P1[-1] + mas_P2[-1] + mas_P3[-1] + mas_P4[-1] + mas_P5[-1] + mas_P6[-1] + mas_P7[-1] + mas_P8[-1]
print()

result = solve()
# print(result)
answers = result[-1]
answ_P0 = answers[0]
answ_P1 = answers[1]
answ_P2 = answers[2]
answ_P3 = answers[3]
answ_P4 = answers[4]
answ_P5 = answers[5]
answ_P6 = answers[6]
answ_P7 = answers[7]
answ_P8 = answers[8]

print('Решение при помощи модуля')
print(f'P0 = {answ_P0}')
print(f'P1 = {answ_P1}')
print(f'P2 = {answ_P2}')
print(f'P3 = {answ_P3}')
print(f'P4 = {answ_P4}')
print(f'P1 = {answ_P5}')
print(f'P2 = {answ_P6}')
print(f'P3 = {answ_P7}')
print(f'P4 = {answ_P8}')

fig, axs = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(10)

axs.grid(color='black',
                linewidth=1,
                linestyle='--')

axs.axis([mas_x[0], mas_x[-1], 0, 1.1])
axs.plot(mas_x, mas_P0, 'b', label='P0', linewidth=2)
axs.plot(mas_x, mas_P1, 'g', label='P1', linewidth=2)
axs.plot(mas_x, mas_P2, 'r', label='P2', linewidth=2)
axs.plot(mas_x, mas_P3, 'y', label='P3', linewidth=2)
axs.plot(mas_x, mas_P4, 'purple', label='P4', linewidth=2)
axs.plot(mas_x, mas_P5, 'gold', label='P5', linewidth=2)
axs.plot(mas_x, mas_P6, 'pink', label='P6', linewidth=2)
axs.plot(mas_x, mas_P7, 'm', label='P7', linewidth=2)
axs.plot(mas_x, mas_P8, 'k', label='P8', linewidth=2)
axs.legend(loc='upper right')

plt.show()

make_plot()
fig, axs = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(10)

axs.grid(color='black',
                linewidth=1,
                linestyle='--')

axs.axis([a_x[0], a_x[-1], 0, 1.1])
axs.plot(a_x, a_mas_P0, 'b', label='P0', linewidth=2)
axs.plot(a_x, a_mas_P1, 'g', label='P1', linewidth=2)
axs.plot(a_x, a_mas_P2, 'r', label='P2', linewidth=2)
axs.plot(a_x, a_mas_P3, 'y', label='P3', linewidth=2)
axs.plot(a_x, a_mas_P4, 'purple', label='P4', linewidth=2)
axs.plot(a_x, a_mas_P5, 'gold', label='P5', linewidth=2)
axs.plot(a_x, a_mas_P6, 'pink', label='P6', linewidth=2)
axs.plot(a_x, a_mas_P7, 'm', label='P7', linewidth=2)
axs.plot(a_x, a_mas_P8, 'k', label='P8', linewidth=2)
axs.legend(loc='upper right')

plt.show()
