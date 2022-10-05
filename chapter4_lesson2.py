# step 8
a = int(input())
if -1 < a < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")


# step 9
a = int(input())
if a <= -3 or a >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")


# step 10
a = int(input())
if -30 < a <= -2 or 7 < a <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")


# step 11
num = int(input())
if 1 <= (num // 1000) < 10 and (num % 7 == 0 or num % 17 == 0):
    print("YES")
else:
    print("NO")


# step 12
a, b, c = int(input()), int(input()), int(input())
if (a + b > c) and (a + c > b) and (b + c > a):
    print("YES")
else:
    print("NO")


# step 13
num = int(input())
if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print("YES")
else:
    print("NO")


# step 14
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == c or b == d:
    print("YES")
else:
    print("NO")


# step 15
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if b - d > 1 or c - a > 1 or d - b > 1 or a - c > 1:
    print("NO")
else:
    print("YES")
