import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt, log
from math import e
# f"{some_float:.2f}"
# print("R1 = " + f"{r1:.2f}" + " \u03A9")
# Omega = \u03A9
# Micro = \u00B5

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables

i_s = 0.06
r_eq = (1000 * 5000) / (6000)
va = i_s * r_eq
ia = va / 5000

#x = 0.01 * 50
#print(x / 4)

#y = (50 * 0.005)
#print(y)

L = -0.25 / log(0.25)
print(L)
t = 0.005

tau = L / 50  # L/R
print(tau)
phi = 0.005 / tau
#print(phi)

x = 0.01 * t
#print(x)



U = (0.01 ** 2 * L / 2)
print("U = " + f"{U * 1e6:.2f}" + " \u00B5J")

i_5ms = 0.01 * e ** (-1 / tau * t)
power = i_5ms ** 2 * 50


W = (x / (-2) * tau) * (1 - (e ** (-2 * t / tau)))
W_percent = W / (x / (-2) * tau)

# print((x / (2 * phi)))

print("Energy = " + f"{W * 1e6:.3f}" + " uW")
print("Energy = " + f"{W_percent * 100:.2f}" + "% ")

