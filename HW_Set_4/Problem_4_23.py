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

v1 = 53.125

i1 = v1 / 5000
print(i1)

i2 = v1 / 500
print(i2)


i4 = (i2 - i1 + 0.01) * -1
print(i4)

i5 = 80 / 4000

i3 = -1 * (i5 - 0.01 - i4)

print(i3)