# step 3
n = input()
e = n.split()
print(*e, sep='\n')


# step 4
n = input().split()
for i in range(len(n)):
    print(n[i][0], end='.')


# step 5
n = input().split('\\')
print(*n, sep='\n')


# step 6
s = input().split()
for i in s:
    print('+' * int(i))


# step 7
s = input().split('.')
for i in s:
    if int(i) < 0 or int(i) > 255:
        print('НЕТ')
        break
else:
    print('ДА')


# step 8
n, b = list(input()), input()
print(b.join(n))


# step 9
ls = input().split()
c = 0
for i in range(len(ls)):
    for j in range(i + 1, len(ls)):
        if ls[j] == ls[i]:
            c += 1
print(c)
