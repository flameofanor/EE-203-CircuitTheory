import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import e

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables
i = 2.4 
ra = 90 * 10  / ( 90 + 10)
rb = ra + 6
rc = 20 + 10
rd = rc * rb / (rc + rb)

v = i * rd
ia = v / rc
ib = v / rb

v0 = ia * 20
v1 = ia * 10

vb = ib * 6

#i0 = (24 - vb - 10 * ib) / 80
i0 = ib / 10
i1 = ib - i0

#print(i0 + i1 == ib)
#print(ib)

power = ib ** 2 * 6 
p_total = i * v

print(str(p_total) + " watts")

