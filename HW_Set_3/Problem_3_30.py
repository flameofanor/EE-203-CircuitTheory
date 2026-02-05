import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import e

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables
ra = 150 * 75 / (150 + 75)
rb = (ra + 40) * (90) / (ra + 40 + 90)
req = 90 + rb
print(req)

v = 3
i = v / req
print(i)
va = i * 90
print(va)


v1 = ra / (ra + 40)
print(v1)
#print((40 / (ra + 40)) + v1 == 1) #yay!

v2 = 30 / 90
print(v2)




#incorrect below this
#v1 = v * ra / req
#print(v1)

#v3 = v * 90/ req
#print(v3)