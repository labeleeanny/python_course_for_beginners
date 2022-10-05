# step 5
a, b = int(input()), int(input())
counter = 0
for i in range(a, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        counter += 1
print(counter)


# step 6
n = int(input())
total = 0
for i in range(n):
    num = int(input())
    total += num
print(total)


# step 7
from math import log
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i ** (-1)
print(total - log(n))


# step 8
n = int(input())
total = 0
for i in range(1, n + 1):
    if (i ** 2 % 10 == 2) or (i ** 2 % 10 == 5) or (i ** 2 % 10 == 8):
        total = total + i
print(total)


# step 9
n = int(input())
total = 1
for i in range(1, n + 1):
    total = total * i
print(total)


# step 10
total = 1
for i in range(10):
    num = int(input())
    if num != 0:
        total *= num
print(total)


# step 11
n = int(input())
counter = 0
for i in range(1, n + 1):
    if n % i == 0:
        counter = counter + i
print(counter)


# step 12
n = int(input())
counter = 0
for i in range(n):
    if i % 2 == 0:
        counter += i + 1
    else:
        counter -= i + 1
print(counter)


# step 13
n = int(input())
total1 = 0
total2 = 0
for i in range(n):
    num = int(input())
    if num > total1:
        total2 = total1
        total1 = num
    elif total1 > num > total2:
        total2 = num
print(total1)
print(total2)


# step 14
counter = 0
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        counter = counter + 1
if counter == 10:
    print("YES")
else:
    print("NO")


# step 15
b = 0
a = 0
c = 1
n = int(input())
for i in range(n):
    if i == 0:
        c = c
    elif i > 0:
        a = b
        b = c
        c = a + b
    print(c, end=' ')
