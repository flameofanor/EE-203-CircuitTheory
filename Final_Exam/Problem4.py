import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt, log
from math import e, pi
# f"{some_float:.2f}"
# print("R1 = " + f"{r1:.2f}" + " \u03A9")
# Omega = \u03A9
# Micro = \u00B5

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

''' unit conversions:
F to pF x * 1e12
F to nF x * 1e9
F to uF x * 1e6
F to mF x * 1e3
mF to F x * 1e-3
uF to F x * 1e-6
nF to F x * 1e-9
pF to F x * 1e-12
'''

#problem variables

L = 10e-3
C = 1e-6
w = 10000

R1 = w * L
print(R1) #100j

R2 = -1 / (C * w)
print(R2) #-100j

x = sqrt(160**2 + 100**2)
print(x)