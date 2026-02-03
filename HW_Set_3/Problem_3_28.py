import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import e

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables

Vs = 18




ra = 2000 + 6000
rb = 9000 + 3000

req = (ra * rb) / (ra + rb)

i1 = Vs / ra
i2 = Vs / rb

vx_positive = i1 * 2000
vx_negative = i2 * 9000
vx = vx_negative - vx_positive


print(vx)