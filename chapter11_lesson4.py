# step 2
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
total = 0
for i in numbers:
    k = i ** 2
    total += k
print(total)


# step 3
n = int(input())
xs = []
qs = []
for i in range(1, n + 1):
    x = int(input())
    xs.append(x)
    q = x * x + 2 * x + 1
    qs.append(q)
print(*xs, sep='\n')
print()
print(*qs, sep='\n')


# step 4
n = int(input())
s = []
ls = []
for i in range(n):
    k = int(input())
    s.append(k)
for j in s:
    a = min(s)
    b = max(s)
    if j != a and j != b:
        ls.append(j)
print(*ls, sep='\n')


# step 5
n = int(input())
r = []
for i in range(n):
    ls = input()
    if ls not in r:
        r.append(ls)
print(*r, sep='\n')


# step 6
n = int(input())
r = []
for _ in range(n):
    y = input()
    r.append(y)
b = input()
for u in r:
    if b.lower() in u.lower():
        print(u)


# step 7
n = int(input())
s = []
s1 = []
for i in range(n):
    x = input()
    s.append(x)
k = int(input())
c = []
for j in range(k):
    x = input()
    c.append(x)
for ls in range(n):
    counter = 0
    for m in range(k):
        counter += 0
        if c[m].lower() in (s[ls].lower()):
            counter += 1
    if counter == k:
        print(s[ls])


# step 8
n = int(input())
s = []
r = []
t = []
for _ in range(n):
    p = int(input())
    if p < 0:
        s.append(p)
    elif p == 0:
        r.append(p)
    else:
        t.append(p)
print(*s, sep='\n')
print(*r, sep='\n')
print(*t, sep='\n')
