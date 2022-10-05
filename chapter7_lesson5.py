# step 4
num = int(input())
while num != 0:
    ld = num % 10
    num = num // 10
    print(ld)


# step 5
num = int(input())
while num != 0:
    ld = num % 10
    num = num // 10
    print(ld, end='')


# step 6
num = int(input())
maax = 0
miin = 9
while num > 0:
    ld = num % 10
    if ld > maax:
        maax = ld
    if ld < miin:
        miin = ld
    num = num // 10
print('Максимальная цифра равна', maax)
print('Минимальная цифра равна', miin)


# step 7
num = int(input())
n_sum = 0
n_count = 0
n_multip = 1
n_first = int(str(num)[0])
n_last = num % 10
n_sum_f_and_l = n_first + n_last
while num != 0:
    n = num % 10
    n_sum += n
    n_count += 1
    n_multip *= n
    num = num // 10
print(n_sum)
print(n_count)
print(n_multip)
print(n_sum / n_count)
print(n_first)
print(n_sum_f_and_l)


# step 8
a = int(input())
while a > 99:
    a = a // 10
b = a % 10
print(b)


# step 9
n = int(input())
flag = True
a = n % 10
while n != 0:
    if n % 10 != a:
        flag = False
    n = n // 10
if flag:
    print('YES')
else:
    print('NO')


# step 10
n = int(input())
flag = True
while n // 10 > 0:
    if n % 10 > ((n // 10) % 10):
        flag = False
    n = n // 10
if flag:
    print('YES')
else:
    print('NO')
