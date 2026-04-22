import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt, log
from math import e
# f"{some_float:.2f}"
# print("R1 = " + f"{r1:.2f}" + " \u03A9")

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables

r1 = 15e3
r2 = 20e3
r3 = 40e3

c1 = 5e-6
c2 = 1e-6
r_sum = r1 + r2 + r3

V = 15

v1 = (r2 * V) / r_sum
print(v1)

v2 = (r3 * V) / r_sum
print(v2)

tau = r2 * c1
print(1/tau)

