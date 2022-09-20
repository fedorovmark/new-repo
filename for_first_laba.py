import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *
from math import sqrt
kvadr_v = []
kvadr_i = []
array_x = [115.2, 107.5, 99.3, 93.8, 83.6, 78.6, 69.6, 63.2, 56.3, 45.9, 0.0]
array_y = [604.0, 564.0, 520.0, 492.0, 440.0, 409.0, 364.0, 332.0, 296.0, 240.0, 0.0]
array_x1 = [185.8, 175.0, 159.5, 150.7, 136.4, 125.4, 113.9, 101.5, 90.2, 74.5, 0.0]
array_y1 = [588.0, 556.0, 508.0, 480.0, 436.0, 400.0, 364.0, 324.0, 288.0, 236.0, 0.0]
array_x2 = [282.5, 261.3, 246.7, 224.6, 205.0, 186.0, 174.0, 155.7, 130.3, 113.5, 0.0]
array_y2 = [588.0, 544.0, 512.0, 468.0, 428.0, 388.0, 360.0, 324.0, 272.0, 236.0, 0.0]
for i in range(len(array_x2)):
     kvadr_i.append((array_x2[i]*0.001)**2)
     kvadr_v.append((array_y2[i]*0.001)**2)
R = 2.081
d = 0.36*0.001
l = 0.2
print(R*3.14*d*d/(4*l))

def magic_f(array_x, array_y):
     k = 0.01
     x = np.array(array_x)
     y = np.array(array_y)

     x_err = np.array([0.002*i+2*k for i in x])
     y_err = np.array([2.5 for i in y])

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
     plt.errorbar(x, y, xerr=x_err, yerr=y_err, linestyle='None', marker='')
     plt.plot(x_fit, y_fit, linewidth = 0.8)

magic_f(array_x, array_y)
magic_f(array_x1, array_y1)
magic_f(array_x2, array_y2)
plt.minorticks_on()
plt.grid(which='minor',
        color = 'r')
plt.grid(which='minor',
        color = 'r',
        linestyle = ':')
plt.grid()
plt.show()
plt.savefig('first_laba.png')
