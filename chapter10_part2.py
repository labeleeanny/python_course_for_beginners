# task 1
s = 'Python rocks!'
print(len(s))


# task 2
s = 'Python rocks!'
print(s[3])


# task 3
s = 'Python rocks!'
print(s[1:5])


# task 4
s = '    Python rocks!     '
print(s.strip())


# task 5
s = 'Python rocks!'
print(s.upper())


# task 6
s = 'Python rocks!'
print(s.replace('o', '@'))


# task 7
s = input()
for i in range(len(s)):
    if i % 3 != 0:
        print(s[i], end='')


# task 8
s = input()
print(s.replace('1', 'one'))


# task 9
s = input()
print(s.replace('@', ''))


# task 10
n = input()
if n.count('f') == 1:
    print('-1')
elif n.count('f') == 0:
    print('-2')
else:
    n = n.replace('f', ' ', 1)
    print(n.find('f'))


# task 11
s = input()
a = s.find("h")
b = s.rfind("h")
c = s[a+1:b]
s = s.replace(c, c[::-1])
print(s)
