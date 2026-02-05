import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import e

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables
v = 100


ra = 6 + (6 * 24 / (6+ 24))
rb = 10+10+20
rc = ra * rb / (ra + rb)
req = 2 + rc
print(req)
ig = v / req
print(ig)


ia = ig * rc / ra
print(ia)

io = ia * (6 * 24 / (6+ 24)) / 24
print(io) #booh yah baby
#v1 = v * 2 / req
#print(v1)


