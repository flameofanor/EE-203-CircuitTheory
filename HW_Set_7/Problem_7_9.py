import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt, log
from math import e
# f"{some_float:.2f}"
# print("R1 = " + f"{r1:.2f}" + " \u03A9")

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables

L = 20e-3
t = 10e-6

i_initial = 10

U = 0.5 * L * i_initial ** 2

R = -L * log(sqrt(U/L) / 10) / t
print("R = " + f"{R:.2f}" + " \u03A9")


