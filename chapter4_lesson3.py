# step 3
n, k = int(input()), int(input())
if n > k:
    print("NO")
elif k > n:
    print("YES")
else:
    print("Don't know")


# step 4
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print("Равносторонний")
elif a == b != c or a == c != b or b == c != a:
    print("Равнобедренный")
elif a != b != c:
    print("Разносторонний")


# step 5
a, b, c = int(input()), int(input()), int(input())
if b > a > c or c > a > b:
    print(a)
elif a > b > c or c > b > a:
    print(b)
elif a > c > b or b > c > a:
    print(c)


# step 6
a = int(input())
if a == 2:
    print(28)
elif a == 4 or a == 6 or a == 9 or a == 11:
    print(30)
else:
    print(31)


# step 7
a = int(input())
if a < 60:
    print("Легкий вес")
elif a < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")


# step 8
a, b, c = int(input()), int(input()), str(input())
if b != 0 and c == "/":
    print(a / b)
elif c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif b == 0 and c == "/":
    print("На ноль делить нельзя!")
else:
    print("Неверная операция")


# step 9
a, b = str(input()), str(input())
if (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
    print('фиолетовый')
elif (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
    print('оранжевый')
elif (a == 'синий' and b == 'желтый') or (a == 'желтый' and b == 'синий'):
    print(a)
else:
    print('ошибка цвета')


# step 10
a = int(input())
if a == 0:
    print("зеленый")
elif (a % 2 == 0) and a <= 10:
    print("черный")
elif 10 >= a > 0:
    print("красный")
elif (a % 2 == 0) and a <= 18:
    print("красный")
elif 18 >= a >= 11:
    print("черный")
elif (a % 2 == 0) and a <= 28:
    print("черный")
elif 28 >= a >= 19:
    print("красный")
elif (a % 2 == 0) and a <= 36:
    print("красный")
elif 36 >= a >= 29:
    print("черный")
else:
    print("ошибка ввода")


# step 11
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if b < c or d < a:
    print("пустое множество")
elif a < b and c < d:
    if b == c:
        print(c)
    elif a == d:
        print(d)
    elif (c > a or c == a) and (d > b or d == b):
        print(c, b)
    elif a > c and (d > b or d == b):
        print(a, b)
    elif b > d and c > a:
        print(c, d)
    else:
        print(a, d)
