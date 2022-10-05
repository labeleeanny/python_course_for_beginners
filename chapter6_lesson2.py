# step 5
print('"Python is a great language!", said Fred.' + ' "I ' + "don't " + 'ever remember having this much fun before."')


# step 6
a, b = input(), input()
c = ' '
print('Hello ' + a + c + b + '! ' + 'You just delved into Python')


# step 7
a = input()
b = len(a)
print('Футбольная команда' + ' ' + a + ' ' + 'имеет длину' + ' ' + str(b) + ' ' + 'символов')


# step 8
a, b, c = input(), input(), input()
d = len(a)
e = len(b)
f = len(c)
h = min(d, e, f)
i = max(d, e, f)
if h == d and i == e:
    print(a, b, sep='\n')
elif h == d and i == f:
    print(a, c, sep='\n')
elif h == e and i == d:
    print(b, a, sep='\n')
elif h == e and i == f:
    print(b, c, sep='\n')
elif h == e and i == d:
    print(b, a, sep='\n')
elif h == f and i == d:
    print(c, a, sep='\n')
else:
    print(c, b, sep='\n')


# step 9
a, b, c = len(input()), len(input()), len(input())
if (a + c) / 2 == b or (a + b) / 2 == c or (b + c) / 2 == a:
    print("YES")
else:
    print("NO")


# step 12
a = input()
b = "синий"
if b in a:
    print("YES")
else:
    print("NO")


# step 13
a = input()
b = 'суббота'
c = 'воскресенье'
if (b in a) or (c in a):
    print("YES")
else:
    print("NO")


# step 14
email = input()
a = "@"
b = "."
if (a in email) and (b in email):
    print("YES")
else:
    print("NO")
