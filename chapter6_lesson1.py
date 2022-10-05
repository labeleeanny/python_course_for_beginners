# step 3
a, b = float(input()), float(input())
print(1 / 2 * a * b)


# step 4
a, b, c = float(input()), float(input()), float(input())
print(a / (b + c))


# step 5
num = float(input())
if num == 0:
    print("Обратного числа не существует")
else:
    print(1 / num)


# step 6
a = float(input())
print(5 / 9 * (a - 32))


# step 7
age = int(input())
if age <= 2:
    print(age * 10.5)
else:
    print(21 + (age - 2) * 4)


# step 8
num = float(input())
a = (num * 10)
b = int(a % 10)
print(b)


# step 9
num = float(input())
a = int(num)
b = num - a
print(b)


# step 12
a, b, c, d, h = int(input()), int(input()), int(input()), int(input()), int(input())
e = min(a, b, c, d, h)
f = max(a, b, c, d, h)
print('Наименьшее число =', e)
print('Наибольшее число =', f)


# step 13
a, b, c = int(input()), int(input()), int(input())
d = max(a, b, c)
e = min(a, b, c)
if a == d and b == e:
    print(d, c, e, sep='\n')
elif a == d and c == e:
    print(d, b, e, sep='\n')
elif b == d and a == e:
    print(b, c, e, sep='\n')
elif b == d and c == e:
    print(d, a, e, sep='\n')
elif c == d and a == e:
    print(d, b, e, sep='\n')
else:
    print(d, a, e, sep='\n')


# step 14
num = int(input())
a = num // 100
b = (num // 10) % 10
c = num % 10
d = max(a, b, c)
e = min(a, b, c)
if d - e == a or d - e == b or d - e == c:
    print('Число интересное')
else:
    print('Число неинтересное')


# step 15
a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())
f = abs(a) + abs(b) + abs(c) + abs(d) + abs(e)
print(f)


# step 16
p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
pq1 = abs(p1 - q1)
pq2 = abs(p2 - q2)
print(pq1 + pq2)
