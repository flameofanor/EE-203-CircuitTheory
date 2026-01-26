import math


i = 9 / 1000 #amps
t = 40 * 3600 #seconds
v = 1.25 #avg volts

#power = i * (1.5 - m * (power(s)))
power = i * v * t
print(power)
print(math.e)

#print(i * 1.5 * s)

