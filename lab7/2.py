from scipy.integrate import odeint
import numpy as np


# Функция, задающая систему дифференциальных уравнений
def system(P, t):
    lambda_val = 2.0
    T = 0.5

    dP0dt = -lambda_val * P[0] + lambda_val * P[1] - 0.5 * P[0]
    dP1dt = 0.5 * P[0] - lambda_val * P[1] + lambda_val * P[2] - 0.5 * P[1]
    dP2dt = 0.5 * P[1] - lambda_val * P[2] + lambda_val * P[3] - 0.5 * P[2]
    dP3dt = 0.5 * P[2] - lambda_val * P[3] - 0.5 * P[3]

    return [dP0dt, dP1dt, dP2dt, dP3dt]


# Начальные условия
P0_0 = 1.0
P1_0 = P2_0 = P3_0 = 0.0
P0_init = [P0_0, P1_0, P2_0, P3_0]

# Временной интервал
t = np.linspace(0, 10, 100)  # Промежуток времени от 0 до 10 с с шагом 0.1

# Решение системы дифференциальных уравнений
P_solution = odeint(system, P0_init, t)

# Извлечение решения
P_0 = P_solution[:, 0]
P_1 = P_solution[:, 1]
P_2 = P_solution[:, 2]
P_3 = P_solution[:, 3]

# Вычисление коэффициента готовности
R = P_0 + P_1 + P_2 + P_3

# Вывод результатов
print("Вероятности состояний:")
print("P_0(t):", P_0)
print("P_1(t):", P_1)
print("P_2(t):", P_2)
print("P_3(t):", P_3)
print("Коэффициент готовности:")
print("R(t):", R)