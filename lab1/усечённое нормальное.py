from scipy.stats import truncnorm

# задаем параметры усеченного нормального распределения
# a - нижняя граница, b - верхняя граница
# loc - среднее, scale - стандартное отклонение
a, b = 385, 8649
mean, std = 5, 2
alpha = (a - mean) / std
beta = (b - mean) / std

# генерируем выборку размера 10000
samples = truncnorm.rvs(alpha, beta, loc=mean, scale=std, size=10000)

# вычисляем характеристики распределения
p_success = truncnorm.cdf(b, alpha, beta, loc=mean, scale=std) - \
            truncnorm.cdf(a, alpha, beta, loc=mean, scale=std)
mttf = truncnorm.mean(alpha, beta, loc=mean, scale=std)
std_mttf = truncnorm.std(alpha, beta, loc=mean, scale=std)
intensity = 1 / mttf
pdf = truncnorm.pdf(samples, alpha, beta, loc=mean, scale=std)
gamma_percentile = truncnorm.ppf(0.95, alpha, beta, loc=mean, scale=std)

# выводим результаты
print("Вероятность безотказной работы:", p_success)
print("Средняя наработка до отказа:", mttf)
print("Среднее квадратическое отклонение времени безотказной работы:", std_mttf)
print("Интенсивность отказов:", intensity)
print("Плотность распределения времени до отказа:", pdf)
print("Гамма-процентная наработка до отказа:", gamma_percentile)