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

i1 = 1.5 / 20000
print("i1 = " + f"{i1 * 1000:.4f}" + " mA")

v1 = -i1 * 160000
print("v1 = " + f"{v1 :.0f}" + " V")


v2 = -(3 / 20000 ) * 160000
print("v2 = " + f"{v2 :.0f}" + " V  *actually capped at -18 V because of opamp power source")

i3 = -1 / 20000
v3 = -i3 * 160000 + 2
print("v3 = " + f"{v3 :.0f}" + " V")

i4 = -2 / 200000
v4 = -i4 * 160000 + 6
print("v4 = " + f"{v4 :.0f}" + " V")

