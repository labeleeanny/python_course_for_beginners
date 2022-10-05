# step 8
s = input()
x = len(s)
a = x // 2 + x % 2
print(s[a:] + s[:a])


# step 9
n = input()
print(n.swapcase())


# step 10
s = input()
if 'хорош' in s.lower():
    print('YES')
else:
    print('NO')


# step 11
s, counter = input(), 0
for i in s:
    if i != i.upper():
        counter += 1
print(counter)
