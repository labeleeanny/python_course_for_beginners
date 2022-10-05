# step 5
n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()


# step 6
n = int(input())
for i in range(1, n + 1):
    for _ in range(5):
        print(i, end=' ')
    print()


# step 7
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()


# step 8
n = int(input())
for i in range(1, n // 2 + 2):
    print('*' * i)
for j in range(n//2, 0, -1):
    print('*' * j)


# step 9
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(i, end='')
    print()
