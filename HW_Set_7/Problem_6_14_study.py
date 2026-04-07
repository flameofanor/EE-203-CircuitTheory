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

# this is a practice problem for the exam
#problem variables

C = 0.6e-6

t = 0
dv_dt = 40 * e ** (-15000 * t) * (-15000 * sin(30000 * t) + 30000 * cos(30000 * t))
i_0 = dv_dt * C

print("initial current = " + f"{i_0:.2f}" + " A")


t = (pi / 80) / 1000
V_t = 40 * e ** (-15000 * t) * sin(30000 * t)
dv_dt = 40 * e ** (-15000 * t) * (-15000 * sin(30000 * t) + 30000 * cos(30000 * t))
p = C * dv_dt * V_t

print("power = " + f"{p * 1000:.2f}" + " mW")

w = 1/2 * C * V_t ** 2
print("energy stored = " + f"{w * 1e6:.2f}" + " \u00B5J")
