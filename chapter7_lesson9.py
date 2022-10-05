# step 1
n = int(input())
counter = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        counter += 1
        print(counter, end=' ')
    print()


# step 2
num = int(input())
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for k in range(i - 1, 0, -1):
        print(k, end='')
    print()


# step 3
a, b = int(input()), int(input())
total_maximum = 0
digit = 0

for i in range(a, b + 1):
    maximum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            maximum += j
        if maximum >= total_maximum:
            total_maximum = maximum
            digit = j
print(digit, total_maximum)


# step 4
n = int(input())
for i in range(1, n + 1):
    print(i, end='')
    for j in range(1, i + 1):
        if i % j == 0:
            print('+', end='')
    print()


# step 5
n = int(input())
while n // 10 > 0:
    n = n // 10 + n % 10
print(n)


# step 6
n = int(input())
a = 1
b = 0
for i in range(1, n + 1):
    a *= i
    b += a
print(b)


# step 7
a, b, = int(input()), int(input())
for i in range(a, b + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        