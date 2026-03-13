import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import e
# f"{some_float:.2f}"
# print("R1 = " + f"{r1:.2f}" + " \u03A9")

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables

v1 = 45
v2 = 25
r1 = 15000
r2 = 5000

i1 = v1 / r1
i2 = v2 / r2

rth = (v2-v1) / (i1-i2)
print("Rth = " + f"{rth / 1000:.0f}" + " k\u03A9")

