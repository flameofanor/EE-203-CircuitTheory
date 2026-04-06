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

C = 250e-9
i1 = 50e-3 / 10e-6

i2 = 50e-3

t = 30e-6
v_30 = i2 * t / C  - i2 * 10e-6 / C
v_10 = i1 * (10e-6 ** 2) / (2 * C)
#print("V at 30 uS = " + f"{v_30:.2f}" + " volts")

charge = (v_30 + v_10) * C
print("Charge at 30 uS = " + f"{charge * 1e6:.9f}" + " uC")

