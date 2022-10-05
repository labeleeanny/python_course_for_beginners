# step 4
password_1, password_2 = input(), input()
if password_2 == password_1:
    print("Пароль принят")
else:
    print("Пароль не принят")


# step 5
number = int(input())
if number % 2 == 0:
    print("Четное")
else:
    print("Нечетное")


# step 6
num = int(input())
a = num // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10
if a + d == b - c:
    print("ДА")
else:
    print("НЕТ")


# step 7
age = int(input())
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")


# step 8
a, b, c = int(input()), int(input()), int(input())
if c == (b - a) + b:
    print("YES")
else:
    print("NO")


# step 9
a, b = int(input()), int(input())
if b > a:
    print(a)
else:
    print(b)


# step 10
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)


# step 11
age = int(input())
if age <= 13:
    print("детство")
elif 24 >= age >= 14:
    print("молодость")
elif 59 >= age >= 25:
    print("зрелость")
else:
    print("старость")


# step 12
a, b, c = int(input()), int(input()), int(input())
if a > 0 and b > 0 and c > 0:
    print(a + b + c)
elif (a > 0) and (b < 0) and c > 0:
    print(a + c)
elif (a > 0) and (b > 0) and c < 0:
    print(a + b)
elif (b > 0) and (a < 0) and c > 0:
    print(b + c)
elif (a > 0) and (b < 0) and c < 0:
    print(a)
elif (b > 0) and (a < 0) and c < 0:
    print(b)
elif (c > 0) and (a < 0) and b < 0:
    print(c)
elif (a < 0) and (b < 0) and c < 0:
    print(0)
