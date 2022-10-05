# step 5
numbers = [8, 9, 10, 11]
s = [4, 5, 6]
numbers.remove(9)
numbers.insert(1, 17)
numbers.extend(s)
numbers.remove(8)
numbers.extend(numbers)
numbers.insert(3, 25)
print(numbers)


# step 6
n = []
for i in input().split():
    n.append(int(i))
a = n.index(max(n))
b = n.index(min(n))
n[a], n[b] = n[b], n[a]
print(*n)


# step 7
n = input().lower().split()
a, b, c = n.count('a'), n.count('an'), n.count('the')
print('Общее количество артиклей:', a + b + c)


# step 8
n = input()
n = n.replace('#', '')
n = int(n)
for i in range(n):
    s = input()
    if '#' in s:
        a = s.find('#')
        b = s.replace(s[a:], '')
        s = b.rstrip()
        print(s)
    else:
        print(s)


# step 11
n = input().split()
r = []
for i in n:
    r.append(int(i))
r.sort()
print(*r)
r.sort(reverse=True)
print(*r)
