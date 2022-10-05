# step 7
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])


# step 8
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])


# step 9
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])


# step 10
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])


# step 11
n = input()
if n[:] == n[::-1]:
    print('YES')
else:
    print('NO')


# step 12
n = input()
print(len(n))
print(n[:] * 3)
print(n[0])
print(n[:3])
print(n[-3:])
print(n[::-1])
print(n[1:-1])


# step 13
s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[0:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])


# step 14
s = input()
x = len(s)
a = x // 2 + x % 2
print(s[a:] + s[:a])
