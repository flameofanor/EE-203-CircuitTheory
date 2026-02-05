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
v = 30

ra = 70
rb = 30
rc = 12

rsum = ra + rb + rc

r1 = rb * rc / rsum
r2 = rc * ra / rsum
r3 = ra * rb / rsum

print("R1 = " + f"{r1:.2f}" + " \u03A9")
print("R2 = " + f"{r2:.2f}" + " \u03A9")
print("R3 = " + f"{r3:.2f}" + " \u03A9")

RAA = (2 + r1) * (20 + r2) / (20 + r2 + 2 + r1)
req = RAA + r3
print("Req = " + f"{req:.2f}" + " \u03A9")

i = v / req
print("i = " + f"{i:.2f}" + " A")



VAA = i * RAA
print("VAA = " + f"{VAA:.2f}" + " v")


va = i * r3
print("va = " + f"{va:.2f}" + " v")

#vj = VAA * 2 / (2 + r1)
#v1 = 30 - vj

#vi = VAA * 20 / ()

vj = (VAA) * r1 /( 2 + r1)  #oh my lord these parenthesis are gonna be the death of me i stg
v1 = vj + va
#print("vj = " + f"{vj:.2f}" + " v")
print("v1 = " + f"{v1:.2f}" + " v")

vi = (VAA) * r2 / (20 + r2)
v2 = vi + va
print("v2 = " + f"{v2:.2f}" + " v")


'''
vj = v * 2 / (2 + r1 + r3)
print("vj = " + f"{vj:.2f}" + " v")
va = v * r1 / (2 + r1 + r3)
print (va)

vi = v * 20 / (20 + r2 + r3)
print("vi = " + f"{vi:.2f}" + " v")
'''

