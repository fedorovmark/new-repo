import math
from math import sqrt
g=9.81
R = 114.6 #мм
dR=0.5#мм
r = 30.5#мм
dr=0.3#мм
m=668.2+669.1+934.7#г
dm=0.6#г
z0=216.9#см
dz0=0.15#см
k = (g*(R/(10**3))*(r/(10**3)))/(4*(math.pi**2)*(z0/(10**2)))
dk = sqrt((dR/R)**2+(dr/r)**2+(dz0/z0)**2)*k
period = 4.36
periods = [period, period, period, period]
sum_sqrt=0
N=len(periods)
for i in range(N):
    sum_sqrt+=(sum(periods)/len(periods) - periods[i])**2
T=sum(periods)/len(periods)
dT = sqrt((1/(N*(N-1)))*sum_sqrt)
print(dk*10000,k*10000,dm,m,dT,T)

I=(4*(10**-4)*(m/1000)*T*T)*1000

print(I, I*sqrt((dk/k)**2+(dm/m)**2+2*(dT/T)**2))