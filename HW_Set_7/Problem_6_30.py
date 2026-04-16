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

c1 = (8 * 32) / 40
c2 = 5.6 + c1
c3 = (c2 * 18) / (c2 + 18)
c4 = c3 + 12.8

c = 1 / (1/c4 + 1/8 + 1/40)
print("capacitance = " + f"{c:.2f}" + " nF")

c1 = (21 * 28) / (49)
c2 = 24 + c1
c3 = (c2 * 36) / (c2 + 36)
c4 = c3 + 14
c = (32 * c4) / (32 + c4)
print("capacitance = " + f"{c:.2f}" + " uF")



