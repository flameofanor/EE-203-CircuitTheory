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

ia = 0.006
ib = 0.0042

ra = 2300
rb = 1000
rc = 2700

va = ia * ra
vb = ib * rb

print("va = " + f"{va:.4f}" + " volts")
print("vb = " + f"{vb:.4f}" + " volts")

v = va + vb
r = ra + rb + rc

io = v / r
print("io = " + f"{io * 1e3:.5f}" + " mA")

### current division

v2 = (ia + ib) / (1 + 1/rc + 1/ra + rb/(ra+rc))
io2 = v2 / rc
print("v2 = " + f"{v2:.4f}" + " volts")
print("io2 = " + f"{io2 * 1e3:.8f}" + " mA")
