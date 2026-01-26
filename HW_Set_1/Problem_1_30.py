import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import e

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables

volts_amps = [
	[-3, -250],
	[4, -400],
	[1, 400],
	[1, 150],
	[-4, 200],
	[4, 50]
]

def power():
	total = 0
	for row in volts_amps:
		total += row[0] * row[1]
	return total

print(power())
#gives -900 indicating that power is not balanced, fails power check.

