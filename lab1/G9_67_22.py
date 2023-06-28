import math
import matplotlib.pyplot as plt
import scipy.stats as stats


def gamma(t):
    global x_mas, F_mas
    return 100*(F_mas[x_mas.index(t)])
    # return 100*(1 - integrate(a, t, St))
    #return 100*(1 - ((-(t*math.fabs(2*t-1023))/954529)+(1023*abs(2*t-1023))/1909058+(2*t)/977))

def intense(ind):
    global x_mas, G_mas, F_mas
    # print(f'{t} : {x_mas.index(t)} : {S_mas[x_mas.index(t)]} : {F_mas[x_mas.index(t)]} : {S_mas[x_mas.index(t)] / F_mas[x_mas.index(t)]}')
    # return diffs[x_mas.index(t)] / F_mas[x_mas.index(t)]
    return G_mas[ind] / (F_mas[ind])
    # return S_mas[x_mas.index(t)] / F_mas[x_mas.index(t)]
    #return St(t) / F_mas[x_mas.index(t)]

# def get_diffs(mas):
#     global h
#     temp = []
#     for i in range(len(mas) - 1):
#         temp.append((math.fabs(mas[i] - mas[i+1])) / h)
#     temp.append((mas[-1] - mas[-2]) / h)
#     return temp

# def get_plt(S_mas):
#     global a, b, h
#     plt_mas = []
#     for x in range(len(S_mas) - 1):
#         plt_mas.append((S_mas[x] - S_mas[x+1]) / h)
#     plt_mas.append(0)
#     return plt_mas

# def D(t):
#     return t ** 2 * Gt(t) # работает лучше
#     #return (t - M(t))**2 * St(t)
#
# def M(t):
#     return Gt(t) * t

# def F(t):
#     global a
#     # return 1 - St(t)
#     return 1 - integrate(a, t, Gt)

# def F(t):
#     global a
#     return 1 - integrate(a, t, St)
#     # return 1 - integrate(a, t, St)

# def get_sum_mas(func):
#     global x_mas, h
#     temp = []
#     prev = 0
#     for x in x_mas:
#         curr = prev + (func(x) * h)
#         temp.append(curr)
#         prev = curr
#     return temp

def Gt(t):
    return t**(k-1) * ((math.exp(-t/tetta)) / (tetta**k * gamm(k)))

def gamm(k):
    return math.factorial(k-1)

def get_func_values_by_index(func):
    global x_mas, h
    temp_mas = []
    for x_ind in range(len(x_mas)):
        temp_mas.append(func(x_ind))
    return temp_mas

def get_func_values_by_x(func):
    global x_mas, h
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

a = 75
b = 1300
# b = 50
h = 0.1
k = 9
tetta = 67
x_mas = []
G_mas = []
F_mas = []
diffs = []

def main():
    global a, b, h, x_mas, F_mas, G_mas, diffs
    x = a
    while x <= b:
        x_mas.append(x)
        x += h

    G_mas = stats.gamma.pdf(x_mas, a=k, scale=tetta) #5. плотность распределения времени до отказа (St)
    # F_mas = get_sum_mas(St) # 1. вероятность безотказной работы; (F)
    F_mas = stats.gamma.cdf(x_mas, a=k, scale=tetta) # 1. вероятность безотказной работы; (F)
    for i in range(len(F_mas)):
        F_mas[i] = 1 - F_mas[i]
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
    axs[0].plot(x_mas, G_mas, label='Плотность распределения')
    axs[1].plot(x_mas, F_mas, label='Вероятность безотказной работы')
    axs[2].plot(x_mas, intense_mas, label='Интенсивность отказов')
    # axs[2].set_ylim([0, 1])
    axs[3].plot(gammas_mas, x_mas, label='Гамма-процентная наработка')
    # plt.plot(x_mas, intense_mas)
    # plt.plot(x_mas, M_mas)
    # plt.plot(x_mas, sum_mas) ХЗ
    for axs_i in axs:
        axs_i.legend(loc='upper right')
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