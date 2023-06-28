import numpy as np

import S23_1000, G9_67_2
import math
import matplotlib.pyplot as plt
import scipy. stats as stats
import scipy.integrate


def gamma(t):
    global x_mas, All_F_mas
    return 100*(All_F_mas[x_mas.index(t)])
    # return 100*(1 - integrate(a, t, St))
    #return 100*(1 - ((-(t*math.fabs(2*t-1023))/954529)+(1023*abs(2*t-1023))/1909058+(2*t)/977))

def intense(ind):
    global x_mas, All_mas, All_F_mas
    # print(f'{t} : {x_mas.index(t)} : {S_mas[x_mas.index(t)]} : {F_mas[x_mas.index(t)]} : {S_mas[x_mas.index(t)] / F_mas[x_mas.index(t)]}')
    # return diffs[x_mas.index(t)] / F_mas[x_mas.index(t)]
    if All_F_mas[ind] == 0:
        return 1
    return All_mas[ind] / All_F_mas[ind]
    # return S_mas[x_mas.index(t)] / F_mas[x_mas.index(t)]
    #return St(t) / F_mas[x_mas.index(t)]

def Et(t):
    return 1.5 * 10**(-4) * math.exp(-1.5 * 10**(-4) * t)

def Gt(t):
    return t**(k-1) * ((math.exp(-t/tetta)) / (tetta**k * gamm(k)))

def gamm(k):
    return math.factorial(k-1)

def E_F(t):
    global a
    return 1 - integrate(a, t, Et)

def get_func_values_by_index(func):
    global x_mas
    temp_mas = []
    for x_ind in range(len(x_mas)):
        temp_mas.append(func(x_ind))
    return temp_mas

def get_func_values_by_x(func):
    global x_mas
    temp_mas = []
    for x in x_mas:
        temp_mas.append(func(x))
    return temp_mas

def get_func_values(a, b, func): # не то
    global h
    temp_mas = []
    x = a
    while x <= b:
        temp_mas.append(func(x))
        x += h
    return temp_mas

def integrate(a, b, func):
    global h
    result = 0
    x = a
    while x <= b:
        result += func(x) * h
        x += h
    return result

def multiply(E_mas, S_mas, G_mas):
    global x_mas
    mult = []
    # print(S_mas)
    check = False
    for x_ind in range(len(x_mas)):
        # P = scipy.integrate.quad(lambda x: S23_1000.get_func_values_by_x(S23_1000.St), x_mas[0], x_mas[x_ind])[0]
        temp = E_mas[x_ind] * S_mas[x_ind] * G_mas[x_ind]
        mult.append(temp)
    return mult

a = 23
b = 1200
# b = 50
h = 0.1
k = 9
tetta = 67
x_mas = []
S_mas = []
G_mas = []
F_mas = []
All_mas = []
All_F_mas = []

def main():
    global a, b, h, x_mas, F_mas, S_mas, G_mas, All_mas, All_F_mas
    x = a
    while x <= b:
        x_mas.append(x)
        x += h
    S23_1000.main()
    G9_67_2.main()

    E_mas = get_func_values_by_x(Et)
    S_mas = S23_1000.S_mas #5. плотность распределения времени до отказа (St)
    G_mas = G9_67_2.G_mas #5. плотность распределения времени до отказа (St)

    # All_mas = multiply(E_mas, S_mas, G_mas)
    # F_mas = get_sum_mas(St) # 1. вероятность безотказной работы; (F)
    F_E_mas = get_func_values_by_x(E_F) # 1. вероятность безотказной работы; (F)
    F_S_mas = S23_1000.F_mas # 1. вероятность безотказной работы; (F)
    F_G_mas = G9_67_2.F_mas # 1. вероятность безотказной работы; (F)
    All_F_mas = multiply(F_E_mas, F_S_mas, F_G_mas) # 1. вероятность безотказной работы; (F)


    All_mas = np.diff(All_F_mas)
    All_mas = np.array((-1) * All_mas)
    All_mas = np.insert(All_mas, 0, All_mas[0])
    # for i in range(len(F_mas)):
    #     F_mas[i] = 1 - F_mas[i]
    #diffs = get_diffs(F_mas)
    # intense_mas = get_func_values_by_x(intense) # 4. интенсивность отказов
    intense_mas = get_func_values_by_index(intense) # 4. интенсивность отказов
    gammas_mas = get_func_values_by_x(gamma) # 6. гамма-процентную наработку до отказа (γ = 0,10,20,..., 100)
    # sum_mas = get_func_values(a, b, f_sum) ХЗ

    MO = stats.gamma.median(k, scale=tetta)
    print(f'Мат. ожидание = {MO}') #2. средняя наработка до отказа (среднее время безотказной работы) (M)
    # Disp = integrate(a, b, D)
    Disp = stats.gamma.var(k, scale=tetta)
    print(f'Дисперсия = {Disp}') # 3. дисперсию времени безотказной работы
    print(f'Ср. кв. отклонение = {math.sqrt(Disp)}') # 3. среднее квадратическое отклонение

    fig, axs = plt.subplots(nrows=4, ncols=1)
    fig.set_figwidth(10)
    fig.set_figheight(10)
    axs[0].plot(x_mas, All_mas, label='Плотность распределения')
    axs[1].plot(x_mas, All_F_mas, label='Вероятность безотказной работы')
    axs[2].plot(x_mas[:len(x_mas) - 1], intense_mas[:len(x_mas) - 1], label='Интенсивность отказов')
    axs[2].set_ylim([0, 1])
    axs[3].plot(gammas_mas, x_mas, label='Гамма-процентная наработка')
    # plt.plot(x_mas, intense_mas)
    # plt.plot(x_mas, M_mas)
    # plt.plot(x_mas, sum_mas) ХЗ
    for axs_i in axs:
        axs_i.legend(loc='upper right')
    plt.yscale('linear')
    plt.show()

'''
1. вероятность безотказной работы; (F)
2. средняя наработка до отказа (среднее время безотказной работы) (M)
3. среднее квадратическое отклонение и дисперсию времени безотказной работы
4. интенсивность отказов
5. плотность распределения времени до отказа (St)
6. гамма-процентную наработку до отказа (γ = 0,10,20,..., 100)
'''

if __name__ == "__main__":
    main()