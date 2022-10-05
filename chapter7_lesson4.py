# step 8
word = input()
while word != "КОНЕЦ":
    print(word)
    word = input()


# step 9
text = input()
while text != 'КОНЕЦ' and text != "конец":
    print(text)
    text = input()


# step 10
a = input()
counter = 0
while a != 'стоп' and a != 'хватит' and a != 'достаточно':
    a = input()
    counter += 1
print(counter)


# step 11
a = int(input())
while a % 7 == 0:
    print(a)
    a = int(input())


# step 12
a = int(input())
total = 0
while a >= 0:
    total += a
    a = int(input())
print(total)


# step 13
a = int(input())
counter = 0
while 0 < a <= 5:
    if a == 5:
        counter += 1
    a = int(input())
print(counter)


# step 14
a = int(input())
counter = 0
while a != 0:
    if a >= 25:
        a = a - 25
    elif a >= 10:
        a = a - 10
    elif a >= 5:
        a = a - 5
    elif a >= 1:
        a = a - 1
    counter += 1
print(counter)
