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

i1 = 0.5 / 20000
i2 = 1.5 / 30000
i3 = -2.5 / 60000

i = i1 + i2 + i3


v0 = - 180000 * i
print(v0)

ig = i1 + i2
v3 = (0.00005 - ig) * 60000
v4 = (-0.00005 - ig) * 60000
print("Limits on Vc: " + f"{v4:.2f}" + " < Vc < " + f"{v3:.2f}")