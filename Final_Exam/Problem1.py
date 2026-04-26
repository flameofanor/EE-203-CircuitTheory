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
r1 = 200
r2 = 600
r3 = 400
r4 = 1000
L = 100e-3
C = 400e-9

V1 = -160
V2 = -60

ri = r1 + r3


iL_initial = V1 / (ri + r4)


vC_inital = V1 * ri / (ri + r4)

# final state
R = 1000

Neper_frequency = R / (2 * L)
Resonant_frequency = 1 / (sqrt(L * C))

print(Neper_frequency ** 2 == Resonant_frequency ** 2) #true, therefore critically damped
