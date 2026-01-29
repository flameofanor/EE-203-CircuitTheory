import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import e

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables
g1 = 2
g2 = 1/5
g3 = 1/8
g4 = 1/10
g5 = 1/20
g6 = 1/40

g_sum = g1 + g2 + g3 + g4 + g5 + g6

i = 40

i6 = (i * g6) / g_sum
print(i6)

i5 = (i * g5) / g_sum
print(i5)

i4 = (i * g4) / g_sum
print(i4)

i3 = (i * g3) / g_sum
print(i3)

i2 = (i * g2) / g_sum
print(i2)

i1 = (i * g1) / g_sum
print(i1)

print((i1 + i2+ i3 + i4 + i5 + i6) == i)
#nice!


