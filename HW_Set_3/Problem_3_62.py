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
ra = 20 * 60 / (20 + 60)
rb = ra + 20
rc = 30 + (rb * 280) / (rb + 280)
rd = rc * 75 / (rc + 75)
req = rd + 10

v = 300
i = v / req
print("Req = " + f"{req:.2f}" + " \u03A9")
print("Rb = " + f"{rb:.2f}" + " \u03A9")

v3 = v * 10 / req
print("v3 = " + f"{v3:.2f}" + " v")

io = i * rd / 75
print("io = " + f"{io:.2f}" + " A")

ig = i - io
rm = (rb * 280) / (rb + 280)
im = ig * rm / 280
print("im = " + f"{im:.2f}" + " A")

power = im ** 2 * 280
print("\npower = " + f"{power:.2f}" + " watts")



