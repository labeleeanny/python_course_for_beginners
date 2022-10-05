# step 7
n, m = int(input()), int(input())
for i in range(n, m + 1):
    print(i)


# step 8
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if n > m:
        print(i)
for i in range(m, n - 1, -1):
    if m > n:
        print(i)
    else:
        print(n)


# step 9
m, n = int(input()), int(input())
if m % 2 !=0:
    for i in range(m, n, -2):
        print(i)
else:
    for i in range(m - 1, n - 1, -2):
        print(i)


# step 10
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 15 == 0:
        print(i)
    elif i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)


# step 11
a = int(input())
for i in range(1, 11):
    print(a, "x", i, "=", a * i)
