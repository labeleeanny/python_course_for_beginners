# step 2
from math import *
a, b, c, d = float(input()), float(input()), float(input()), float(input())
e = pow((a - c), 2)
f = pow((b - d), 2)
print(sqrt(e + f))


# step 3
import math
a = float(input())
b = (math.pi * (pow(a, 2)))
c = 2 * math.pi * a
print(b, c, sep='\n')


# step 4
from math import *
a, b = float(input()), float(input())
c = (a + b) / 2
d = sqrt(a * b)
e = (2 * a * b) / (a + b)
f = sqrt(((pow(a, 2)) + (pow(b, 2))) / 2)
print(c, d, e, f, sep='\n')


# step 5
from math import *
a = float(input())
c = (a * pi) / 180
e = tan(c)
b = sin(c) + cos(c) + (pow(e, 2))
print(b)


# step 6
from math import *
num = float(input())
print(floor(num) + ceil(num))


# step 7
from math import *
a, b, c = float(input()), float(input()), float(input())
d = pow(b, 2) - (4 * a * c)
if d < 0:
    print("Нет корней")
elif d == 0:
    print(- b / (2 * a))
elif d > 0:
    x1 = (- b - sqrt(d)) / (2 * a)
    x2 = (- b + sqrt(d)) / (2 * a)
    print(min(x1, x2), sep='\n')
    print(max(x1, x2), sep='\n')


# step 8
from math import *
n, a = float(input()), float(input())
s = (n * pow(a, 2)) / (4 * tan(pi / n))
print(s)
