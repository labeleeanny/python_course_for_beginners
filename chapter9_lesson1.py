# step 5
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])


# step 6
s = "In 2010, someone paid 10k Bitcoin for two pizzas"
for i in range(0, len(s)):
    if s[i] == 'w':
        print(s[i])


# step 7
n = input()
for i in range(0, len(n), 2):
    print(n[i])


# step 8
n = input()
for i in range(1, len(n) + 1):
    print(n[-i])


# step 9
n = input()
a = input()
c = input()
print(a[0], n[0], c[0], sep='')


# step 10
a = input()
count = 0
for i in a:
    count = count + int(i)
print(count)


# step 11
n = input()
s = 'Цифр нет'
for i in range(len(str(n))):
    if n[i] in '0123456789':
        s = 'Цифра'
        break
print(s)


# step 12
n = input()
count = 0
count1 = 0
for c in n:
    if c in '+':
        count += 1
    if c not in "*":
        continue
    count1 += 1
print('Символ + встречается', count, 'раз')
print('Символ * встречается', count1, 'раз')


# step 13
n = input()
count = 0
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        count += 1
print(count)


# step 14
n = input()
count = 0
count1 = 0
for c in n:
    if c in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        count += 1
    if c in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        count1 += 1
print('Количество гласных букв равно', count)
print('Количество согласных букв равно', count1)


# step 15
n = int(input())
s = ''
s2 = ''
while n != 0:
    digit = n % 2
    s = s + str(digit)
    n = n // 2
for i in range(len(s) - 1, -1, -1):
    s2 = s2 + s[i]
print(s2)
