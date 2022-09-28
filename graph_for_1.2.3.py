import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *
from math import sqrt

array_x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
array_x = [x**2 for x in array_x]
array_y = [8.73,  8.90, 9.24, 9.96, 10.88, 12.11, 13.47, 15.20, 17.28]
proizv = []
for i in range(len(array_x)):
     proizv.append(array_x[i]*array_y[i])
kvadr_x = []
kvadr_y = []
for x in array_x:
     kvadr_x.append(x**2)
kvadr_x = sum(kvadr_x)/len(array_x)
for y in array_y:
     kvadr_y.append(y**2)
kvadr_y = sum(kvadr_y)/len(array_x)

xy = sum(proizv)/len(proizv)
x = sum(array_x)/len(array_x)
y = sum(array_y)/len(array_y)
print(sum(proizv), xy, x, y, kvadr_x, kvadr_y, proizv)
k = abs(xy-x*y)/abs(kvadr_x-x**2)
b = y - k*x

sigma_k = (1/sqrt(len(array_x)))*sqrt(abs((kvadr_y-y**2)/(kvadr_x-x**2)-k**2))
sigma_b = sigma_k*sqrt(abs(kvadr_x-x**2))
sigma_syst = b*sqrt(0.01**2+0.01/(49*49))
sigma_poln = sqrt(sigma_b**2 + sigma_syst**2)
print(round(k, 3), round(b, 3), round(sigma_k, 3), round(sigma_b, 3), round(sigma_syst, 3), round(sigma_poln, 3))

def magic_f(array_x, array_y):
     x = np.array(array_x)
     y = np.array(array_y)

     x_err = np.array([0.1 for i in x])
     y_err = np.array([0.09, 0.10, 0.10, 0.11, 0.12, 0.13, 0.15, 0.16, 0.19])

     def quad_func(p, x):
          m, c = p
          return m*x + c
     quad_model = Model(quad_func)
     data = RealData(x, y, sx=x_err, sy=y_err)
     odr = ODR(data, quad_model, beta0=[0., 1.])
     out = odr.run()
     out.pprint()
     x_fit = np.linspace(x[0], x[-1], 1000)
     y_fit = quad_func(out.beta, x_fit)
     plt.errorbar(x, y, xerr=x_err, yerr=y_err, linestyle='None', marker='.')
     plt.plot(x_fit, y_fit, linewidth = 0.8)

# magic_f(array_x, array_y)
# plt.grid()
# plt.show()
