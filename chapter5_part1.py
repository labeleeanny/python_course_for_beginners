# task 1
num = int(input())
a = (num // 10) % 10
b = num % 10
if a == 0 and b == 0:
    print("YES")
else:
    print("NO")


# task 2
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if ((a + b) % 2 == 0) and ((c + d) % 2 > 0) or ((a + b) % 2 > 0) and ((c + d) % 2 == 0):
    print("NO")
else:
    print("YES")


# task 3
age, sex = int(input()), str(input())
if 10 <= age <= 15 and sex == "f":
    print("YES")
else:
    print("NO")


# task 4
a = int(input())
if a == 1:
    print("I")
elif a == 2:
    print("II")
elif a == 3:
    print("III")
elif a == 4:
    print("IV")
elif a == 5:
    print("V")
elif a == 6:
    print("VI")
elif a == 7:
    print("VII")
elif a == 8:
    print("VIII")
elif a == 9:
    print("IX")
elif a == 10:
    print("X")
else:
    print("ошибка")


# task 5
a = int(input())
if (a % 2 == 0 and 2 <= a <= 5) or (a % 2 == 0 and a > 20):
    print("NO")
else:
    print("YES")


# task 6
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if ((a + b) == (c + d)) or ((a - b) == (c - d)):
    print('YES')
else:
    print('NO')


# task 7
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (c - a == 1 or a - c == 1) and (b - d == 2 or d - b == 2) or ((b - d == 1 or d - b == 1) and (c - a == 2 or a - c == 2)):
    print("YES")
else:
    print("NO")


# task 8
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (c - a == 1 or a - c == 1) and (b - d == 2 or d - b == 2) or ((b - d == 1 or d - b == 1) and (c - a == 2 or a - c == 2)):
    print("YES")
else:
    print("NO")
