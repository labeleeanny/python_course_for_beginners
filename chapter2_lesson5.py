# step 6
a, b, c = int(input()), int(input()), int(input())
print(a * b ** (c - 1))


# step 7
a = int(input())
print(a // 100)


# step 8
n, k = int(input()), int(input())
print(k // n)
print(k % n)


# step 9
n = int(input())
print((n + 1) // 2)


# step 10
a = int(input())
print((a + 3) // 4)


# step 11
a = int(input())
b = a // 60
print(a, "мин - это", b, "час", a - (b * 60), "минут.")


# step 13
num = int(input())
last_num = num % 10
second_num = (num % 100) // 10
first_num = num // 100
print("Сумма цифр =", first_num + second_num + last_num)
print("Произведение цифр =",  first_num * second_num * last_num)


# step 14
n = int(input())
x = n // 100
y = (n // 10) % 10
c = n % 10
print(x, y, c, sep='')
print(x, c, y, sep='')
print(y, x, c, sep='')
print(y, c, x, sep='')
print(c, x, y, sep='')
print(c, y, x, sep='')


# step 15
m = int(input())
m1 = m // 1000
m2 = (m // 100) % 10
m3 = (m // 10) % 10
m4 = m % 10
print("Цифра в позиции тысяч равна", m1)
print("Цифра в позиции сотен равна", m2)
print("Цифра в позиции десятков равна", m3)
print("Цифра в позиции единиц равна", m4)
