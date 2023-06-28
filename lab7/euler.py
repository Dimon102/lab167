lambd = 2
T = 0.5
nu = 1 / T

''''
dP0/dt = λP1 - μP0 
dP1/dt = λP2 + μP0 - (λ + μ)P1 
dP2/dt = λP3 + μP1 - (2λ + μ)P2 
dP3/dt = μP2 - λP3
'''

def P0func(P0, P1, P2, P3):
    return lambd * P1 - nu * P0

def P1func(P0, P1, P2, P3):
    return lambd * P2 + nu * P0 - (lambd + nu) * P1

def P2func(P0, P1, P2, P3):
    return lambd * P3 + nu * P1 - (2*lambd + nu) * P2

def P3func(P0, P1, P2, P3):
    return nu * P2 - lambd * P3


def euler(P0, P1, P2, P3, a, b, h, mas_x, mas_P0, mas_P1, mas_P2, mas_P3):
    x = a
    while x < b:
        P0 += (P0func(P0, P1, P2, P3) * h)
        P1 += (P1func(P0, P1, P2, P3) * h)
        P2 += (P2func(P0, P1, P2, P3) * h)
        P3 += (P3func(P0, P1, P2, P3) * h)
        mas_P0.append(P0)
        mas_P1.append(P1)
        mas_P2.append(P2)
        mas_P3.append(P3)
        mas_x.append(x)
        x += h


a = 0
b = 50
h = 0.0001
P0 = 1
P1 = 0
P2 = 0
P3 = 0
mas_x = []
mas_P0 = []
mas_P1 = []
mas_P2 = []
mas_P3 = []

euler(P0, P1, P2, P3, a, b, h, mas_x, mas_P0, mas_P1, mas_P2, mas_P3)

print(f'P0 = {mas_P0[-1]}')
print(f'P1 = {mas_P1[-1]}')
print(f'P2 = {mas_P2[-1]}')
print(f'P3 = {mas_P3[-1]}')

sum = mas_P0[-1] + mas_P1[-1] + mas_P2[-1] + mas_P3[-1]
print(f'Сумма вероятностей = {sum}')

diff = 1 - sum
print(f'Разница = {diff}')

sum_ready = mas_P1[-1] + mas_P2[-1] + mas_P3[-1]
print(f'Коэффициент готовности = {sum_ready}')
