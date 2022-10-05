# step 3
count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p *= x
        count += 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')


# step 4
mx = -10**6 - 1
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
    if (x < 0) and x > mx:
        mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')


# step 5
s = 0
for _ in range(7):
    n = int(input())
    if n % 2 == 0:
        s += n
print(s)


# step 6
n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)


# step 7
n = int(input())
d = 0
while n > 0:
    d = n
    n //= 10
print(d)


# step 8
n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
