# step 3
def get_middle_point(x1, y1, x2, y2):
    a1 = (x_1 + x_2) / 2
    b1 = (y_1 + y_2) / 2
    return a1, b1


x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)


# step 4
from math import pi


def get_circle(radius):
    c1 = 2 * pi * r
    len1 = pi * (pow(r, 2))
    return c1, len1


r = float(input())

length, square = get_circle(r)
print(length, square)


# step 5
from math import *


def solve(a1, b1, c1):
    d = pow(b1, 2) - (4 * a1 * c1)
    if d > 0:
        y1 = (- b1 - sqrt(d)) / (2 * a1)
        z = (- b1 + sqrt(d)) / (2 * a1)
        return min(y1, z), max(y1, z)
    if d == 0:
        y1 = (- b1 - sqrt(d)) / (2 * a1)
        z = (- b1 + sqrt(d)) / (2 * a1)
        return y1, z


a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)
