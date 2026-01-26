import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import e

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables

a = (120 * 360) / (120 + 360)
a += 90

b = (360 * a) / (360 + a)
#print(b)

p = (0.03 ** 2) * b
#print(p)

##################

c = (20*15)/(20+15)
d = (20*c)/(20+c)
e = (4*d)/(4+d)
f = (12*e)/(12+e)
g = 16 + f
h = (16 * g) / (16 + g)
j = h + 8 + 10
print(j)

P = 144 ** 2 / j
print(str(P) + " watts")


