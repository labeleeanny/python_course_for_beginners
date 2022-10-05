# step 2
for i in range(10):
    print("Python is awesome!")


# step 3
a = input()
b = int(input())
for i in range(b):
    print(a)


# step 4
for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')


# step 5
num = int(input())
for i in range(num):
    print('*******************')


# step 7
a = input()
for i in range(10):
    print(i, a)


# step 8
num = int(input())
for i in range(num+1):
    print('Квадрат числа', i, 'равен', i ** 2)


# step 9
n = int(input())
for i in range(n + 1):
    print('*' * (n - i))


# step 10
m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, m)
    m = m + (m * p) / 100
