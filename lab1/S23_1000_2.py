import math
import matplotlib.pyplot as plt

def gamma(t):
    global x_mas, F_mas
    return 100*(F_mas[x_mas.index(t)])
    # return 100*(1 - integrate(a, t, St))
    #return 100*(1 - ((-(t*math.fabs(2*t-1023))/954529)+(1023*abs(2*t-1023))/1909058+(2*t)/977))

def intense(ind):
    global x_mas, S_mas, F_mas
    # print(f'{t} : {x_mas.index(t)} : {S_mas[x_mas.index(t)]} : {F_mas[x_mas.index(t)]} : {S_mas[x_mas.index(t)] / F_mas[x_mas.index(t)]}')
    # return diffs[x_mas.index(t)] / F_mas[x_mas.index(t)]
    return S_mas[ind] / (F_mas[ind])
    # return S_mas[x_mas.index(t)] / F_mas[x_mas.index(t)]
    #return St(t) / F_mas[x_mas.index(t)]

def get_diffs(mas):
    global h
    temp = []
    for i in range(len(mas) - 1):
        temp.append((math.fabs(mas[i] - mas[i+1])) / h)
    temp.append((mas[-1] - mas[-2]) / h)
    return temp

def get_plt(S_mas):
    global a, b, h
    plt_mas = []
    for x in range(len(S_mas) - 1):
        plt_mas.append((S_mas[x] - S_mas[x+1]) / h)
    plt_mas.append(0)
    return plt_mas

def D(t):
    return t**2*St(t) # работает лучше
    #return (t - M(t))**2 * St(t)

def M(t):
    return St(t) * t

def F(t):
    global a
    # return 1 - St(t)
    return 1 - integrate(a, t, St)

# def F(t):
#     global a
#     return 1 - integrate(a, t, St)
#     # return 1 - integrate(a, t, St)

def get_sum_mas(func):
    global x_mas, h
    temp = []
    prev = 0
    for x in x_mas:
        curr = prev + (func(x) * h)
        temp.append(curr)
        prev = curr
    return temp

def St(t):
    global a, b
    return S(a, b, t)

def S(a, b, t):
    return 2/(b-a) - (2/((b-a)**2)) * math.fabs(a + b - 2*t)
    # return (2 * (977-math.fabs(1023-2*t))) / (977**2)

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

a = 45
b = 6000
# a = 23
# b = 1000
# b = 50
h = 1
x_mas = []
S_mas = []
F_mas = []
diffs = []

def main():
    global a, b, h, x_mas, F_mas, S_mas, diffs
    x = a
    while x <= b:
        x_mas.append(x)
        x += h

    S_mas = get_func_values_by_x(St) #5. плотность распределения времени до отказа (St)
    # F_mas = get_sum_mas(St) # 1. вероятность безотказной работы; (F)
    F_mas = get_func_values_by_x(F) # 1. вероятность безотказной работы; (F)
    #diffs = get_diffs(F_mas)
    # intense_mas = get_func_values_by_x(intense) # 4. интенсивность отказов
    intense_mas = get_func_values_by_index(intense) # 4. интенсивность отказов
    gammas_mas = get_func_values_by_x(gamma) # 6. гамма-процентную наработку до отказа (γ = 0,10,20,..., 100)
    # sum_mas = get_func_values(a, b, f_sum) ХЗ

    MO = integrate(a, b, M)
    print(f'Мат. ожидание = {MO}') #2. средняя наработка до отказа (среднее время безотказной работы) (M)
    # Disp = integrate(a, b, D)
    Disp = integrate(a, b, D) - MO**2
    print(f'Дисперсия = {Disp}') # 3. дисперсию времени безотказной работы
    print(f'Ср. кв. отклонение = {math.sqrt(Disp)}') # 3. среднее квадратическое отклонение

    fig, axs = plt.subplots(nrows=4, ncols=1)
    fig.set_figwidth(10)
    fig.set_figheight(10)
    axs[0].plot(x_mas, S_mas, label='Плотность распределения')
    axs[1].plot(x_mas, F_mas, label='Вероятность безотказной работы')
    axs[2].plot(x_mas, intense_mas, label='Интенсивность отказов')
    axs[2].set_ylim([0, 1])
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