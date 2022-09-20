array = [497.59, 497.61, 497.88, 497.99, 498.05, 498.11, 498.12, 498.13, 498.15, 498.17, 498.19, 498.21, 498.23, 498.27, 498.32, 498.32,
498.38, 498.4, 498.43, 498.43, 498.45, 498.46, 498.52, 498.52, 498.54, 498.57, 498.58, 498.62, 498.62, 498.63, 498.66, 498.67, 498.67,
498.69, 498.7, 498.72, 498.73, 498.73, 498.74, 498.76, 498.76, 498.78, 498.78, 498.79, 498.8, 498.84, 498.85, 498.86, 498.88, 498.9, 498.93,
498.94, 498.94, 498.98, 499.0, 499.03, 499.04, 499.1, 499.11, 499.11, 499.13, 499.15, 499.15, 499.16, 499.19, 499.2, 499.22, 499.25, 499.25,
499.27, 499.28, 499.29, 499.3, 499.31, 499.32, 499.33, 499.34, 499.35, 499.38, 499.38, 499.39, 499.43, 499.43, 499.43, 499.44, 499.44, 499.44,
499.44, 499.45, 499.46, 499.47, 499.47, 499.49, 499.51, 499.51, 499.52, 499.53, 499.54, 499.54, 499.55, 499.56, 499.56, 499.56, 499.57, 499.58,
499.58, 499.59, 499.61, 499.63, 499.63, 499.63, 499.66, 499.68, 499.68, 499.71, 499.75, 499.75, 499.76, 499.76, 499.77, 499.8, 499.81, 499.84,
499.85, 499.91, 499.91, 499.92, 499.92, 499.94, 499.95, 499.96, 499.97, 499.97, 499.97, 499.98, 499.99, 500.0, 500.01, 500.01, 500.03, 500.04,
500.05, 500.05, 500.06, 500.06, 500.08, 500.08, 500.08, 500.09, 500.09, 500.09, 500.11, 500.11, 500.14, 500.16, 500.17, 500.18, 500.18, 500.19,
500.19, 500.19, 500.23, 500.24, 500.26, 500.27, 500.28, 500.29, 500.29, 500.29, 500.3, 500.31, 500.31, 500.33, 500.33, 500.34, 500.34, 500.34,
500.35, 500.37, 500.41, 500.41, 500.41, 500.42, 500.43, 500.45, 500.52, 500.53, 500.53, 500.54, 500.55, 500.57, 500.57, 500.57, 500.57, 500.59,
500.59, 500.59, 500.6, 500.61, 500.61, 500.62, 500.62, 500.63, 500.63, 500.64, 500.66, 500.67, 500.68, 500.68, 500.69, 500.71, 500.71, 500.72,
500.73, 500.73, 500.73, 500.74, 500.81, 500.84, 500.86, 500.86, 500.88, 500.89, 500.9, 500.91, 500.92, 500.94, 500.94, 500.95, 501.02, 501.02,
501.1, 501.12, 501.19, 501.27, 501.27, 501.28, 501.29, 501.3, 501.35, 501.37, 501.42, 501.49, 501.5, 501.55, 501.69, 501.76, 501.85, 501.9, 501.95,
501.95, 501.97, 502.07, 502.09, 502.13, 502.17, 502.17, 502.17, 502.2, 502.37, 502.41, 502.43, 502.54, 502.66, 502.74, 502.75, 503.08, 503.28,
503.77, 505.48]
sum_of_array = sum(array)
ten = 1
for resist in array:
    print(resist, end = ' ')
    if ten == 15:
        print('\n')
        ten=0
    ten+=1

from matplotlib import pyplot as plt
import numpy as np
import math

#число частей
n = 10

#создаем массив и координатные оси
a = np.array(array)
fig, ax = plt.subplots(figsize=(10, 7))

#массив значений, которые будут отложены по 0y
array_for_raspr = [0 for i in range(n)]
dist = (max(array)-min(array))/n
for i in range(1, n+1):
    for resistanse in array:
        if resistanse>=min(array)+dist*(i-1) and resistanse <= min(array)+dist*i:
            array_for_raspr[i-1] += 1
for i in range(len(array_for_raspr)):
   array_for_raspr[i] = 1000*array_for_raspr[i]/(len(array)*dist)

#среднеквадратичные отклонения
sum = 0
for res in array:
    sum+=(res- sum_of_array/len(array))**2
razbros_2 = sum/len(array) #квадрат отклонения
razbros = razbros_2**0.5 #отклонение

srednee = sum_of_array/len(array)
x = np.linspace(497, 507, 1000)
y=(1/(math.sqrt(2*math.pi)*razbros))*(math.e**(-(((x-srednee)**2)/(2*razbros_2))))
for i in range(len(array)):
print(
    '<R> = ',
      round(sum_of_array/len(array), 2),
      ' m = ', round(dist, 2),
      ' sigma^2 = ', round(razbros_2, 2) ,
      ' sigma = ', round(razbros, 2) ,
      '\n',
      array_for_raspr
)

#строим гистограмму. density делает гистограмму плотности вероятности
ax.hist(array, bins=[min(array)+i*(max(array)-min(array))/n for i in range(n+1)], density = True, align = 'right')
ax.plot(x, y)
plt.xlabel('R, Ом')
plt.text(505, 0.35, f'⟨R⟩ = {round(srednee, 2)} Ом'+'\n'+f'σ = {round(razbros, 2)} Ом'+'\n'+fr'$σ^2$ = {round(razbros_2, 2)}'+r'$Ом^2$', fontsize=15)
plt.title(f'Гистограмма для m = {n}')
plt.ylabel('ω')
plt.axvline(x=sum_of_array/len(array), color = 'r', linestyle = '-.', linewidth = 0.4)
plt.axvline(x=sum_of_array/len(array) - razbros, color = 'b', linestyle = '-.', linewidth = 0.4)
plt.axvline(x=sum_of_array/len(array) + razbros, color = 'b', linestyle = '-.', linewidth = 0.4)
plt.axvline(x=sum_of_array/len(array) - 2*razbros, color = 'g', linestyle = '-.', linewidth = 0.4)
plt.axvline(x=sum_of_array/len(array) + 2*razbros, color = 'g', linestyle = '-.', linewidth = 0.4)
plt.axvline(x=sum_of_array/len(array) - 3*razbros, color = 'y', linestyle = '-.', linewidth = 0.4)
plt.axvline(x=sum_of_array/len(array) + 3*razbros, color = 'y', linestyle = '-.', linewidth = 0.4)
#plt.show()
plt.savefig(f'resistanse_with_{n}_points.png')