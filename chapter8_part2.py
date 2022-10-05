# task 1
n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)


# task 2
n = 8
count = 0
maximum = -(10 ** 12) - 1
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


# task 3
n = 4
count = 0
maximum = -(10 ** 8)
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


# task 4
n = 4
count = 0
maximum = -(10 ** 8)
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


# task 5
n = int(input())
while n > 99:
    b = n % 10
    n = n // 10
print(b)


# task 6
n = int(input())
count = 0
count1 = 0
count2 = 0
count3 = 0
total = 0
a = n % 10
multi = 1
while n > 0:
    b = n % 10
    if b == 3:
        count += 1
    if a == b:
        count1 += 1
    if b % 2 == 0:
        count2 += 1
    if b > 5:
        total += b
    if b > 7:
        multi *= b
    if b == 0 or b == 5:
        count3 += 1
    n //= 10
print(count)
print(count1)
print(count2)
print(total)
print(multi)
print(count3)
