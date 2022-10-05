# step 6
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
           12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 and 17 in numbers:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)


# step 7
n = int(input())
list1 = []
for i in range(n):
    a = input()
    list1.append(a)
print(list1)


# step 8
n = []
for i in range(26):
    n.append(chr(ord('a') + i) * (i + 1))
print(n)


# step 9
n = int(input())
li = []
for i in range(n):
    r = int(input())
    li.append(r ** 3)
print(li)


# step 10
n = int(input())
ls = []
for i in range(1, n + 1):
    if n % i == 0:
        ls.append(i)
print(ls)


# step 11
n = int(input())
l, s = [], []
for i in range(n):
    l.append(int(input()))
    if i > 0:
        s.append(l[i] + l[i - 1])
print(s)


# step 12
n = int(input())
a = []
for i in range(n):
    r = int(input())
    a.append(r)
del a[1::2]
print(a)


# step 13
n, ls = int(input()), []
for _ in range(n):
    ls.append(input())
k = int(input())
for i in range(n):
    c = ls[i]
    if len(c) >= k:
        print(c[k - 1], end='')


# step 14
n = int(input())
y = []
for i in range(n):
    k = input()
    chars = list(k)
    y.extend(chars)
print(y)
